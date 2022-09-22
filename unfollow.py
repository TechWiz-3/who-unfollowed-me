#!/usr/bin/env python3

import os
import requests
import time
import json
import threading

HOME = os.path.expanduser("~")
stop_threads = False
stop_spinner = True

# note to self: remember to make the ~/.unfollow dir in the program

def get_user():
    global stop_spinner
    # if the username has been configured
    if os.path.exists(f"{HOME}/.test.unfollow/user.txt"):
        with open(f"{HOME}/.test.unfollow/user.txt") as user_file:
            user = user_file.readlines()
        return user[0]
    # first run
    else:
        if not os.path.exists(f"{HOME}/.test.unfollow"):
            os.mkdir(f"{HOME}/.test.unfollow")  # create directory
        stop_spinner = True
        user = input("What is your github username: ")
        # todo: verify the user exists
        with open(f"{HOME}/.test.unfollow/user.txt", "w") as user_file:
            user_file.write(user)
        get_followers(user, write_file=True, overwrite=True)
        return None


def write_followers(payload):
    if os.path.exists(f"{HOME}/.test.unfollow/followers.json"):
        pass
    else:
        #with open(f"{HOME}/.unfollow/followers.json", "w") as follower_file:
        #    folower_file.write(payload, "\n")
        pass
    with open(f"{HOME}/.test.unfollow/followers.json", "a") as follower_file:
        follower_file.write(f"{payload}\n")


def get_followers(username, write_file=False, overwrite=False):
    if overwrite:
        # empty the followers file before filling it
        open(f'{HOME}/.test.unfollow/followers.json', 'w').close()

    total_followers = []
    #username = "ahmadawais"
    #username = "constantinrazvan"
    page = 1
    TOKEN = "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"
    headers = {'Authorization': 'token ' + TOKEN}
    while True:
        raw_data = requests.get(f"https://api.github.com/users/{username}/followers?page={page}&per_page=100", headers=headers)
        if raw_data.json() == []:
           # empty data, breaking now
           break
        if write_file == True:
            # write to file
            for user_object in raw_data.json():
                write_followers(user_object["login"])
        total_followers.append(raw_data.json())
        page += 1
    return total_followers


def get_unfollows(username):
    """compare json"""
    unfollowers = []
    current_followers = []
    previous_followers = []  # read from the file before being changed
    with open(f"{HOME}/.test.unfollow/followers.json") as follower_file:
       for follower in follower_file:
           previous_followers.append(follower)

    open(f'{HOME}/.test.unfollow/followers.json', 'w').close()

    get_followers(username, write_file=True)

    with open(f"{HOME}/.test.unfollow/followers.json") as follower_file:
       for follower in follower_file:
           current_followers.append(follower)

    # compare
    for old_follower in previous_followers:
        result = scan_follows(old_follower, current_followers)
        if result != True:
            unfollowers.append((result,f"https://github.com/{result}/"))
    return unfollowers


def scan_follows(old_follower, current_followers):
    for current_follower in current_followers:
        if old_follower == current_follower:
            old_follower = old_follower.replace("\n", "")
            # user found
            return True
    old_follower = old_follower.replace("\n", "")
    return old_follower


def run_unfollow():
    username = get_user()
    if username == None:
        stop_threads = True
        return "first"
    else:
        stop_threads = True
        return get_unfollows(username)


def main():
    global stop_threads
    while True:
        if stop_threads:
            time.sleep(1)  # give time for functions to exit
            break


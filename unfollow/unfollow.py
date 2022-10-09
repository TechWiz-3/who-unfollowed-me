#!/usr/bin/env python3

import os
import sys
import time
import requests
import concurrent.futures

from rich.status import Status

from unfollow.input import get_input_username

HOME = os.path.expanduser("~")
UNFOLLOW_PATH = f"{HOME}/.unfollow"

if "--test" in sys.argv:
    UNFOLLOW_PATH = f"{HOME}/.test.unfollow"

if "--token" in sys.argv:
    print("yes")
    TOKEN = os.getenv("UNFOLLOW_TOKEN")
    try:
        HEADERS = {'Authorization': f'token {TOKEN}'}
    except TypeError:
        print("Error: UNFOLLOW_TOKEN not found. Maybe refresh your terminal?")
        sys.exit(1)
else:
    TOKEN = ""
    HEADERS = {}

threads_stopped = False  # used to stop spinner thread
stop_spinner = None  # none, true, false

executor = concurrent.futures.ThreadPoolExecutor()


def get_user() -> tuple:
    global stop_spinner
    # if the username has been configured
    if os.path.exists(f"{UNFOLLOW_PATH}/user.txt"):
        with open(f"{UNFOLLOW_PATH}/user.txt") as user_file:
            user = user_file.readlines()
        return ("regular", user[0])
    # first run
    else:
        if not os.path.exists(f"{UNFOLLOW_PATH}"):
            os.mkdir(f"{UNFOLLOW_PATH}")  # create directory
        stop_spinner = True
        time.sleep(1.5)  # give a second for the for loop to catch up and stop the spinner
        user = get_input_username()
        stop_spinner = False
        # todo: verify the user exists
        with open(f"{UNFOLLOW_PATH}/user.txt", "w") as user_file:
            user_file.write(user)
        get_followers(user, write_file=True, overwrite=True)
        return ("first", user)


def write_followers(payload):
    if os.path.exists(f"{UNFOLLOW_PATH}/followers.json"):
        pass
    else:
        pass
    with open(f"{UNFOLLOW_PATH}/followers.json", "a") as follower_file:
        follower_file.write(f"{payload}\n")


def get_followers(username, write_file=False, overwrite=False):
    """writes to file"""
    if overwrite:
        # empty the followers file before filling it
        open(f'{UNFOLLOW_PATH}/followers.json', 'w').close()

    total_followers = []
    page = 1
    while True:
        raw_data = requests.get(f"https://api.github.com/users/{username}/followers?page={page}&per_page=100", headers=HEADERS)
        if raw_data.json() == []:
            # empty data, breaking now
           break
        if write_file is True:
            # write to file
            for user_object in raw_data.json():
                write_followers(user_object["login"])
        total_followers.append(raw_data.json())
        page += 1


def get_follow_num(username):
    # get number of followers and return
    raw_data = requests.get(f"https://api.github.com/users/{username}", headers=HEADERS)
    j_data = raw_data.json()
    try:
        follower_number = j_data["followers"]
    except KeyError:
        return "Failed to get number of followers"
    return follower_number


def check_deleted(username):
    """ checks if page doesn't exit
        returns true if deleted
        true otherwise"""
    response_code = requests.get(f"https://api.github.com/users/{username}", headers=HEADERS).status_code
    if response_code == 404:
        return True
    else:
        return False


def get_unfollows(username):
    """compare json"""
    unfollowers = []
    current_followers = []
    previous_followers = []  # read from the file before being changed
    # load the current content of the file
    with open(f"{UNFOLLOW_PATH}/followers.json") as follower_file:
        previous_followers.extend(iter(follower_file))

    # clear the file
    open(f'{UNFOLLOW_PATH}/followers.json', 'w').close()

    # get the new followers and put in file
    get_followers(username, write_file=True)

    # get newly added 'current' followers and load to file
    with open(f"{UNFOLLOW_PATH}/followers.json") as follower_file:
        current_followers.extend(iter(follower_file))

    # compare
    for old_follower in previous_followers:
        result = scan_follows(old_follower, current_followers)
        result_for_link = result
        if result is not True:
            if check_deleted(result):
                result = f"{result} \[deleted]"
            unfollowers.append((result, f"https://github.com/{result_for_link}/"))
    return unfollowers


def scan_follows(old_follower, current_followers):
    """
    takes a single old follower and
    compares to current followers
    if found: return True
    if not found: return name of follower
    """
    for current_follower in current_followers:
        if old_follower == current_follower:
            old_follower = old_follower.replace("\n", "")
            # user found
            return True
    old_follower = old_follower.replace("\n", "")
    return old_follower


def run_unfollow():
    global threads_stopped
    action, username = get_user()  # since item list
    follow_num = get_follow_num(username)
    if action == "first":  # user running for first time so no need to compare followers
        threads_stopped = True
        return ("first", follow_num)  # returns the number of followers
    else:
        threads_stopped = True
        unfollows = get_unfollows(username)
        if unfollows:  # if the list came back with content
            return ("regular", follow_num, unfollows)
        else:  # no unfollows
            return ("regular", follow_num)


def run_spinner():
    global stop_spinner
    print("")  # print a new line for spacing
    spinner = Status("Getting followers")
    spinner.start()
    while True:
        if stop_spinner:
            spinner.stop()
        elif stop_spinner is False:  # false, not none
            spinner.start()
        if threads_stopped:
            time.sleep(1)  # add a bit of time for aesthetics
            spinner.stop()
            return


def main():
    """
    returns either a two item tuple or
    three item tuple
    item 1: "regular" or "first"
    item 2: number of followers on account
    [item 3: unfollows]
        format: [("username", "link"),]
    """

    global threads_stopped  # used to stop run_spinner()
    unfollowed_future = executor.submit(run_unfollow)
    spin_future = executor.submit(run_spinner)
    # shutdown the thread pool
    executor.shutdown()     # blocks
    return unfollowed_future.result()

Files run in order:

1. `unfollow` imports `src.unfollow.cli` and runs the `main` function
2. `cli.py` - `main()`
    1.  `main()` runs and dispays start screen through function `start()`
    2. `check_connectivity()` - makes a request to google.com to ensure the user is connected to the internet
    3. Runs `get_links()` which imports the main function from `unfollow.py` and runs it to get the github unfollowers
    4. `get_links` then runs `print_get()` which displays a *Fetched Github followers* line
    5. based on the result of `check_connectivity` (which is assigned to a global variable `info`), actions are taken
       1. If `info` is equal to 'first' that means the user is using the program for the first time because there is no `user.txt` file in the program folder. Run the `end()` function with the number of followers the user has.
       2. Otherwise, the payload of `info` is examined. If unfollowers found, run `beautify_unfollows` from `beautify.py` (which displays a table of the unfollowers)
       3. Otherwise, run `no_unfollows()` which displays a message and then run `end()`

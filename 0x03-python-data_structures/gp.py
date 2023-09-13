#!/usr/bin/env python3

import os
import readline
import signal
import shlex
import re
import sys

# Define the signal handler
def signal_handler(signal, frame):
    print("\nOperation canceled by user.")
    exit(0)

# Set the signal handler for SIGINT
signal.signal(signal.SIGINT, signal_handler)

# Enable tab autocompletion for file names
readline.parse_and_bind("set show-all-if-ambiguous on")

def push_to_github(files=None, commit_message=None):
    try:
        while True:
            if files is None:
                # Running in interactive mode
                # Ask for the files to push
                while True:
                    files = input("Enter the file(s) to push (separated by spaces): ").strip()
                    if files:
                        break
                    else:
                        print("Error: No file(s) entered. Please try again.")

            # Check if the input is equal to "."
            if files == ".":
                # Run the "git add ." command directly
                exit_code = os.system("git add .")
                if exit_code != 0:
                    print("Error: Failed to add files to the index.")
                else:
                    break

            else:
                # Split the files into a list using a regular expression
                files_list = re.findall(r'\".+?\"|\'.+?\'|[^\'\"\s]+', files)

                # Check if the files exist
                if not all(os.path.isfile(file) for file in files_list):
                    print("Error: One or more files do not exist. Please try again.")
                    files = None
                else:
                    # Add the files to the index
                    exit_code = os.system("git add " + " ".join(files_list))
                    if exit_code != 0:
                        print("Error: Failed to add files to the index.")
                    else:
                        break

        # Ask for the commit message if not entered
        if commit_message is None:
            while True:
                commit_message = input("Enter the commit message: ").strip()
                if commit_message:
                    break
                else:
                    print("Error: No commit message entered.")

        # Make the commit
        os.system(f"git commit -m {shlex.quote(commit_message)}")

        # Push to GitHub
        os.system("git push")

    except EOFError:
        signal_handler(signal.SIGINT, None)

if __name__ == "__main__":
    # Check if command-line arguments are provided
    if len(sys.argv) > 1:
        files = sys.argv[1]
        commit_message = sys.argv[2] if len(sys.argv) > 2 else None
        push_to_github(files, commit_message)
    else:
        push_to_github()


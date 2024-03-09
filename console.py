#!/usr/bin/python3

import cmd
import shlex

"""
Create a note
Delete a note
Update the note

Note:
    - Title
    - Description
    - UserId for now which is empty string
    - Priority
    (Create, update time, id)

User:
    - This user have created this note
    - username
    - (created, updated, id)
"""

class HelloWorld(cmd.Cmd):

    """Simple Command Processor example."""

    prompt = "Enter Command: "
    intro = "A CLI for our App"

    def do_greet(self, line):
        """This is a function that says hi"""
        names = shlex.split(line)
        for name in names:
            print("hello", name)

    def do_sum(self, nums):
        total = sum(map(int, shlex.split(nums)))
        print(f"the sum is {total}")

    def do_EOF(self, line):
        return True
    


if __name__ == '__main__':
    import sys

    if len(sys.argv) > 1:
        # non interactive mode
        HelloWorld().onecmd(' '.join(sys.argv[1:]))
    else:
        HelloWorld().cmdloop()
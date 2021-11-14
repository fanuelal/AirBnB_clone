#!/usr/bin/python3

import cmd

class HBNBCommand(cmd.Cmd):
    """
    making the console
    """
    prompt = '(hbnb)'

    def do_quit(self, arg):
        """ exiting the program"""
        return True

    def do_EOF(self, arg):
        """ quit """
        return True









if __name__ == '__main__':
    HBNBCommand().cmdloop()

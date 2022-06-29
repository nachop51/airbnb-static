#!/usr/bin/python3
""" Console module """
import cmd


class HBNBCommand(cmd.Cmd):
    """ Class for HBNB console """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Ends the program"""
        return True

    def emptyline(self):
        """execute nothing"""
        pass

    def do_help(self, line):
        """show helpfull messages"""
        super().do_help(line)

if __name__ == '__main__':
    HBNBCommand().cmdloop()

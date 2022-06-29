#!/usr/bin/python3
""" Console module """
import cmd
from models import storage


class HBNBCommand(cmd.Cmd):
    """ Class for HBNB console """
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        return True

    def do_EOF(self, arg):
        """Ends the program
        """
        return True

    def emptyline(self):
        """In case of an empty line
        """
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id
        """
        if arg is None or arg == "":
            print("** class name missing **")
        elif arg not in storage.classes():
            print("** class doesn't exist **")
        else:
            obj = storage.classes()[arg]()
            print(obj.id)
            obj.save()

    def do_show(self, arg):
        """Prints the string representation of an
        instance based on the class name and id
        """
        if arg is None or arg == "":
            print("** class name missing **")
        else:
            arg = arg.split()
            if arg[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(arg) == 1 or arg[1] is None or arg[1] == "":
                print("** instance id missing **")
            else:
                key = arg[0] + "." + arg[1]
                if key in storage.all():
                    print(storage.all()[key])
                else:
                    print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id
        """
        if arg is None or arg == "":
            print("** class name missing **")
        else:
            arg = arg.split()
            if arg[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(arg) == 1 or arg[1] is None or arg[1] == "":
                print("** instance id missing **")
            else:
                key = arg[0] + "." + arg[1]
                if key in storage.all():
                    del storage.all()[key]
                    storage.save()
                else:
                    print("** no instance found **")

    def do_all(self, arg):
        """Prints all string representation of all
        instances based or not on the class name
        """
        if storage.all() is None or storage.all() == {}:
            print("[]")
        else:
            print(storage.all())

    def do_update(self, arg):
        """Updates an instance based on the class
        name and id by adding or updating attribute
        """

        """execute nothing"""
        pass

    def do_help(self, line):
        """Show helpfull messages"""
        super().do_help(line)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

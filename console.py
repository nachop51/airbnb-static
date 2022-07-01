#!/usr/bin/python3
""" Console module """
import cmd
from models import storage
import shlex


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
            arg = shlex.split(arg)
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
            arg = shlex.split(arg)
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
            arg = shlex.split(arg)
            values = [str(obj) for obj in storage.all().values()]
            if len(arg) == 0 or arg is None or arg == "":
                print(values)
            elif arg[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                values = [str(obj) for obj in storage.all().values()
                          if obj.__class__.__name__ == arg[0]]
                print(values)

    def do_help(self, line):
        """Show helpfull messages"""
        super().do_help(line)

    def do_update(self, arg):
        """Updates an instance based on the class
        name and id by adding or updating attribute
        """
        if arg is None or arg == "":
            print("** class name missing **")
        else:
            arg = shlex.split(arg)
            if arg[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(arg) == 1 or arg[1] is None or arg[1] == "":
                print("** instance id missing **")
            elif len(arg) == 2 or arg[2] is None or arg[2] == "":
                print("** attribute name missing **")
            elif len(arg) == 3 or arg[3] is None or arg[3] == "":
                print("** value missing **")
            else:
                key = arg[0] + "." + arg[1]
                for a in arg:
                    if a == a.strip('"'):
                        arg[arg.index(a)] = a.strip('"')
                if key in storage.all():
                    setattr(storage.all()[key], arg[2], arg[3])
                    storage.save()
                else:
                    print("** no instance found **")

    def precmd(self, arg):
        classname = arg.split('.')[0]
        if classname in storage.classes() and '(' in arg and ')' == arg[-1]:
            command = arg.split('.')[1].split('(')[0]
            commands = ['all', 'count', 'show', 'destroy', 'update']
            if command in commands:
                if command == 'count':
                    values = [str(obj) for obj in storage.all().values()
                              if obj.__class__.__name__ == classname]
                    print(len(values))
                    return ""
                elif command == 'show' or command == 'destroy':
                    id = arg.split('.')[1].split('(')[1][1:-2]
                    return f"{command} {classname} {id}"
                elif command == 'update':
                    args = arg.split('.')[1].split('(')[1][:-1]
                    id = args.split(',')[0].strip()[1:-1]
                    attr = "".join(args.split('{')[1:]).strip()
                    attr = '{' + attr
                    print(attr)
                    if '{' in attr and '}' in attr:
                        attribute = attr.split(':')[0][2:-1]
                        value = attr.split(':')[1].split(',')[0][2:-1]
                        # print(f"{classname} {id} {attribute} {value}")
                        self.do_update(
                            f"{classname} {id} {attribute} {value}")
                        return ""
                    else:
                        attr = args.split(',')[1].strip()[1:-1]
                        value = args.split(',')[2].strip()[1:-1]
                        return f"{command} {classname} {id} {attr[1:-1]} {value}"
                    # print(f"{command} {classname} {id} {attr} {value}")
                return f"{command} {classname}"
        return arg


if __name__ == '__main__':
    HBNBCommand().cmdloop()

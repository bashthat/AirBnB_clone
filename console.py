#!/usr/bin/env python3
""" 
Console for the hbnb
"""
import cmd
import re
import shlex

from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    handling the HBNB application
    """

    prompt = '(hbnb) '
    __classes = {'BaseModel': BaseModel, 'User': User,
                 'State': State, 'City': City, 'Amenity': Amenity,
                 'Place': Place, 'Review': Review}
    

    def do_create(self, *args):
        """
        instance to create
        """
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(args[0] + "." + str(eval(args[0] + "()")))

    def do_update(self, *args):
        """
        Updates an instance
        """
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print('** instance id missing **')
        elif len(args) < 3:
            print('** attribute name missing **')
        elif len(args) < 4:
            print('** value missing **')

        else:
            key = args[0] + '.' + args[1]
            if key in storage.all().keys():
                if args[2] in ['created_at', 'updated_at']:
                    print("** attribute name cannot be 'created_at' or "
                          "'updated_at' **")
                else:
                    storage.all()[key].__dict__[args[2]] = args[3]
                    storage.all()[key].save()
            else:
                print("** no instance found **")

    def do_all(self, *args):
        """ Prints all instances """
        if args[0] == ' ':
            print(storage.all())
        elif args and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print([str(v) for k, v in storage.all().items()
                   if args[0] in k])

    def do_count(self, args):
        """
        counts the instances
        """
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(len([v for k, v in storage.all().items()
                       if args[0] in k]))

    def do_show(self, args):
        """Prints the instance"""
        args = args.split(' ')
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print('** instance id missing **')
        else:
            key = args[0] + '.' + args[1]
            if key in storage.all().keys():
                print(storage.all()[key])
            else:
                print("** no instance found **")

    def do_destroy(self, *args):
        """destroy the instance! """
        args = args.split(' ')
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print('** instance id missing **')
        else:
            key = args[0] + '.' + args[1]
            if key in storage.all().keys():
                del storage.all()[key]
                storage.save()
            else:
                print("** no instance found **")

    def default(self, line):
        """
        consoles default.
        """
        print("*** Unknown syntax: {}".format(line))

    def do_quit(self, args):
        """ Quits the application"""
        return True

    def do_exit(self, args):
        """ Quits the application"""
        return True

    def do_EOF(self, args):
        """ Quits the application with an end of file"""
        return True

    def emptyline(self):
        """ empty line"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()

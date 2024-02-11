#!/usr/bin/python3

import cmd
import shlex
from models.base_model import BaseModel
from models.user import User
from models import storage


class HBNBCommand(cmd.Cmd):
    """
    A command-line interpreter for managing objects in a file storage system.
    """

    prompt = "(hbnb) "

    allowed_classes = ["BaseModel", "User"]

    def emptyline(self):
        """Override emptyline method to do nothing."""
        pass

    def do_quit(self, arg):
        """Quit command to exit the program."""
        return True

    def help_quit(self):
        """Display help message for quit command."""
        print("Quit command to exit the program")

    def do_create(self, arg):
        """
        Create a new instance of a specified class.

        Args:
            arg (str): Class name.

        """
        line = shlex.split(arg)

        if len(line) == 0:
            print("** class name missing **")
        elif line[0] not in self.allowed_classes:
            print("** class doesn't exist **")
        else:
            new_instance = eval(f"{line[0]}()")
            storage.save()
            print(new_instance.id)

    def do_show(self, arg):
        """
        Display the string representation of an instance.

        Args:
            arg (str): Class name and instance ID.

        """
        line = shlex.split(arg)
        if len(line) == 0:
            print("** class name missing **")
        elif line[0] not in self.allowed_classes:
            print("** class doesn't missing **")
        elif len(line) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(line[0], line[1])
            if key in objects:
                print(objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, arg):
        """
        Delete an instance based on the class name and ID.

        Args:
            arg (str): Class name and instance ID.

        """
        line = shlex.split(arg)
        if len(line) == 0:
            print("** class name missing **")
        elif line[0] not in self.allowed_classes:
            print("** class doesn't exist **")
        elif len(line) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(line[0], line[1])
            if key in objects:
                del objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Display all instances of a specified class.

        Args:
            arg (str): Optional class name.

        """
        objects = storage.all()
        line = shlex.split(arg)
        if len(line) == 0:
            for key, value in objects.items():
                print(str(value))
        elif line[0] not in self.allowed_classes:
            print("** class doesn't exist **")
        else:
            for key, value in objects.items():
                if key.split('.')[0] == line[0]:
                    print(str(value))

    def do_update(self, arg):
        """
        Update an instance attribute.

        Args:
            arg (str): Class name, instance ID, attribute name, and attribute value.

        """
        line = shlex.split(arg)
        if len(line) == 0:
            print("** class name missing **")
        elif line[0] not in self.allowed_classes:
            print("** class doesn't exist **")
        elif len(line) < 2:
            print("** instance id missing **")
        else:
            objects = storage.all()
            key = "{}.{}".format(line[0], line[1])
            if key not in objects:
                print("** no instance found **")
            elif len(line) < 3:
                print("** attribute name missing **")
            elif len(line) < 4:
                print("** value missing **")
            else:
                obj = objects[key]
                attribute_name = line[2]
                attribute_value = line[3]
                try:
                    attribute_value = eval(attribute_value)
                except Exception:
                    pass
                setattr(obj, attribute_name, attribute_value)
                obj.save()

    def do_EOF(self, arg):
        """Handle EOF (Ctrl+D) to exit the program."""
        print()
        return True


if __name__ == "__main__":
    HBNBCommand().cmdloop()

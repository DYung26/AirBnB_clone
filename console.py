#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    all_classes = {
        'BaseModel': BaseModel
    }

    def do_create(self, arg):
        """Creates a new model instance of the class passed as arg

            Usage: create <ModelName>
        """
        if not arg:
            print('** class name missing **')
            return
        try:
            new_instance = HBNBCommand.all_classes[arg]()
            print(new_instance.id)
        except KeyError:
            print("** class doesn't exist **")

    def do_EOF(self, line):
        """Handle End-of-File (EOF) input"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """An empty line + `ENTER` shouldn’t execute anything"""

    def do_show(self, line):
        """Show instance based on class name and id

            Usage: show <ClassName> <InstanceID>
        """
        args = line.split()
        if not args or not args[0]:
            print('** class name missing **')
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        class_name = args[0]
        if class_name not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        id = args[1]
        key = f"{class_name}.{id}"

        # file_storage_instance = FileStorage()

        if key not in storage.all():
            print('** no instance found **')
        else:
            print(storage.all()[key])


if __name__ == '__main__':
    HBNBCommand().cmdloop()

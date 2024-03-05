#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    all_classes = {
        'BaseModel': BaseModel
    }

    def do_create(self, line):
        """Creates a new model instance of the class passed as arg

            Usage: create <ModelName>
        """
        if not line:
            print('** class name missing **')
            return
        try:
            new_instance = HBNBCommand.all_classes[line]()
            print(new_instance.id)
        except KeyError:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """do_destroy deletes a model instance

            Usage: destroy <ModelName> <ModelId>
        Args:
            line (str): model name and model id
        """
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        model_name = args[0]
        if model_name not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        model_id = args[1]
        key = model_name + "." + model_id
        all_objs = storage.all()
        if key not in all_objs:
            print("** no instance found **")
            return
        del all_objs[key]

    def do_EOF(self, line):
        """Handle End-of-File (EOF) input"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def emptyline(self):
        """An empty line + `ENTER` shouldn’t execute anything"""


if __name__ == '__main__':
    HBNBCommand().cmdloop()

#!/usr/bin/python3
import cmd
from models.base_model import BaseModel


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


if __name__ == '__main__':
    HBNBCommand().cmdloop()

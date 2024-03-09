#!/usr/bin/python3
"""
Module: console.py
This module defines the HBNBCommand class,
a command-line interpreter for managing AirBnB objects.
"""
import cmd
import json
import re
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


def parse_attr_value(attr_value):
    """parse_attr_value Parses JSON like data to appropriate type

    Args:
        attr_value (str): data to be parsed

    Returns:
        (str, int, float, bool): _description_
    """
    try:
        return json.loads(attr_value)
    except json.JSONDecodeError:
        if attr_value.lower() in ['true', 'false']:
            return attr_value.lower() == 'true'
        try:
            return int(attr_value)
        except ValueError:
            try:
                return float(attr_value)
            except ValueError:
                return attr_value


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class: Command-line interpreter for managing AirBnB objects.

    Attributes:
        prompt (str): The command prompt displayed to the user.
        all_classes (dict):
            A dictionary mapping class names to their corresponding classes.

    Methods:
        do_create(self, line):
            Creates a new model instance of the class passed as an argument.
        do_destroy(self, line):
            Deletes a model instance based on class name and ID.
        do_EOF(self, line): Handles End-of-File (EOF) input.
        do_quit(self, line):
            Quits the command interpreter and exits the program.
        emptyline(self): Handles an empty line input.
        do_show(self, line):
            Displays the string representation of an instance
            based on class name and ID.
        do_all(self, line):
            Prints all string representations of instances based on class name.

    Usage:
        Execute this script to launch the AirBnB command-line interpreter.
    """
    prompt = "(hbnb) "
    all_classes = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    def do_create(self, line):
        """Creates a new model instance of the class passed as arg

            Usage:
                `create <ModelName>`
        """
        args = line.split()
        if not args or not args[0]:
            print("** class name missing **")
            return
        try:
            new_instance = HBNBCommand.all_classes[args[0]]()
            new_instance.save()
            print(new_instance.id)
        except KeyError:
            print("** class doesn't exist **")

    def do_destroy(self, line):
        """do_destroy deletes a model instance based on class name and ID.

        Usage: `destroy <ModelName> <ModelId>`
        Args:
            line (str): model name and model ID.
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
        storage.save()

    def do_update(self, line):
        """update updates a model instance

            Usage: update <ModelName> <ModelId> <attribute_name>
            <attribute_value>
        Args:
            line (str): model name, model id, attribute name, attribute value
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
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        model_obj = all_objs[key]
        attr_name = args[2]
        attr_value = args[3]
        if attr_name in ['id', 'created_at', 'updated_at']:
            return
        try:
            attr_value = parse_attr_value(attr_value)
            setattr(model_obj, attr_name, attr_value)
            model_obj.save()
        except json.JSONDecodeError:
            return
        return

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

        class_name = args[0]
        if class_name not in HBNBCommand.all_classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        _id = args[1]
        key = class_name + "." + _id

        if key not in storage.all():
            print('** no instance found **')
        else:
            print(storage.all()[key])

    def do_all(self, line):
        """Prints all string rep. of instances based on class name.

        Usage:
            `all <ClassName>` or `all`
        """
        args = line.split()

        if args:
            class_name = args[0]
            if class_name not in HBNBCommand.all_classes:
                print("** class doesn't exist **")
                return

            instances = [
                str(obj) for obj in storage.all().values()
                if obj.__class__.__name__ == class_name]
            print(instances)
        else:
            instances = [str(obj) for obj in storage.all().values()]
            print(instances)

    def parseline(self, line):
        """parseline overiding parent method to allow more dynamic inputs

        Args:
            line (string): stdin input

        Returns:
            (tuple): (command, args, line)
        """
        self.current_line = line
        pattern = r"(\b\w+)\.(\w+)\(([^()]*)\)"
        matches = re.findall(pattern, line)
        if matches and len(matches[0]) == 3:
            method_name = matches[0][1]
            model_name = matches[0][0]
            arguments = ""
            pattern = r"{[^{}]*}"
            match = re.search(pattern, line)
            if match:
                pre = re.split(r",\s*", matches[0][2])
                try:
                    a = json.loads(match.group().replace("'", '"'))
                    arr = []
                    for k, v in a.items():
                        arr.append(k)
                        arr.append(str(v).strip())
                    arguments = pre[0].replace('"', "") + " " + " ".join(arr)
                    method_name = "dict_" + method_name
                except json.decoder.JSONDecodeError:
                    return cmd.Cmd.parseline(self, line)
            else:
                pre = re.split(r",\s*", matches[0][2])
                for item in pre:
                    if bool(re.match(r'^("[^"]*"|\'[^\']*\')$', item)):
                        arguments += " " + item.replace("'", "").replace(
                            '"', "")
                    else:
                        cmd.Cmd.parseline(self, line)
            combined = (
                method_name.strip()
                + " " +
                model_name.strip()
                + " " +
                arguments.strip()
            )
            return (None, None, combined)
        ret = cmd.Cmd.parseline(self, line)
        return ret

    def default(self, line):
        """default overiding parent default method

        Args:
            line (str): Input from parseline

        Returns: None
        """
        args = line.split(' ')
        if len(args) < 3:
            return cmd.Cmd.default(self, self.current_line)
        model_method = args[0]
        final_args = args[1:]
        try:
            _cls = getattr(self, 'do_' + model_method)
            _cls(" ".join(final_args))
        except AttributeError:
            return cmd.Cmd.default(self, self.current_line)
        return None

    def do_dict_update(self, line):
        """do_dict_update handles arguments passed as a dictionary

        Args:
            line (str): parsed input

        Returns:
            bool: True if successful and False if not
        """
        args = line.split()
        if len(args) <= 4:
            self.do_update(line)
            return
        model_name = args[0]
        model_id = args[1]
        rest = args[2:]
        while len(rest) > 0:
            my_line = model_name + " " + model_id + " " + " ".join(rest)
            self.do_update(my_line)
            rest = rest[2:]
        return

    def do_count(self, line):
        """Counts all instances of class class name.

        Usage:
            `<ModelName>all()
        """
        args = line.split()

        if args:
            class_name = args[0]
            if class_name not in HBNBCommand.all_classes:
                print("** class doesn't exist **")
                return

            instances = [
                str(obj) for obj in storage.all().values()
                if obj.__class__.__name__ == class_name]
            print(len(instances))


if __name__ == '__main__':
    HBNBCommand().cmdloop()

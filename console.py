#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    all_classes = {
        "BaseModel": BaseModel,
        "User": User
    }

    def do_create(self, line):
        """Creates a new model instance of the class passed as arg

            Usage: create <ModelName>
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
        model_name = args[0]
        model_id = args[1]
        attr_name = args[2]
        attr_value = args[3]
        if attr_name in ['id', 'created_at', 'updated_at']:
            return
        key = model_name + "." + model_id
        model_obj = all_objs[key]
        try:
            setattr(model_obj, attr_name, json.loads(
                '"' + attr_value + '"'))
            model_obj.save()
        except json.JSONDecodeError:
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
                if isinstance(obj, HBNBCommand.all_classes[class_name])]
            print(instances)
        else:
            instances = [str(obj) for obj in storage.all().values()]
            print(instances)


if __name__ == '__main__':
    HBNBCommand().cmdloop()

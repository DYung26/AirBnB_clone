import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = HBNBCommand()
        self.held_output = StringIO()

    def tearDown(self):
        self.held_output.close()

    def test_create_command(self):
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("create BaseModel")
        output = self.held_output.getvalue().strip()
        self.assertTrue(storage.all()["BaseModel." + output])

    def test_create_command_nonexistent_class(self):
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("create NonExistentClass")
        output = self.held_output.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_destroy_command(self):
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("create BaseModel")
        obj_id = self.held_output.getvalue().strip()
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd(f"destroy BaseModel {obj_id}")
        output = self.held_output.getvalue().strip()
        self.assertFalse(storage.all().get("BaseModel." + obj_id))
        self.assertEqual(output, "")

    def test_destroy_command_nonexistent_class(self):
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("destroy NonExistentClass 123")
        output = self.held_output.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_destroy_command_missing_id(self):
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("destroy BaseModel")
        output = self.held_output.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")

    def test_show_command(self):
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("create BaseModel")
        obj_id = self.held_output.getvalue().strip()
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd(f"show BaseModel {obj_id}")
        output = self.held_output.getvalue().strip()
        self.assertIn(f"BaseModel.{obj_id}", output)

    def test_show_command_nonexistent_class(self):
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("show NonExistentClass 123")
        output = self.held_output.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_show_command_missing_id(self):
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("show BaseModel")
        output = self.held_output.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")

    def test_all_command(self):
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("create BaseModel")
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("all BaseModel")
        output = self.held_output.getvalue().strip()
        self.assertIn("BaseModel", output)

    def test_all_command_nonexistent_class(self):
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("all NonExistentClass")
        output = self.held_output.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_count_command(self):
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("create BaseModel")
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("count BaseModel")
        output = self.held_output.getvalue().strip()
        self.assertEqual(output, "1")

    def test_count_command_nonexistent_class(self):
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("count NonExistentClass")
        output = self.held_output.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_update_command(self):
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("create BaseModel")
        obj_id = self.held_output.getvalue().strip()
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd(f"update BaseModel {obj_id} name 'NewName'")
        output = self.held_output.getvalue().strip()
        self.assertEqual(output, "")

    def test_update_command_nonexistent_class(self):
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("update NonExistentClass 123 name 'NewName'")
        output = self.held_output.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_update_command_missing_id(self):
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("update BaseModel name 'NewName'")
        output = self.held_output.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")

    def test_update_command_nonexistent_instance(self):
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("update BaseModel 123 name 'NewName'")
        output = self.held_output.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    def test_update_command_missing_attribute(self):
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("create BaseModel")
        obj_id = self.held_output.getvalue().strip()
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd(f"update BaseModel {obj_id}")
        output = self.held_output.getvalue().strip()
        self.assertEqual(output, "** attribute name missing **")

    def test_update_command_missing_value(self):
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("create BaseModel")
        obj_id = self.held_output.getvalue().strip()
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd(f"update BaseModel {obj_id} name")
        output = self.held_output.getvalue().strip()
        self.assertEqual(output, "** value missing **")


if __name__ == '__main__':
    unittest.main()

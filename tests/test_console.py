import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand
from models import storage


class TestConsole(unittest.TestCase):
    """
    TestConsole class to test the functionality of the HBNBCommand class.
    """

    def setUp(self):
        """
        Set up method to initialize the test environment.
        """
        self.console = HBNBCommand()
        self.held_output = StringIO()

    def tearDown(self):
        """
        Tear down method to clean up after each test.
        """
        self.held_output.close()

    def test_create_command(self):
        """
        Test create command to ensure it creates a new instance.
        """
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("create BaseModel")
        output = self.held_output.getvalue().strip()
        self.assertTrue(storage.all()["BaseModel." + output])

    def test_create_command_nonexistent_class(self):
        """
        Test create command with a nonexistent class.
        """
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("create NonExistentClass")
        output = self.held_output.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_destroy_command(self):
        """
        Test destroy command to ensure it deletes an instance.
        """
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("create BaseModel")
        obj_id = self.held_output.getvalue().strip()
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd(f"destroy BaseModel {obj_id}")
        output = self.held_output.getvalue().strip()
        self.assertFalse(storage.all().get("BaseModel." + obj_id))
        self.assertEqual(output, "")

    def test_destroy_command_nonexistent_class(self):
        """
        Test destroy command with a nonexistent class.
        """
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("destroy NonExistentClass 123")
        output = self.held_output.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_destroy_command_missing_id(self):
        """
        Test destroy command with missing instance ID.
        """
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("destroy BaseModel")
        output = self.held_output.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")

    def test_show_command(self):
        """
        Test show command to ensure it displays instance information.
        """
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("create BaseModel")
        obj_id = self.held_output.getvalue().strip()
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd(f"show BaseModel {obj_id}")
        output = self.held_output.getvalue().strip()
        self.assertIn(f"BaseModel.{obj_id}", output)

    def test_show_command_nonexistent_class(self):
        """
        Test show command with a nonexistent class.
        """
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("show NonExistentClass 123")
        output = self.held_output.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_show_command_missing_id(self):
        """
        Test show command with missing instance ID.
        """
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("show BaseModel")
        output = self.held_output.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")

    def test_all_command(self):
        """
        Test all command to ensure it prints all instances.
        """
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("create BaseModel")
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("all BaseModel")
        output = self.held_output.getvalue().strip()
        self.assertIn("BaseModel", output)

    def test_all_command_nonexistent_class(self):
        """
        Test all command with a nonexistent class.
        """
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("all NonExistentClass")
        output = self.held_output.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_count_command(self):
        """
        Test count command to ensure it counts instances.
        """
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("create BaseModel")
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("count BaseModel")
        output = self.held_output.getvalue().strip()
        self.assertEqual(output, "1")

    def test_count_command_nonexistent_class(self):
        """
        Test count command with a nonexistent class.
        """
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("count NonExistentClass")
        output = self.held_output.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_update_command(self):
        """
        Test update command to ensure it updates an instance.
        """
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("create BaseModel")
        obj_id = self.held_output.getvalue().strip()
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd(f"update BaseModel {obj_id} name 'NewName'")
        output = self.held_output.getvalue().strip()
        self.assertEqual(output, "")

    def test_update_command_nonexistent_class(self):
        """
        Test update command with a nonexistent class.
        """
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("update NonExistentClass 123 name 'NewName'")
        output = self.held_output.getvalue().strip()
        self.assertEqual(output, "** class doesn't exist **")

    def test_update_command_missing_id(self):
        """
        Test update command with missing instance ID.
        """
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("update BaseModel name 'NewName'")
        output = self.held_output.getvalue().strip()
        self.assertEqual(output, "** instance id missing **")

    def test_update_command_nonexistent_instance(self):
        """
        Test update command with a nonexistent instance.
        """
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("update BaseModel 123 name 'NewName'")
        output = self.held_output.getvalue().strip()
        self.assertEqual(output, "** no instance found **")

    def test_update_command_missing_attribute(self):
        """
        Test update command with missing attribute name.
        """
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("create BaseModel")
        obj_id = self.held_output.getvalue().strip()
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd(f"update BaseModel {obj_id}")
        output = self.held_output.getvalue().strip()
        self.assertEqual(output, "** attribute name missing **")

    def test_update_command_missing_value(self):
        """
        Test update command with missing attribute value.
        """
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("create BaseModel")
        obj_id = self.held_output.getvalue().strip()
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd(f"update BaseModel {obj_id} name")
        output = self.held_output.getvalue().strip()
        self.assertEqual(output, "** value missing **")

    def test_update_command_invalid_json(self):
        """
        Test update command with invalid JSON input.
        """
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd('create BaseModel')
        obj_id = self.held_output.getvalue().strip()
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd(f'update BaseModel {obj_id} name invalid_json')
        output = self.held_output.getvalue().strip()
        self.assertEqual(output, "** invalid JSON **")

    def test_update_command_valid_json(self):
        """
        Test update command with valid JSON input.
        """
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd('create BaseModel')
        obj_id = self.held_output.getvalue().strip()
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd(f'update BaseModel {obj_id} \
            \'name {"NewName"}')
        output = self.held_output.getvalue().strip()
        self.assertEqual(output, "")

    def test_dict_update_command_invalid_json(self):
        """
        Test dict_update command with invalid JSON input.
        """
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd('create BaseModel')
        obj_id = self.held_output.getvalue().strip()
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd(f'dict_update BaseModel {obj_id} \
            \'dict_attribute invalid_json')
        output = self.held_output.getvalue().strip()
        self.assertEqual(output, "** invalid JSON **")

    def test_dict_update_command_valid_json(self):
        """
        Test dict_update command with valid JSON input.
        """
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd('create BaseModel')
        obj_id = self.held_output.getvalue().strip()
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd(f'dict_update BaseModel {obj_id} \
            \'dict_attribute \'{"{"key": "value"}"}\'')
        output = self.held_output.getvalue().strip()
        updated_obj = storage.all()["BaseModel." + obj_id]
        self.assertEqual(updated_obj.dict_attribute, {"key": "value"})

    def test_count_command_valid_json(self):
        """
        Test count command with valid JSON input.
        """
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("create BaseModel")
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("count BaseModel")
        output = self.held_output.getvalue().strip()
        self.assertEqual(output, "1")

    def test_count_command_invalid_json(self):
        """
        Test count command with invalid JSON input.
        """
        with patch('sys.stdout', new=self.held_output):
            self.console.onecmd("count BaseModel invalid_json")
        output = self.held_output.getvalue().strip()
        self.assertEqual(output, "** invalid JSON **")


if __name__ == '__main__':
    unittest.main()

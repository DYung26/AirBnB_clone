import os
import unittest
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):
    """
    A class to test the FileStorage class methods.

    Methods:
    - setUp(self): Set up the test environment before each test case.
    - tearDown(self): Clean up the test environment after each test case.
    - test_filestorage_has_docstrings(self): Test if FileStorage class and its
        methods have docstrings.
    - test_filestorage_has_methods(self): Test if FileStorage class has the
        required methods.
    - test_filestorage_all_method(self): Test the 'all' method of the
        FileStorage class.
    - test_filestorage_new_method(self): Test the 'new' method of the
        FileStorage class.
    - test_filestorage_save_and_reload_method(self): Test the 'save' and
        'reload' methods of the FileStorage class.
    """

    def setUp(self):
        """
        Set up the test environment before each test case.
        """
        self.file_path = "file.json"
        self.storage = FileStorage()

    def tearDown(self):
        """
        Clean up the test environment after each test case.
        """
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_filestorage_has_docstrings(self):
        """
        Test if FileStorage class and its methods have docstrings.
        """
        self.assertIsNotNone(FileStorage.__doc__)
        self.assertGreaterEqual(len(FileStorage.__doc__), 10)
        self.assertIsNotNone(FileStorage.all.__doc__)
        self.assertGreaterEqual(len(FileStorage.__doc__), 10)
        self.assertIsNotNone(FileStorage.new.__doc__)
        self.assertGreaterEqual(len(FileStorage.__doc__), 10)
        self.assertIsNotNone(FileStorage.save.__doc__)
        self.assertGreaterEqual(len(FileStorage.__doc__), 10)
        self.assertIsNotNone(FileStorage.reload.__doc__)
        self.assertGreaterEqual(len(FileStorage.__doc__), 10)

    def test_filestorage_has_methods(self):
        """
        Test if FileStorage class has the required methods.
        """
        self.assertTrue(hasattr(FileStorage, "all"))
        self.assertTrue(hasattr(FileStorage, "new"))
        self.assertTrue(hasattr(FileStorage, "save"))
        self.assertTrue(hasattr(FileStorage, "reload"))

    def test_filestorage_all_method(self):
        """
        Test the 'all' method of the FileStorage class.
        """
        fs_objs = self.storage.all()
        self.assertIsNotNone(fs_objs)
        self.assertEqual(type(fs_objs), dict)

    def test_filestorage_new_method(self):
        """
        Test the 'new' method of the FileStorage class.
        """
        from models.base_model import BaseModel  # noqa  # pylint: disable=unused-import disable=import-outside-toplevel
        new_obj = BaseModel()
        self.storage.new(new_obj)
        key = new_obj.__class__.__name__ + "." + str(new_obj.id)
        self.assertIn(key, self.storage.all().keys())
        from_storage = self.storage.all()[key]
        self.assertIsInstance(from_storage, BaseModel)

    def test_filestorage_save_and_reload_method(self):
        """
        Test the 'save' and 'reload' methods of the FileStorage class.
        """
        from models.base_model import BaseModel  # noqa  # pylint: disable=unused-import disable=import-outside-toplevel
        obj1 = BaseModel()
        obj2 = BaseModel()
        key1 = obj1.__class__.__name__ + "." + str(obj1.id)
        key2 = obj2.__class__.__name__ + "." + str(obj2.id)
        self.storage.new(obj1)
        self.storage.new(obj2)
        new_storage = FileStorage()
        new_storage.reload()
        objects = new_storage.all()
        self.assertIn(key1, objects.keys())
        self.assertIn(key2, objects.keys())


if __name__ == "__main__":
    unittest.main()

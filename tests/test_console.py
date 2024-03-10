#!/usr/bin/python3
""" _summary_
"""
import unittest
import console


class TestConsole(unittest.TestCase):
    def setUp(self):
        self.console = console.HBNBCommand()

    def test_attributes_default_values(self):
        pass


if __name__ == '__main__':
    unittest.main()

#!/usr/bin/python3
"""Unit tests for console.py"""

import unittest
import pycodestyle
from console import HBNBCommand
from models.base_model import BaseModel
from models.amenity import Amenity
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.engine.file_storage import FileStorage
from unittest.mock import patch
from io import StringIO
import os
from os.path import exists


class ConsoleTest(unittest.TestCase):
    """Test for console.py"""

    def set_up(self):
        """Sets up test cases."""
        if exists("file.json"):
            os.remove("file.json")
        self.reset()

    def reset(self):
        """Resets FileStorage data."""
        FileStorage._FileStorage__objects = {}
        if exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_pep8(self):
        """Check PEP8 style"""
        syntaxis = pycodestyle.StyleGuide(quit=True)
        check = syntaxis.check_files(['console.py'])
        self.assertEqual(
            check.total_errors, 0, "Found style errors"
        )

    def test_do_quit(self):
        """Test do_quit method"""
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("quit")
            self.assertEqual(input_t.getvalue(), "")

    def test_EOF(self):
        """Test do_EOF method"""
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("EOF")
            self.assertEqual(input_t.getvalue(), "")

    def test_emptyline(self):
        """test emptyline method"""
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("\n")
            self.assertEqual(input_t.getvalue(), "")

    def test_help(self):
        """Test self method"""
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("help help")
            self.assertEqual(input_t.getvalue(), "Show helpfull messages\n")
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("help EOF")
            self.assertEqual(input_t.getvalue(), "Ends the program\n")
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("help quit")
            self.assertEqual(input_t.getvalue(),
                             "Quit command to exit the program\n")
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("help destroy")
            self.assertEqual(
                input_t.getvalue(),
                "Deletes an instance based on the class name and id\n"
            )
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("help create")
            self.assertEqual(
                input_t.getvalue(),
                "Creates a new instance of BaseModel, saves it, and prints the id\n"
            )

    def test_do_create(self):
        """test do_create method"""
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("create")
            self.assertEqual(input_t.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("create Amenityzcv")
            self.assertEqual(input_t.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("create User")
            id = input_t.getvalue()[:-1]
            self.assertFalse(id == "")
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("all User")
            self.assertTrue(id in input_t.getvalue())
            key = f"User.{id}"
            self.assertIsNotNone(
                FileStorage._FileStorage__objects[key]
            )

    def test_do_show(self):
        """test do_show method"""
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("show")
            self.assertEqual(input_t.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("show Usertre")
            self.assertEqual(input_t.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("show User")
            self.assertEqual(input_t.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("show User 9")
            self.assertEqual(input_t.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("create User")
            id = input_t.getvalue()[:-1]
            self.assertFalse(id == "")
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd(f"show User {id}")
            key = f"User.{id}"
            self.assertEqual(
                str(FileStorage._FileStorage__objects[key]),
                input_t.getvalue()[:-1]
            )

    def test_do_destroy(self):
        """test do_destroy"""
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("destroy")
            self.assertEqual(input_t.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("destroy Everything")
            self.assertEqual(input_t.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("destroy User")
            self.assertEqual(input_t.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("destroy User 9")
            self.assertEqual(input_t.getvalue(), "** no instance found **\n")
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("create User")
            id = input_t.getvalue()[:-1]
            self.assertFalse(id == "")
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd(f"show User {id}")
            key = f"User.{id}"
            self.assertEqual(
                str(FileStorage._FileStorage__objects[key]),
                input_t.getvalue()[:-1]
            )
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd(f"destroy User {id}")
            self.assertEqual(input_t.getvalue(), "")
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd(f"show User {id}")
            key = f"User.{id}"
            self.assertEqual(
                "** no instance found **",
                input_t.getvalue()[:-1]
            )

    def test_do_all(self):
        """test do_all method"""
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("all Userfdsf")
            self.assertEqual(input_t.getvalue(), "** class doesn't exist **\n")
        self.reset()
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("create User")
            HBNBCommand().onecmd("create BaseModel")
            HBNBCommand().onecmd("create User")
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("all")
            values = "["
            for value in FileStorage._FileStorage__objects.values():
                if values != "[":
                    values += ", "
                values += f"\"{str(value)}\""
            values += "]"
            self.assertEqual(
                values,
                input_t.getvalue()[:-1]
            )
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("all User")
            values = "["
            for value in FileStorage._FileStorage__objects.values():
                if values != "[" and isinstance(value, User):
                    values += ", "
                if isinstance(value, User):
                    values += f"\"{str(value)}\""
            values += "]"
            self.assertEqual(
                values,
                input_t.getvalue()[:-1]
            )

    def test_do_update(self):
        """test de_update method"""
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("update")
            self.assertEqual(input_t.getvalue(), "** class name missing **\n")
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("update Userdasd")
            self.assertEqual(input_t.getvalue(), "** class doesn't exist **\n")
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("update User")
            self.assertEqual(input_t.getvalue(), "** instance id missing **\n")
        with patch('sys.stdout', new=StringIO()) as inpt:
            HBNBCommand().onecmd("update User 9")
            self.assertEqual(inpt.getvalue(), "** attribute name missing **\n")
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd("create User")
            id = input_t.getvalue()[:-1]
            self.assertFalse(id == "")
        with patch('sys.stdout', new=StringIO()) as inpt:
            HBNBCommand().onecmd(f"update User {id} name")
            self.assertEqual(inpt.getvalue(), "** value missing **\n")
        with patch('sys.stdout', new=StringIO()) as inpt:
            HBNBCommand().onecmd(f"update User {id} name John")
            self.assertEqual(inpt.getvalue(), "")
        with patch('sys.stdout', new=StringIO()) as input_t:
            HBNBCommand().onecmd(f"show User {id}")
            key = f"User.{id}"
            self.assertTrue(
                str(FileStorage._FileStorage__objects[key]),
                "John"
            )


if __name__ == "__main__":
    unittest.main()

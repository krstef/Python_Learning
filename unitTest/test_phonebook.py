import unittest

from phonebook import Phonebook

class PhonebookTest(unittest.TestCase):

    def test_create_phonebook(self):
        phonebook = Phonebook()
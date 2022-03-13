import unittest
from main import *


class TestApiCall(unittest.TestCase):

    def test_to_str(self):
        self.assertRaises(ValueError, to_str, 123)
        self.assertRaises(ValueError, to_str, "hola")
        self.assertRaises(ValueError, to_str, 123.42)

if __name__ == '__main__':
    unittest.main()

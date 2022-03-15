import unittest
from api_call import peticion


class TestApiCall(unittest.TestCase):

    def test_peticion(self):
        self.assertRaises(ValueError, peticion, 2,2)
        self.assertRaises(ValueError, peticion, "hola", "hola")

if __name__ == '__main__':
    unittest.main()

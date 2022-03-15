import unittest
from csv_converter import a_df


class TestApiCall(unittest.TestCase):

    def test_a_df(self):
        self.assertRaises(ValueError, a_df, 32412)
        self.assertRaises(ValueError, a_df, "data/dataset1.doc")

if __name__ == '__main__':
    unittest.main()

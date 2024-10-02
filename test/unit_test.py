import unittest
from ml_code.data_load import load_data

class TestDataLoader(unittest.TestCase):

    def test_load_data(self):
        data = load_data("data/data.csv")
        self.assertIsNotNone(data)
        self.assertNotEqual(len(data), 0)  # Ensure the file is not empty

if __name__ == '__main__':
    unittest.main()
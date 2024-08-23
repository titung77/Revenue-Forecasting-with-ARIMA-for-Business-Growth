import unittest
from app.data_loader import DataLoader
from config.settings import DATA_PATH


class TestDataLoader(unittest.TestCase):
    def setUp(self):
        self.data_loader = DataLoader(DATA_PATH)

    def test_load_and_preprocess(self):
        data = self.data_loader.load_and_preprocess()
        self.assertIsNotNone(data)
        self.assertIn("Revenue", data.columns)
        self.assertGreater(len(data), 0)


if __name__ == "__main__":
    unittest.main()

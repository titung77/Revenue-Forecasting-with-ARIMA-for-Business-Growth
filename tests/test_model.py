import unittest
from app.model import RevenueModel
from app.data_loader import DataLoader
from config.settings import DATA_PATH


class TestRevenueModel(unittest.TestCase):
    def setUp(self):
        data_loader = DataLoader(DATA_PATH)
        self.data = data_loader.load_and_preprocess()
        self.model = RevenueModel(self.data)

    def test_model_training(self):
        self.model.train()
        self.assertIsNotNone(self.model.model_fit)


if __name__ == "__main__":
    unittest.main()

import unittest
from app.evaluation import ModelEvaluator
from app.model import RevenueModel
from app.data_loader import DataLoader
from config.settings import DATA_PATH


class TestModelEvaluator(unittest.TestCase):
    def setUp(self):
        data_loader = DataLoader(DATA_PATH)
        data = data_loader.load_and_preprocess()
        model = RevenueModel(data)
        model.train()
        self.evaluator = ModelEvaluator(model, data)

    def test_evaluate(self):
        self.evaluator.evaluate()


if __name__ == "__main__":
    unittest.main()

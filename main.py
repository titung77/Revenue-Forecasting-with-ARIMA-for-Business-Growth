from app.data_loader import DataLoader
from app.model import RevenueModel
from app.evaluation import ModelEvaluator
from app.forecasting import RevenueForecaster
from config.settings import DATA_PATH

if __name__ == "__main__":
    # Khởi tạo các thành phần chính
    data_loader = DataLoader(DATA_PATH)
    data = data_loader.load_and_preprocess()

    model = RevenueModel(data)
    model.train()

    evaluator = ModelEvaluator(model, data)
    evaluator.evaluate()

    forecaster = RevenueForecaster(model)
    forecaster.forecast_for_specific_date(2024, 8)

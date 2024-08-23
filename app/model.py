from statsmodels.tsa.arima.model import ARIMA, ARIMAResults
import pandas as pd
import logging


class RevenueModel:
    def __init__(self, data: pd.DataFrame):
        self.data = data
        self.model_fit: ARIMAResults = None

    def train(self):
        try:
            logging.info("Training ARIMA model...")
            stepwise_fit_order = (5, 1, 0)
            # Dùng dữ liệu trừ 12 tháng cuối để huấn luyện
            months_ahead = 12
            train_data = self.data.iloc[:-months_ahead]  
            self.model_fit = ARIMA(
                train_data["Revenue"], order=stepwise_fit_order
            ).fit()
            logging.info(f"Model trained with order: {stepwise_fit_order}")
        except Exception as e:
            logging.error(f"Error during model training: {e}")
            raise

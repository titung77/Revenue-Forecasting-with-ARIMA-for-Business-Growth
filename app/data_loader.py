import pandas as pd
import numpy as np
from statsmodels.tsa.stattools import adfuller
import logging


class DataLoader:
    def __init__(self, file_path):
        self.file_path = file_path
        self.data = None

    def load_and_preprocess(self):
        try:
            logging.info("Loading data...")
            sales_data = pd.read_csv(self.file_path)
            sales_data["Date"] = pd.to_datetime(sales_data["Date"], format="%Y-%m-%d")
            daily_revenue = (
                sales_data.groupby("Date").agg({"Revenue": "sum"}).reset_index()
            )
            daily_revenue = daily_revenue.set_index("Date").asfreq("D", method="pad")
            monthly_revenue = (
                daily_revenue.resample("ME").sum().reset_index().set_index("Date")
            )

            if not self.is_data_stationary(monthly_revenue["Revenue"]):
                logging.info("Data is non-stationary. Applying log transformation.")
                monthly_revenue["Revenue"] = np.log1p(monthly_revenue["Revenue"])

            self.data = monthly_revenue
            return self.data
        except Exception as e:
            logging.error(f"Error loading or preprocessing data: {e}")
            raise

    @staticmethod
    def is_data_stationary(data):
        result = adfuller(data)
        return result[1] <= 0.05  # Dữ liệu dừng nếu p-value <= 0.05

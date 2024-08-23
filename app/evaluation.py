import matplotlib.pyplot as plt
from sklearn.metrics import mean_squared_error
import logging
import numpy as np
from app.model import RevenueModel
import pandas as pd
import streamlit as st
from statsmodels.tsa.seasonal import seasonal_decompose


class ModelEvaluator:
    def __init__(self, model: RevenueModel, data: pd.DataFrame):
        self.model = model
        self.data = data

    def evaluate(self):
        try:
            test_data = self.data.iloc[-12:]  # 12 tháng cuối để kiểm tra
            forecast = self.model.model_fit.forecast(steps=len(test_data))
            mse = mean_squared_error(test_data["Revenue"], forecast)
            rmse = np.sqrt(mse)
            logging.info(f"Model Evaluation - MSE: {mse:.2f}, RMSE: {rmse:.2f}")
        except Exception as e:
            logging.error(f"Error during model evaluation: {e}")
            raise

    @staticmethod
    def plot_forecast(test_data, forecast):
        plt.figure(figsize=(10, 6))
        plt.plot(
            test_data.index, test_data["Revenue"], label="Actual Data", color="green"
        )
        plt.plot(test_data.index, forecast, label="Forecasted Data", color="red")
        plt.title("Actual vs Forecasted Revenue")
        plt.legend()
        plt.show()

    def plot_forecast_ui(self):
        test_data = self.data.iloc[-12:]  # 12 tháng cuối để kiểm tra
        forecast = self.model.model_fit.forecast(steps=len(test_data))
        mse = mean_squared_error(test_data["Revenue"], forecast)
        rmse = np.sqrt(mse)
        st.write(f"Model Evaluation - MSE: {mse:.2f}, RMSE: {rmse:.2f}")
        st.line_chart(
            {"Actual Revenue": test_data["Revenue"], "Forecasted Revenue": forecast}
        )

    def plot_detailed_analysis(self):
        # Thêm các đồ thị chi tiết về seasonality, trend, hoặc decomposition
        st.write("Seasonal Decomposition")
        seasonal_decomposition = seasonal_decompose(self.data["Revenue"], model="additive")
        st.line_chart(seasonal_decomposition.seasonal)
        st.write("Trend Decomposition")
        st.line_chart(seasonal_decomposition.trend)
        st.write("Residual Decomposition")
        st.line_chart(seasonal_decomposition.resid)
        st.write("Overall Decomposition")
        st.line_chart(seasonal_decomposition.observed)

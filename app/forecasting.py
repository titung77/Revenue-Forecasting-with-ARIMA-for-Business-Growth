import logging
import pandas as pd
import matplotlib.pyplot as plt
from pandas.tseries.offsets import DateOffset
import streamlit as st
from app.model import RevenueModel


class RevenueForecaster:
    def __init__(self, model: RevenueModel):
        self.model = model

    def forecast_for_specific_date(self, year, month):
        try:
            input_date = pd.Timestamp(f"{year}-{month:02d}-01")
            last_date = self.model.data.index[-1]
            months_ahead = (input_date.year - last_date.year) * 12 + (input_date.month - last_date.month)
            forecast = self.model.model_fit.forecast(steps=months_ahead)
            predicted_revenue = forecast.iloc[-1]
            print(f"Predicted Revenue for {input_date.strftime('%B %Y')}: {predicted_revenue:.2f}")
            self.plot_forecast(input_date, months_ahead, forecast, last_date)
            self.plot_forecast_ui(input_date, months_ahead, forecast, last_date)
            logging.info(
                f"Predicted Revenue for {input_date.strftime('%B %Y')}: {predicted_revenue:.2f}"
            )
            return predicted_revenue
        except Exception as e:
            logging.error(f"Error during revenue forecasting: {e}")
            raise

    def plot_forecast(self, input_date, months_ahead, forecast, last_date):
        plt.figure(figsize=(12, 6))
        plt.plot(
            self.model.data.index, self.model.data["Revenue"], label="Actual Revenue"
        )
        future_dates = [last_date + DateOffset(months=i) for i in range(1, months_ahead + 1)]
        plt.plot(future_dates, forecast, label='Forecasted Revenue', color='red')
        plt.axvline(x=input_date, color='green', linestyle='--', label=f'Forecast for {input_date.strftime("%B %Y")}')
        plt.title('Monthly Revenue Prediction')
        plt.xlabel('Date')
        plt.ylabel('Revenue')
        plt.legend()
        plt.show()

    def plot_forecast_ui(self, input_date, months_ahead, forecast, last_date):
        # Plot the forecasted revenue
        fig, ax = plt.subplots()
        fig.set_size_inches(12, 6)
        ax.plot(
            self.model.data.index, self.model.data["Revenue"], label="Actual Revenue"
        )
        future_dates = [last_date + DateOffset(months=i) for i in range(1, months_ahead + 1)]
        ax.plot(future_dates, forecast, label='Forecasted Revenue', color='red')
        ax.axvline(x=input_date, color='green', linestyle='--', label=f'Forecast for {input_date.strftime("%B %Y")}')
        ax.set_title('Monthly Revenue Prediction')
        ax.set_xlabel('Date')
        ax.set_ylabel('Revenue')
        ax.legend()
        st.pyplot(fig)

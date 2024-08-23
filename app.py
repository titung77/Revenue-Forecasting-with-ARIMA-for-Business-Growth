import streamlit as st
import pandas as pd
from app.data_loader import DataLoader
from app.model import RevenueModel
from app.evaluation import ModelEvaluator
from app.forecasting import RevenueForecaster
from config.settings import DATA_PATH

# Cấu hình tiêu đề ứng dụng
st.title("Revenue Forecasting with ARIMA")

# Load và hiển thị dữ liệu
data_loader = DataLoader(DATA_PATH)
data = data_loader.load_and_preprocess()

st.subheader("Sales Data")
st.write(data)

# Huấn luyện mô hình
model = RevenueModel(data)
model.train()

# Đánh giá mô hình
evaluator = ModelEvaluator(model, data)
evaluator.evaluate()

with st.expander("Actual vs Forecasted Revenue"):
    evaluator.plot_forecast_ui()

with st.expander("Detailed Forecast Analysis"):
    evaluator.plot_detailed_analysis()

# Phần dự báo doanh thu cho tháng cụ thể
st.subheader("Forecast Revenue for a Specific Month")

year = st.number_input("Enter Year", min_value=2024, max_value=2030, value=2025)
month = st.number_input("Enter Month", min_value=1, max_value=12, value=1)

if st.button("Forecast"):
    forecaster = RevenueForecaster(model)
    predicted_revenue = forecaster.forecast_for_specific_date(year, month)
    st.write(f"Predicted Revenue for {month}/{year}: ${predicted_revenue:.2f}")

# Revenue Forecasting Application

This application forecasts monthly revenue using time series analysis with ARIMA. The project is designed with a modular structure to ensure scalability, maintainability, and ease of testing.

## Features

- Load and preprocess sales data from a CSV file.
- Automatically select the best ARIMA model parameters using auto_arima.
- Evaluate the model with MSE and RMSE metrics.
- Visualize the actual vs. forecasted revenue.
- Forecast revenue for specific future months.

## Project Structure

```cmd
revenue_forecasting/
│
├── app/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── model.py
│   ├── evaluation.py
│   └── forecasting.py
│
├── config/
│   ├── __init__.py
│   └── settings.py
│
├── notebooks/
│   └── exploratory_analysis.ipynb
│
├── tests/
│   ├── __init__.py
│   ├── test_data_loader.py
│   ├── test_model.py
│   └── test_evaluation.py
│
├── logs/
│   └── app.log
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── sales_data.csv
│
├── app.py
├── main.py
├── requirements.txt
└── README.md
```

## How to Run

Python 3.12.4

```cmd
python -m venv .venv 
```

1. Clone this repository.
2. Install the required packages:

```cmd
pip install -r requirements.txt
```

3. Run the application:

```cmd
python main.py
```

4. Run the web application:

```cmd
streamlit run app.py
```

5. Explore the data with the notebook:

```cmd
jupyter notebook notebooks/exploratory_analysis.ipynb
```

## Logging

All logs are stored in the `logs/app.log` file. You can monitor logs in real-time as the application runs.

## Testing

Run unit tests:

```cmd
python -m unittest discover tests
```

## Future Enhancements

- Extend the model to support additional forecasting methods.
- Integrate more advanced visualizations.
- Improve hyperparameter tuning with grid search.

## License

This project is licensed under the MIT License.

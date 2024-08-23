import os
import logging

# Đường dẫn dữ liệu
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data/sales_data.csv")

# Thiết lập logging
LOGGING_CONFIG = {
    "level": logging.INFO,
    "format": "%(asctime)s - %(levelname)s - %(message)s",
    "handlers": [
        logging.FileHandler(os.path.join(BASE_DIR, "logs/app.log")),
        logging.StreamHandler(),
    ],
}

logging.basicConfig(**LOGGING_CONFIG)

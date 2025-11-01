import pandas as pd
import os
from logger_config import get_logger
logger = get_logger(__name__)


def load_data(file_path):
    if not os.path.exists(file_path):
        logger.error("File not found: %s", file_path)
        raise FileNotFoundError(f"{file_path} not found.")
    try:
        logger.debug("reading file path")
        df1=pd.read_csv(file_path)
        logger.info("cleaning ")
        df1=df1.drop(columns=['Unnamed: 0'])
        logger.info("loaded data...")
    except Exception as e:
        logger.error("Failed to load data: %s", e)
    return df1

if __name__ == "__main__":
    #for testing only
    load_data(r'./week_1/day_1/Salary_dataset.csv')
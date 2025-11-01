import pandas as pd
import logging
import os

logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")


def load_data(file_path):
    if not os.path.exists(file_path):
        logging.error("File not found: %s", file_path)
        raise FileNotFoundError(f"{file_path} not found.")
    try:
        logging.debug("reading file path")
        df1=pd.read_csv(file_path)
        logging.debug("cleaning ")
        df1=df1.drop(columns=['Unnamed: 0'])
        logging.debug("loaded data...")
    except Exception as e:
        logging.error("Failed to load data: %s", e)
    return df1

if __name__ == "__main__":
    #for testing only
    load_data(r'./week_1/day_1/Salary_dataset.csv')
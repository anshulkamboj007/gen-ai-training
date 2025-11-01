import pandas as pd
import os
from logger_config import get_logger
logger = get_logger(__name__)

def load_data(config):
    file_path = config["data_path"]

    if not os.path.exists(file_path):
        logger.error("File not found: %s", file_path)
        raise FileNotFoundError(f"{file_path} not found.")

    try:
        logger.debug("Reading file")
        df1 = pd.read_csv(file_path)
        if 'Unnamed: 0' in df1.columns:
            df1 = df1.drop(columns=['Unnamed: 0'])
        logger.info(f"Loaded dataset with shape {df1.shape}")
    except Exception as e:
        logger.error("Failed to load data: %s", e)
        raise e

    return df1

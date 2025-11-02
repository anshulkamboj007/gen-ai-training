import yaml
from logger_config import get_logger
logger = get_logger(__name__)

def load_config(path='week_1\\day_1\\config\\config.yaml'):
    with open(path, 'r') as file:
        logger.info(f"done loadingg config file")
        return yaml.safe_load(file)

load_config(path='week_1\\day_1\\config\\config.yaml')
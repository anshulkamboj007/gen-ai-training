from sklearn.linear_model import LinearRegression
import logging
logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")

def train_model(X,y):
    try:
        logging.debug("creating model")
        model=LinearRegression()
        model.fit(X,y)
        logging.debug("model fit done")
    except Exception as e:
        logging.error("Failed to create / load model: %s", e)
    return model
    
    

from config_loader import load_config
from data_loader import load_data
from model_trainer import train_model
from evaluator import evaluate_model

def main():
    config = load_config()
    X_train, X_test, y_train, y_test = load_data(config)
    model, metrics = train_model(X_train, y_train, X_test, y_test, config)
    evaluate_model(model, metrics, config)

if __name__ == "__main__":
    main()
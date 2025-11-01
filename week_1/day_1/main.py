from config_loader import load_config
from data_loader import load_data
from model_trainer import train_model
from evaluator import evaluate_model

def main():
    config = load_config()
    df = load_data(config)

    # Split features/target
    X = df[["YearsExperience"]]
    y = df["Salary"]

    model, metrics = train_model(X, y, X, y)  # For now: test = train for sanity check
    results = evaluate_model(model, X, y)
    print(results)

if __name__ == "__main__":
    main()

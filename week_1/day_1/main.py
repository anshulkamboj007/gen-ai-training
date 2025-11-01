from data_loader import load_data
from model_trainer import train_model
from evaluator import evaluate_model
from visualizer import plot_regression

if __name__ == "__main__":
    # Step 1: Load
    df = load_data(r"./week_1/day_1/Salary_dataset.csv")
    X, y = df[['YearsExperience']], df['Salary']
    
    # Step 2: Train
    model = train_model(X, y)
    
    # Step 3: Evaluate
    metrics = evaluate_model(model, X, y)
    print("Model performance:", metrics)
    
    # Step 4: Visualize
    plot_regression(X, y, model)
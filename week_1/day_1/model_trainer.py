from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from mlflow.models.signature import infer_signature
import mlflow
import os
import joblib


def train_model(X_train, y_train, X_test, y_test):
    with mlflow.start_run():
        model = LinearRegression()
        model.fit(X_train, y_train)

        preds = model.predict(X_test)
        r2 = r2_score(y_test, preds)

        mlflow.log_param("model_type", "linear_regression_scratch")
        mlflow.log_metric("r2_score", r2)

        # --- Detect directory of the current file ---
        current_dir = os.path.dirname(os.path.abspath(__file__))
        log_dir = os.path.join(current_dir, "logs")
        os.makedirs(log_dir, exist_ok=True)

        log_path = os.path.join(log_dir, "train.log")
        os.makedirs("./week_1/day_1/model", exist_ok=True)
        joblib.dump(model, "./week_1/day_1/model/model.pkl")
        # Create or append to the train.log file
        if not os.path.exists(log_path):
            with open(log_path, "w") as f:
                f.write("Training log initialized.\n")

        with open(log_path, "a") as f:
            f.write(f"Model trained successfully.\nR2 Score: {r2:.4f}\n")

        # Log the log file as an artifact
        mlflow.log_artifact(log_path)

        # Build model signature and log model properly
        signature = infer_signature(X_test, preds)
        mlflow.sklearn.log_model(
            model,
            name="model",
            input_example=X_test[:1],
            signature=signature,
            pip_requirements=["scikit-learn", "mlflow"]
        )

    return model, {"r2_score": r2}

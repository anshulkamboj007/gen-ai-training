from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
import mlflow

def train_model(X_train, y_train, X_test, y_test):
    with mlflow.start_run():
        model = LinearRegression()
        model.fit(X_train, y_train)

        preds = model.predict(X_test)
        r2 = r2_score(y_test, preds)

        # Log metrics and parameters
        mlflow.log_param("model_type", "scratch")
        mlflow.log_metric("r2_score", r2)
        mlflow.log_artifact("logs/train.log")

        mlflow.sklearn.log_model(model, "model")

    
    

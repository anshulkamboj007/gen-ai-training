from sklearn.metrics import mean_squared_error, r2_score

def evaluate_model(model, X, y):
    y_pred = model.predict(X)
    return {
        "mse": mean_squared_error(y, y_pred),
        "r2": r2_score(y, y_pred)
    }
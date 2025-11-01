import matplotlib.pyplot as plt
import logging


def plot_regression(X, y, model):
    logging.getLogger('matplotlib').setLevel(logging.WARNING)
    logging.getLogger('PIL').setLevel(logging.WARNING)
    plt.scatter(X, y, color="blue")
    plt.plot(X, model.predict(X), color="red")
    plt.xlabel("Years of Experience")
    plt.ylabel("Salary")
    plt.title("Salary Prediction")
    plt.show()

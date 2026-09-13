from utilities import load_data, load_model
from model import estimate_price


def metrics(km: list[float], price: list[float], theta0: float, theta1: float) -> None:
    predictions = []

    for k in km:
        prediction = estimate_price(k, theta0, theta1)
        predictions.append(prediction)
    
    errors = []

    for pred, actual in zip(predictions, price):
        error = pred - actual
        errors.append(error)
    
    m = len(price)

    mae = sum(abs(e) for e in errors) / m
    rmse = (sum(e ** 2 for e in errors) / m) ** 0.5
    mean_price = sum(price) / m
    ss_tot = sum((p - mean_price) ** 2 for p in price)
    ss_res = sum(e ** 2 for e in errors)
    r2 = 1 - (ss_res / ss_tot) if ss_tot else 0.0

    print(f"Model metrics:\n")
    print(f"theta0 = {theta0:.6f}, theta1 = {theta1:.6f}")
    print(f"MAE  (mean absolute error) : {mae:.2f}")
    print(f"RMSE (root mean sq. error) : {rmse:.2f}")
    print(f"R^2  (coefficient of determination) : {r2:.4f}")


if __name__ == "__main__":
    data = load_data('data/data.csv')
    if data is None:
        print("Could not load data. Exiting.")
        exit(1)

    km, price = data

    model = load_model("model.csv")

    if model is None:
        exit(1)

    theta0, theta1 = model
    metrics(km, price, theta0, theta1)
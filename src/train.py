from model import estimate_price, normalize, denormalize_theta
from utilities import load_data, save_model

DEFAULT_LEARNING_RATE = 0.1
DEFAULT_STEPS = 1000
PROGRESS_INTERVAL = 100


def compute_cost(km_norm: list[float], price_norm: list[float],
                 theta0: float, theta1: float) -> float:
    m = len(km_norm)
    total_error = 0

    for i in range(m):
        pred = estimate_price(km_norm[i], theta0, theta1)
        error = pred - price_norm[i]
        total_error += error ** 2
    return total_error / (2 * m)


def calculate_gradient(km_norm: list[float],
                       price_norm: list[float], theta0: float,
                       theta1: float) -> tuple[float, float]:
    m = len(km_norm)
    sum_error0 = 0
    sum_error1 = 0

    for i in range(m):
        pred = estimate_price(km_norm[i], theta0, theta1)
        error = pred - price_norm[i]
        sum_error0 += error
        sum_error1 += error * km_norm[i]

    return (sum_error0 / m, sum_error1 / m)


def train(km_norm: list[float], price_norm: list[float],
          learning_rate: float=DEFAULT_LEARNING_RATE, steps: int=DEFAULT_STEPS,
          verbose=False) -> tuple[float, float]:
    theta0 = 0
    theta1 = 0

    for step in range(steps):
        grad_theta0, grad_theta1 = calculate_gradient(km_norm, price_norm, theta0, theta1)

        theta0 -= learning_rate * grad_theta0
        theta1 -= learning_rate * grad_theta1

        if verbose and step % PROGRESS_INTERVAL == 0:
            cost = compute_cost(km_norm, price_norm, theta0, theta1)
            print(f"    Iteration {step}: cost = {cost:.6f}")
    
    final_cost = compute_cost(km_norm, price_norm, theta0, theta1)
    print(f"Training completed. Final cost: {final_cost:.6f}")
    return theta0, theta1


if __name__ == "__main__":
    print("Starting training process for car prices.\n")

    data = load_data('data/data.csv')
    if data is None:
        print("Could not load data. Exiting.")
        exit(1)

    km, price = data

    print("Normalizing data")
    km_norm, km_min, km_max = normalize(km)
    price_norm, price_min, price_max = normalize(price)
    print("Training model")
    theta0_norm, theta1_norm = train(km_norm, price_norm, verbose=True)

    print("Denormalizing parameters")
    theta0_real, theta1_real = denormalize_theta(
        theta0_norm,
        theta1_norm,
        km_min,
        km_max,
    )

    print("Saving model parameters")
    save_model(theta0_real, theta1_real)

    print("\nTraining process completed.")

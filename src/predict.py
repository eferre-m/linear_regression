"""Module for predicting car prices based on mileage"""

import math
from model import estimate_price
from utilities import load_model


def validate_mileage_input(km_input: str) -> float | None:
    """
    Validates that mileage input is valid
    """
    try:
        km = float(km_input)
    except ValueError:
        print("Error: please enter a valid number")
        return None
    
    if not math.isfinite(km):
        print("Error: mileage must be a finite number")
        return None
    if km < 0:
        print("Error: mileage cannot be negative")
        return None
    if km >= 10000000:
        print("Error: mileage is unreasonably high")
        return None
    return km


def predict(theta0: float, theta1: float) -> None:
    """Run the interactive price prediction loop for a trained model."""
    print(f"Model equation: price = {theta0:.2f} + ({theta1:.6f}) × km\n")

    while True:
        try:
            km_input = input()

            if km_input.lower() in ['q', 'quit']:
                print("Goodbye!")
                break

            km = validate_mileage_input(km_input)
            if km is None:
                continue

            price = estimate_price(km, theta0, theta1)
            print(f"Estimated price: ${price:.2f}\n")

            print("-" * 23)
            print("\n")

        except (KeyboardInterrupt, EOFError):
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    model = load_model("model.csv")

    if model is None:
        model_theta0, model_theta1 = 0.0, 0.0
    else:
        model_theta0, model_theta1 = model

    predict(model_theta0, model_theta1)

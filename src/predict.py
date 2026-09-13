from model import estimate_price
from utilities import load_model

MAX_REASONABLE_MILEAGE = 1000000


def validate_mileage_input(km_input: str) -> float | None:
    """
    Validates that mileage input is valid
    """
    try:
        km = float(km_input)
        if km < 0:
            print("Warning: negative mileage, using absolute value")
            km = abs(km)
        if km > MAX_REASONABLE_MILEAGE:
            print("Warning: very high mileage, are you sure?")
        return km
    except ValueError:
        print("Error: please enter a valid number")
        return None
    

def predict(theta0: float, theta1: float) -> None:
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

        except KeyboardInterrupt:
            print("\nGoodbye!")
            break


if __name__ == "__main__":
    model = load_model("model.csv")

    if model is None:
        print("Cannot make predictions without trained model")
        exit(1)

    theta0, theta1 = model

    predict(theta0, theta1)

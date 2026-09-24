"""Module provinding functions for plotting"""

import os
import sys
import matplotlib.pyplot as plt
from utilities import load_data, load_model
from model import estimate_price


def plot(kms: list[float], price: list[float], t0: float, t1: float):
    """Function for plotting"""

    km_min, km_max = min(kms), max(kms)
    x_vals = list(range(int(km_min), int(km_max) + 1, 1000))
    y_vals = [estimate_price(x, t0, t1) for x in x_vals]

    plt.figure(figsize=(10, 6))
    
    plt.scatter(kms, price, color='blue', s=50, 
               label='Training Data')
    
    plt.plot(x_vals, y_vals, color='red', linewidth=2, 
             label='Regression Line')
    
    
    plt.title('Linear Regression')
    plt.xlabel('Mileage (km)')
    plt.ylabel('Price (€)')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()

    out_path = os.path.join(os.path.dirname(__file__), "..", "plot.png")
    plt.savefig(out_path)

    print("\nDisplaying plot... Close window to exit")
    plt.show()



if __name__ == "__main__":
    data = load_data('data/data.csv')
    if data is None:
        print("Could not load data. Exiting.")
        sys.exit(1)

    km, prices = data

    model = load_model("model.csv")

    if model is None:
        sys.exit(1)

    theta0, theta1 = model

    try:
        plot(km, prices, theta0, theta1)
        print("Plot closed successfully")
    except KeyboardInterrupt:
        print("\nInterrupted by user")
    finally:
        print("Goodbye!")

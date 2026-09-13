from utilities import load_data, load_model
from model import estimate_price
import matplotlib.pyplot as plt
import os


def plot(km: list[float], price: list[float], theta0: float, theta1: float):
    km_min, km_max = min(km), max(km)
    x_vals = list(range(int(km_min), int(km_max) + 1, 1000))
    y_vals = [estimate_price(x, theta0, theta1) for x in x_vals]

    plt.figure(figsize=(10, 6))
    
    plt.scatter(km, price, color='blue', s=50, 
               label='Training Data')
    
    plt.plot(x_vals, y_vals, color='red', linewidth=2, 
             label=f'Regression Line')
    
    
    plt.title('Linear Regression')
    plt.xlabel('Mileage (km)')
    plt.ylabel('Price (€)')
    plt.legend()
    plt.grid(True)

    plt.tight_layout()

    out_path = os.path.join(os.path.dirname(__file__), "..", "plot.png")
    plt.savefig(out_path)

    print(f"\nDisplaying plot... Close window to exit")
    plt.show()



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
    
    try:
        plot(km, price, theta0, theta1)
        print("Plot closed successfully")
    except KeyboardInterrupt:
        print("\nInterrupted by user")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        print("Goodbye!")
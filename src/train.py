import csv

KM_COLUMN = 'km'
PRICE_COLUMN = 'price'


def load_data(filename):
    km_list = []
    price_list = []

    try:
        with open(filename, 'r') as f:
            reader = csv.DictReader(f)
            for row in reader:
                km_list.append(float(row[KM_COLUMN]))
                price_list.append(float(row[PRICE_COLUMN]))
        print(f"Loaded {len(km_list)} rows from {filename}")
        return km_list, price_list
    except FileNotFoundError:
        print(f"Error: file '{filename}' not found")
        return [], []
    except KeyError as e:
        print(f"Error: column {e} not found in CSV")
        return [], []
    except ValueError as e:
        print(f"Error: invalid data in file - {e}")
        return [], []


def normalize(data):
    if not data:
        return [], 0, 0

    min_val = min(data)
    max_val = max(data)

    if max_val == min_val:
        print("Warning: all values are equal")

    norm = [(x - min_val) / (max_val - min_val) for x in data]
    return norm, min_val, max_val


def estimate_price(mileage: float, theta0: float, theta1: float) -> float:
    return theta0 + (theta1 * mileage)

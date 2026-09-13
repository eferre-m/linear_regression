import csv

KM_COLUMN = 'km'
PRICE_COLUMN = 'price'


def load_data(filename: str) -> tuple[list[float], list[float]]:
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


def save_model(theta0_real: float, theta1_real: float,
               filename: str = "model.csv") -> None:
    try:
        with open(filename, "w") as f:
            f.write(f"{theta0_real},{theta1_real}\n")
    except Exception as e:
        print(f"Error saving model: {e}")

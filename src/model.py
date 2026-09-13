def normalize(data: list) -> tuple[list[float], float, float]:
    if not data:
        return [], 0, 0

    min_val = min(data)
    max_val = max(data)

    if max_val == min_val:
        print("Warning: all values are equal")
        return [0.5] * len(data), min_val, max_val

    norm = [(x - min_val) / (max_val - min_val) for x in data]
    return norm, min_val, max_val


def estimate_price(km: float, theta0: float, theta1: float) -> float:
    return theta0 + (theta1 * km)


def denormalize_theta(theta0_norm: float, theta1_norm: float,
                      km_min: float, km_max: float, price_min: float,
                      price_max: float) -> tuple[float, float]:
    theta1_real = theta1_norm * (price_max - price_min) / (km_max - km_min)
    theta0_real = price_min + (price_max - price_min) * (theta0_norm - theta1_norm * km_min / (km_max - km_min))
    return theta0_real, theta1_real

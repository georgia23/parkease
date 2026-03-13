def calculate_fee(hours, vehicle_type):
    breakpoint()   # pause here to inspect values

    rates = {
        "car": 2000,
        "bike": 1000,
        "truck": 3000
    }

    fee = hours * rates[vehicle_type]
    return fee
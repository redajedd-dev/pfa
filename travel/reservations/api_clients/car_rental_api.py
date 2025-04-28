import requests

def get_cars(city, checkin, checkout):
    url = "https://api.locationvoituremaroc.com/search"
    headers = {
        "Authorization": "Bearer VOTRE_CLÉ_API_VOITURE"
    }
    params = {
        "city": city,
        "pickup_date": checkin,
        "return_date": checkout
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()['cars']

def get_cars_random():
    return [
        {"name": "Dacia Logan", "price": "25€/jour", "image": "car1.jpg"},
        {"name": "Hyundai i10", "price": "30€/jour", "image": "car2.jpg"},
    ]

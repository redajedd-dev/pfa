# api_clients/car_rental_api.py

import requests

def get_car_rentals(location, pickup_date, return_date):
    url = "https://booking-com15.p.rapidapi.com/api/v1/cars/searchCarRentals"

    querystring = {
        "location": location,    # Exemple: "Casablanca", "Marrakech"
        "pickup": pickup_date,
        "dropoff": return_date,
        "currency": "MAD"
    }

    headers = {
        "X-RapidAPI-Key": "69d7d4ac30msh724c579890bd22dp1b949cjsnf88a42125a1a",
        "X-RapidAPI-Host": "booking-com15.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    return response.json()

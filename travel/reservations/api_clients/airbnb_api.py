# api_clients/airbnb_api.py

import requests

def get_airbnb_locations(city, checkin_date, checkout_date, guests):
    url = "https://airbnb13.p.rapidapi.com/search-location"

    querystring = {
        "location": city,
        "checkin": checkin_date,
        "checkout": checkout_date,
        "adults": guests,
        "currency": "MAD"
    }

    headers = {
        "X-RapidAPI-Key": "TA_CLE_API",  # <<< Ta clé
        "X-RapidAPI-Host": "airbnb13.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    return response.json()

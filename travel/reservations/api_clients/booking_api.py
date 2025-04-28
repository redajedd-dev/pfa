# api_clients/booking_api.py

import requests

def get_booking_hotels(dest_id, checkin_date, checkout_date, adults_number):
    url = "https://booking-com15.p.rapidapi.com/api/v1/cars/searchCarRentals"

    querystring = {
        "dest_id": dest_id,  # Exemple : -1456928 pour Marrakech
        "dest_type": "city",
        "checkin_date": checkin_date,
        "checkout_date": checkout_date,
        "adults_number": adults_number,
        "locale": "fr",
        "currency": "MAD"
    }

    headers = {
        "X-RapidAPI-Key": "69d7d4ac30msh724c579890bd22dp1b949cjsnf88a42125a1a",  # <<< Remplacer par ta vraie clé RapidAPI
        "X-RapidAPI-Host": "booking-com15.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    return response.json()

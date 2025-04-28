import requests

def get_airbnb_homes(city, checkin, checkout):
    url = "https://api.airbnb.com/v2/search_results"
    headers = {
        "Authorization": "Bearer VOTRE_CLÉ_API_AIRBNB"
    }
    params = {
        "location": city,
        "check_in": checkin,
        "check_out": checkout,
        "guests": 2
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()['search_results']

def get_airbnb_homes_random():
    return [
        {"name": "Maison Berbère", "price": "70€", "image": "airbnb1.jpg"},
        {"name": "Riad Marrakech", "price": "90€", "image": "airbnb2.jpg"},
    ]

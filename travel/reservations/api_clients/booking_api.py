import requests

def get_booking_hotels(city, checkin, checkout):
    url = "https://api.booking.com/v1/search"
    headers = {
        "Authorization": "Bearer VOTRE_CLÉ_API_BOOKING"
    }
    params = {
        "city": city,
        "checkin_date": checkin,
        "checkout_date": checkout,
        "adults_number": 2,
    }
    response = requests.get(url, headers=headers, params=params)
    return response.json()['results']

def get_booking_hotels_random():
    # Simulation random (vraie API Booking à connecter)
    return [
        {"name": "Hotel Atlas", "price": "100€", "image": "hotel1.jpg"},
        {"name": "Hotel Agadir", "price": "80€", "image": "hotel2.jpg"},
    ]

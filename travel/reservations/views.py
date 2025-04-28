from django.shortcuts import render

# Create your views here.

def home_view(request):
    return render(request, 'home.html')


# reservations/views.py
from django.shortcuts import render
from .api_clients.booking_api import get_booking_hotels
from .api_clients.airbnb_api import get_airbnb_locations
from .api_clients.car_rental_api import get_car_rentals

def home_view(request):
    return render(request, 'home.html')

def hotels_view(request):
    return render(request, 'hotels.html')

def restaurants_view(request):
    return render(request, 'restaurants.html')

def activities_view(request):
    return render(request, 'activities.html')

def excursions_view(request):
    return render(request, 'excursions.html')

def admin_dashboard_view(request):
    return render(request, 'dashboard_admin.html')

def login_view(request):
    return render(request, 'login.html')

def signup_view(request):
    return render(request, 'signup.html')

def chatbot_view(request):
    return render(request, 'chatbot.html')

def search_view(request):
    service_type = request.GET.get('service_type')
    location = request.GET.get('location')
    price_range = request.GET.get('price_range')
    start_date = request.GET.get('start_date')
    end_date = request.GET.get('end_date')

    results = []

    if service_type == 'hebergement':
        results = get_booking_hotels(location, price_range, start_date, end_date)
    elif service_type == 'restaurant':
        results = get_airbnb_locations(location)
    elif service_type in ['activites', 'excursions']:
        results = get_airbnb_locations(location)

    return render(request, 'search_results.html', {'results': results})






#from django.shortcuts import render

# Create your views here.

#def home(request):
    #return render(request, 'home.html')





from django.shortcuts import render
from .api_clients.booking_api import get_booking_hotels
from .api_clients.airbnb_api import get_airbnb_homes
from .api_clients.car_rental_api import get_cars

def home(request):
    hotels = get_booking_hotels_random()
    homes = get_airbnb_homes_random()
    cars = get_cars_random()
    return render(request, 'home.html', {
        'hotels': hotels,
        'homes': homes,
        'cars': cars
    })

def search(request):
    service = request.GET.get('service')
    city = request.GET.get('city')
    checkin = request.GET.get('checkin')
    checkout = request.GET.get('checkout')

    if service == 'hotel':
        results = get_booking_hotels(city, checkin, checkout)
    elif service == 'airbnb':
        results = get_airbnb_homes(city, checkin, checkout)
    elif service == 'car':
        results = get_cars(city, checkin, checkout)
    else:
        results = []

    return render(request, 'search.html', {
        'results': results,
        'service': service
    })

def login_view(request):
    return render(request, 'login.html')

def signup_view(request):
    return render(request, 'signup.html')




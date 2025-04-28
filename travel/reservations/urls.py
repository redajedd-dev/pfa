


# reservations/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('search/', views.search_view, name='search'),
    path('hotels/', views.hotels_view, name='hotels'),
    path('restaurants/', views.restaurants_view, name='restaurants'),
    path('activities/', views.activities_view, name='activities'),
    path('excursions/', views.excursions_view, name='excursions'),
    path('dashboard/', views.admin_dashboard_view, name='dashboard'),
    path('login/', views.login_view, name='login'),
    path('signup/', views.signup_view, name='signup'),
    path('chatbot/', views.chatbot_view, name='chatbot'),
]




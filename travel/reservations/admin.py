from django.contrib import admin

# Register your models here.


from .models import Logement, Voiture, Restaurant, Reservation ,Hebergement





admin.site.register(Hebergement)

admin.site.register(Logement)
admin.site.register(Voiture)
admin.site.register(Restaurant)
admin.site.register(Reservation)

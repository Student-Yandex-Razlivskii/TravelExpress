from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('add/', add, name='add'),
    path('login/', login, name='login'),
    path('ship/<int:ship_id>/', show_ship, name='ship'),
    path('traveler/<int:traveler_id>/', show_traveler, name='traveler'),
    path('port/<int:port_id>/', show_port, name='port'),
    path('сaptain/<int:сaptain_id>/', show_сaptain, name='сaptain')
]

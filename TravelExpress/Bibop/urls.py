from django.urls import path

from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('about/', about, name='about'),
    path('add/', add, name='add'),
    path('login/', login, name='login'),
    path('ship/<int:ship_id>/', show_ship, name='ship')
]

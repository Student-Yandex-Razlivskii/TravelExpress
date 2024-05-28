from django.http import HttpResponse
from django.shortcuts import render

from .models import *
menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить корабль", 'url_name': 'add'},
        {'title': "Войти", 'url_name': 'login'}
        ]

def index(request): 
  
  context = {
    
    'menu': menu,
    'title': 'Главная страница'
  }
  
  return render(request, 'Travels/index.html', context=context)

def about(request):
  return render(request, 'Travels/about.html', {'title': 'О сайте'})

def add(request):
  return HttpResponse("Добавление корабля")

def login(request):
  return HttpResponse("Авторизация")

def show_ship(request, ship_id):
  return HttpResponse(f"Отображение корабля с id = {ship_id}")

def show_traveler(request, traveler_id):
  return HttpResponse(f"Отображение корабля с id = {traveler_id}")

def show_port(request, port_id):
  return HttpResponse(f"Отображение корабля с id = {port_id}")

def show_сaptain(request, сaptain_id):
  return HttpResponse(f"Отображение корабля с id = {сaptain_id}")
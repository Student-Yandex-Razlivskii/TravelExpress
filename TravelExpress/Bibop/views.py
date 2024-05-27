from django.http import HttpResponse
from django.shortcuts import render

from .models import *
menu = ["О сайте", "Добавить корабль", "Войти"]

def arcadia(request): 
  posts = Ships.objects.all()
  return render(request, 'Travels/index.html', {'posts': posts,'menu': menu, 'title': 'Главная страница'})

def about(request):
  return render(request, 'Travels/about.html', {'title': 'О сайте'})
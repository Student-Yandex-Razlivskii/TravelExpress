from django.http import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render

from .models import *
menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить корабль", 'url_name': 'add'},
        {'title': "Войти", 'url_name': 'login'}
        ]

def index(request): 
  posts = Ships.objects.all()
  
  context = {
    'posts': posts,
    'menu': menu,
    'title': 'Главная страница',
    'port_selected': 0,
  }
  
  return render(request, 'Travels/index.html', context=context)

def about(request):
  context = {
    
    'menu': menu,
    'title': 'О нашем сайте'
  }
                
  return render(request, 'Travels/about.html', context=context)
  
  
  

def add(request):
  return HttpResponse("Добавление корабля")

def login(request):
  return HttpResponse("Авторизация")

def show_ship(request, ship_id):
  ship = get_object_or_404(Ships, pk=ship_id)

def show_traveler(request, traveler_id):
  return HttpResponse(f"Отображение корабля с id = {traveler_id}")

def show_port(request, port_id):
   posts = Ships.objects.filter(port=port_id)
   if len(posts) == 0:
        raise Http404()

   context = {
        'posts': posts,
        'menu': menu,
        'title': 'Отображение по рубрикам',
        'cat_selected': port_id,
    }
   return render(request, 'Travels/index.html', context=context)


def show_сaptain(request, сaptain_id):
  return HttpResponse(f"Отображение корабля с id = {сaptain_id}")
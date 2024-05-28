from django import template
from Bibop.models import *

register = template.Library()

@register.simple_tag(name='getship')
def get_ships():
  return Ships.objects.all()
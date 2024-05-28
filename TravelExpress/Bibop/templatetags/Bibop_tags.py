from django import template
from Bibop.models import *

register = template.Library()

@register.simple_tag(name='getports')
def get_ports(filter=None):
    if not filter:
        return Ports.objects.all()
    else:
        return Ports.objects.filter(pk=filter)

@register.inclusion_tag('Travels/list_ports.html')
def show_ports(sort=None, port_selected=0):
    if not sort:
        ports = Ports.objects.all()
    else:
        ports = Ports.objects.order_by(sort)

    return {"ports": ports, "port_selected": port_selected}

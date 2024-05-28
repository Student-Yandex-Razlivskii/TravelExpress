from django.contrib import admin

from .models import *

class TravelerAdmin(admin.ModelAdmin):
  list_display = ('id', 'name')
  list_display_links = ('id', 'name')
  search_fields = ('name',)
  

class ShipAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'price')
  list_display_links = ('id', 'name')
  search_fields = ('name', 'price')
  list_editable = ('price',)

class PortAdmin(admin.ModelAdmin):
  list_display = ('id', 'name')
  list_display_links = ('id', 'name')
  search_fields = ('name',)

class CaptainAdmin(admin.ModelAdmin):
  list_display = ('id', 'name')
  list_display_links = ('id', 'name')
  search_fields = ('name',)

admin.site.register(Travelers, TravelerAdmin)
admin.site.register(Ships, ShipAdmin)
admin.site.register(Ports, PortAdmin)
admin.site.register(Captains, CaptainAdmin)
from django.contrib import admin

from .models import *

class TravelerAdmin(admin.ModelAdmin):
  list_display = ('id', 'name')
  list_display_links = ('id', 'name')
  search_fields = ('name',)
  

class ShipAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'Price')
  list_display_links = ('id', 'name')
  search_fields = ('name', 'Price')
  list_editable = ('Price',)

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

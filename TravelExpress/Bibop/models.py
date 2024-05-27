from django.db import models
from django.urls import reverse

class Ships(models.Model):
  name = models.CharField(max_length=255)
  Price = models.IntegerField(max_length=255)
  departure_port_id = models.ForeignKey('Ports', on_delete=models.PROTECT)
  captain_id = models.ForeignKey('Captains', on_delete=models.PROTECT)
  traveler_id = models.ForeignKey('Travelers', on_delete=models.PROTECT)

class Ports(models.Model):
  name = models.CharField(max_length=255)
  
class Captains(models.Model):
  name = models.CharField(max_length=255)

class Travelers(models.Model):
  name = models.CharField(max_length=255)

def __str__(self):
    return self.name
  
def get_absolute_url(self):
    return reverse('ship', kwargs={"ship_id": self.pk})


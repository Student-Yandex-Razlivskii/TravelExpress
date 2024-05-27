from django.db import models

class Ships(models.Model):
  name = models.CharField(max_length=255)
  Price = models.IntegerField(max_length=255)
  departure_port_id = models.IntegerField(max_length=255)
  captain_id = models.IntegerField(max_length=255)
  traveler_id = models.IntegerField(max_length=255)

class Ports(models.Model):
  name = models.CharField(max_length=255)
  
class Captains(models.Model):
  name = models.CharField(max_length=255)

class Travelers(models.Model):
  name = models.CharField(max_length=255)

def __str__(self):
    return self.name

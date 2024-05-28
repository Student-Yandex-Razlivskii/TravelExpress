from django.db import models
from django.urls import reverse

class Ships(models.Model):
  name = models.CharField(max_length=255, verbose_name="Имя корабля")
  Price = models.IntegerField(verbose_name="Цена")
  departure_port_id = models.ForeignKey('Ports', on_delete=models.PROTECT, verbose_name="Порт")
  captain_id = models.ForeignKey('Captains', on_delete=models.PROTECT, verbose_name="Капитан")
  traveler_id = models.ForeignKey('Travelers', on_delete=models.PROTECT, verbose_name="Путешественник")
  
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('ship', kwargs={"ship_id": self.pk})
  
  class Meta:
    verbose_name = 'Известные корабли'
    verbose_name_plural = 'Известные корабли'
    ordering = ['Price','name']

class Ports(models.Model):
  name = models.CharField(max_length=255, verbose_name="Имя порта")
  
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('port', kwargs={"port_id": self.pk})
  
  class Meta:
    verbose_name = 'Известные порты'
    verbose_name_plural = 'Известные порты'
    ordering = ['name']
  
class Captains(models.Model):
  name = models.CharField(max_length=255, verbose_name="Имя капитана")
  
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('сaptain', kwargs={"сaptain_id": self.pk})
  
  class Meta:
    verbose_name = 'Известные капитаны'
    verbose_name_plural = 'Известные капитаны'
    ordering = ['name']

class Travelers(models.Model):
  name = models.CharField(max_length=255, verbose_name="Имя путешественника")
  
  def __str__(self):
    return self.name
  
  def get_absolute_url(self):
    return reverse('ship', kwargs={"ship_id": self.pk})
  
  class Meta:
    verbose_name = 'Известные путешественники'
    verbose_name_plural = 'Известные путешественники'
    ordering = ['name']




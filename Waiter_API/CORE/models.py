from django.db import models

class Client(models.Model): # < Will configure the Client label
    Id = models.IntegerField(primary_key=True, blank=False) # < Column configuration
    Name = models.CharField(max_length=50, blank=False)

class Order(models.Model):
    Id = models.IntegerField(primary_key=True, blank=False)
    Order = models.CharField(max_length=255, blank=False)
    Name = models.CharField(max_length=50, blank=False)
    Price = models.FloatField(blank=False)

class Menu(models.Model):
    Id = models.IntegerField(primary_key=True, blank=False)
    Food = models.CharField(max_length=50, blank=False)
    Price = models.FloatField(blank=False)
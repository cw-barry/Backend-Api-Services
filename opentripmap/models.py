from operator import mod
from xml.parsers.expat import model
from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=30)
    country = models.CharField(max_length=5)
    lat = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)
    lon = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)
    population = models.IntegerField()
    timezone = models.CharField(max_length=30)

    def __str__(self):
        return self.name

class Places(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, related_name="places")
    xid = models.CharField(max_length=15)
    name = models.CharField(max_length=30)
    # dist = models.DecimalField(max_digits=10, decimal_places=8, blank=True, null=True)
    osm = models.CharField(max_length=15, null=True)
    wikidata = models.CharField(max_length=15, null=True)
    kinds = models.CharField(max_length=150, null=True)
    # lat = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)
    # lon = models.DecimalField(max_digits=18, decimal_places=15, blank=True, null=True)
    image = models.URLField(null=True)
    text = models.TextField(null=True)
    html = models.TextField(null=True)

    def __str__(self):
        return self.name

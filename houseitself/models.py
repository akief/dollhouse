from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    
    def __str__(self):
        return self.part

class Doll(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    location = models.ForeignKey(Location)
    
    def __str__(self):
        return self.name

class Article(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=100)
    dolls = models.ManyToManyField(Doll)
    
    def __str__(self):
        return self.name
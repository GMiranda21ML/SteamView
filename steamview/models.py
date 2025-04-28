from django.db import models

# Create your models here.
class Jogos(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    rating = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    image = models.URLField()
    released_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.name
    
class HistoricoPesquisa(models.Model):
    name = models.CharField(max_length=150)
    frequency = models.IntegerField()

    def __str__(self):
        return self.name

class MaisJogados(models.Model):
    name = models.CharField(max_length=150)
    players = models.CharField(max_length=15)
    image = models.URLField()

    def __str__(self):
        return self.name

class MaisJogadosHist(models.Model):
    name = models.CharField(max_length=150)
    rating = models.CharField(max_length=15)
    released = models.CharField(max_length=15)
    image = models.URLField()

    def __str__(self):
        return self.name

class MenosJogadosHist(models.Model):
    name = models.CharField(max_length=150)
    rating = models.CharField(max_length=15)
    released = models.CharField(max_length=15)
    image = models.URLField(blank=True)

    def __str__(self):
        return self.name
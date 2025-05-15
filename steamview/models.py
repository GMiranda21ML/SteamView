from django.db import models
from django.contrib.auth.models import User

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
    
class WishList(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="wishlist")
    games = models.ManyToManyField(Jogos, related_name="wishlist_by", blank=True)

    def __str__(self):
        return f"Wishlist de {self.user.username}"


class WishListItem(models.Model):
    wishlist = models.ForeignKey(WishList, on_delete=models.CASCADE)
    game = models.ForeignKey(Jogos, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('wishlist', 'game')
        ordering = ['-added_at']

    def __str__(self):
        return f"{self.game.name} na wishlist de {self.wishlist.user.username}"
from django.db import models

# Create your models here.
class Jogos(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    rating = models.CharField(max_length=20)
    price = models.CharField(max_length=20)
    image = models.URLField()

    def __str__(self):
        return self.name
from django.db import models


class Pokemon(models.Model):
    title = models.TextField()
    image = models.ImageField(null=True)

    def __str__(self):
        if self.title:
            return self.title


class PokemonEntity(models.Model):
    lat = models.FloatField()
    lon = models.FloatField()
    realtion_pokemons = models.ForeignKey(Pokemon, on_delete=models.CASCADE, null=True)
from django.db import models


class Pokemon(models.Model):
    name_ru = models.CharField(max_length=200, null=False, blank=False, verbose_name='Имя на русском')
    name_en = models.CharField(max_length=200, blank=True, verbose_name='Имя на английском')
    name_jp = models.CharField(max_length=200, blank=True, verbose_name='Имя на японском')
    photo = models.ImageField(blank=True, null=True, upload_to='photos_of_pokemons', verbose_name='Фотография')
    description = models.TextField(blank=True, verbose_name='Описание')
    previous_evolution = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE,
                                           related_name='next_evolutions', verbose_name='Из кого эволюционировал')

    def __str__(self):
        return f'{self.name_ru}'


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, null=False, blank=False,
                                related_name='entities', verbose_name='Покемон')
    lat = models.FloatField(null=False, blank=False, verbose_name='Широта')
    lon = models.FloatField(null=False, blank=False, verbose_name='Долгота')
    appeared_at = models.DateTimeField(blank=True, null=True, verbose_name='Появится')
    disappeared_at = models.DateTimeField(blank=True, null=True, verbose_name='Исчезнет')
    level = models.PositiveBigIntegerField(null=True, blank=True, verbose_name='Уровень')
    health = models.PositiveBigIntegerField(null=True, blank=True, verbose_name='Здоровье')
    strength = models.PositiveBigIntegerField(null=True, blank=True, verbose_name='Атака')
    defence = models.PositiveBigIntegerField(null=True, blank=True, verbose_name='Защита')
    stamina = models.PositiveBigIntegerField(null=True, blank=True, verbose_name='Выносливость')

    def __str__(self):
        return f'{self.pokemon}'

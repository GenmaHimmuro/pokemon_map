# Generated by Django 3.1.14 on 2025-04-07 06:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name_ru', models.CharField(max_length=200, verbose_name='Имя на русском')),
                ('name_en', models.CharField(blank=True, max_length=200, verbose_name='Имя на английском')),
                ('name_jp', models.CharField(blank=True, max_length=200, verbose_name='Имя на японском')),
                ('photo', models.ImageField(blank=True, null=True, upload_to='photos_of_pokemons', verbose_name='Фотография')),
                ('description', models.TextField(blank=True, verbose_name='Описание')),
                ('previous_evolution', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='next_evolutions', to='pokemon_entities.pokemon', verbose_name='Из кого эволюционировал')),
            ],
        ),
        migrations.CreateModel(
            name='PokemonEntity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.FloatField(verbose_name='Широта')),
                ('lon', models.FloatField(verbose_name='Долгота')),
                ('appeared_at', models.DateTimeField(blank=True, null=True, verbose_name='Появится')),
                ('disappeared_at', models.DateTimeField(blank=True, null=True, verbose_name='Исчезнет')),
                ('level', models.IntegerField(blank=True, null=True, verbose_name='Уровень')),
                ('health', models.IntegerField(blank=True, null=True, verbose_name='Здоровье')),
                ('strength', models.IntegerField(blank=True, null=True, verbose_name='Атака')),
                ('defence', models.IntegerField(blank=True, null=True, verbose_name='Защита')),
                ('stamina', models.IntegerField(blank=True, null=True, verbose_name='Выносливость')),
                ('pokemon', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='entities', to='pokemon_entities.pokemon', verbose_name='Имя на русском')),
            ],
        ),
    ]

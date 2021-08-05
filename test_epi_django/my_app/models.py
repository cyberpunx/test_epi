from django.db import models


class Game(models.Model):

    GENRE_CHOICES = (
        ('sandbox', 'Sandbox'),
        ('fps', 'Disparos en Primera Persona'),
        ('rpg', 'Juego de Rol'),
        ('rts', 'Estrategia en Tiempo Real'),
        ('city_builder', 'Construcción de Ciudades'),
        ('survival', 'Supervivencia'),
    )

    PLATFORM_CHOICES = (
        ('win', 'Microsoft Windows'),
        ('macos', 'macOS'),
        ('playstation4', 'Playstation 4'),
        ('xboxone', 'Xbox One'),
        ('android', 'Android'),
    )

    name = models.CharField(blank=False, null=False, max_length=50, verbose_name="Nombre")
    publisher = models.CharField(blank=False, null=False, max_length=50, verbose_name="Distribuidora")
    developer = models.CharField(blank=False, null=False, max_length=50, verbose_name="Desarrollador")
    release_date = models.DateField(blank=False, null=False, verbose_name="Fecha de Publicación")
    genre = models.CharField(blank=False, null=False, choices=GENRE_CHOICES, max_length=50, verbose_name="Género")
    platform = models.CharField(blank=False, null=False, choices=PLATFORM_CHOICES, max_length=50, verbose_name="Plataforma")

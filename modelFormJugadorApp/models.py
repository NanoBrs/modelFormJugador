from django.db import models

# Create your models here.
class Jugador(models.Model):
    POSICIONES = [
        ('Base', 'Base'),
        ('Escolta', 'Escolta'),
        ('Alero', 'Alero'),
        ('Ala-Pivot', 'Ala-Pivot'),
        ('Pivot', 'Pivot')
    ]

    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    ppp = models.FloatField()  # Puntos por partido
    eficacia = models.FloatField()
    posicion = models.CharField(max_length=20, choices=POSICIONES)  # Aquí usamos un campo con opciones
    edad = models.IntegerField()
    campeonatos = models.IntegerField()
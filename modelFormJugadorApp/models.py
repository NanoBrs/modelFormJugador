from django.db import models
from django.core.exceptions import ValidationError

class Jugador(models.Model):
    POSICIONES = [
        ('Base', 'Base'),
        ('Escolta', 'Escolta'),
        ('Alero', 'Alero'),
        ('Ala-Pivot', 'Ala-Pivot'),
        ('Pivot', 'Pivot')
    ]

    nombre = models.CharField(max_length=40)
    apellido = models.CharField(max_length=40)
    ppp = models.FloatField()  # Puntos por partido
    eficacia = models.FloatField()
    posicion = models.CharField(max_length=20, choices=POSICIONES)  
    edad = models.IntegerField()
    campeonatos = models.IntegerField()

    def clean(self):
        super().clean()  # Llama a la validación del modelo base

        # Validación para nombre: Verifica si hay números
        if any(char.isdigit() for char in self.nombre):
            raise ValidationError({'nombre': 'El nombre no puede contener números.'})

        # Validación para apellido: Verifica si hay números
        if any(char.isdigit() for char in self.apellido):
            raise ValidationError({'apellido': 'El apellido no puede contener números.'})

        # Validación para PPP
        if self.ppp < 0:
            raise ValidationError({'ppp': 'Los puntos por partido no pueden ser negativos.'})

        # Validación para Edad
        if self.edad < 0:
            raise ValidationError({'edad': 'La edad no puede ser negativa.'})
        if self.edad < 18:
            raise ValidationError({'edad': 'La edad no puede ser menor a 18.'})

        # Validación para Campeonatos
        if self.campeonatos < 0:
            raise ValidationError({'campeonatos': 'El número de campeonatos no puede ser negativo.'})

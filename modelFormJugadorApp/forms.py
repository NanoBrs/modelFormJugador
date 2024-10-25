from django import forms 
from modelFormJugadorApp.models import Jugador
from django.core.exceptions import ValidationError

class FormJugador(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'ppp': forms.NumberInput(attrs={'class': 'form-control'}),
            'eficacia': forms.NumberInput(attrs={'class': 'form-control'}),
            'posicion': forms.Select(attrs={'class': 'form-select'}),
            'edad': forms.NumberInput(attrs={'class': 'form-control'}),
            'campeonatos': forms.NumberInput(attrs={'class': 'form-control'}),
        }

        
   
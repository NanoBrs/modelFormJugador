from django import forms 
from modelFormJugadorApp.models import Jugador
class FormJugador(forms.ModelForm):
    class Meta:
        model = Jugador
        fields = '__all__'
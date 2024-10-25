from django.contrib import admin
from modelFormJugadorApp.models import Jugador
# Register your models here.

class JugadorAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'posicion', 'edad', 'campeonatos','eficacia','ppp')

admin.site.register(Jugador,JugadorAdmin)
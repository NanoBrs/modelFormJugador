from django.shortcuts import render,redirect
from modelFormJugadorApp.forms import FormJugador
from modelFormJugadorApp.models import Jugador

# Create your views here.
def index(request):
    return render(request, 'modelFormJugadorApp/index.html')

def listadoJugadores(request):
    jugadores = Jugador.objects.all()
    data = {'jugadores' : jugadores}
    return render (request, 'modelFormJugadorApp/jugadores.html' , data)

def agregarJugador (request):
    form = FormJugador()
    if request.method == 'POST':
        form = FormJugador(request.POST)
    if form.is_valid():
        form.save()
        return listadoJugadores(request)
    data = {'form' : form}
    return render(request, 'modelFormJugadorApp/agregarJugador.html', data)

def eliminarJugador(request,id):
    proyecto = Jugador.objects.get(id = id)
    proyecto.delete()
    return redirect('../jugadores/')

def actualizarJugador(request,id):
    proyecto= Jugador.objects.get(id = id)
    form = FormJugador(instance=proyecto)
    if request.method == 'POST' :
        form = FormJugador(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
        return index(request)
    data ={'form':form}
    return render(request,'modelFormJugadorApp/agregarJugador.html',data)

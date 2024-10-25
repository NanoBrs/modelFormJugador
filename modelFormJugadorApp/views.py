from django.shortcuts import get_object_or_404,render,redirect
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
    data = {'form' : form,
            'titulo':'Agregar Jugador',
            'boton':'Añadir'}
    return render(request, 'modelFormJugadorApp/agregarJugador.html', data)

def eliminarJugador(request,id):
    proyecto = Jugador.objects.get(id = id)
    proyecto.delete()
    return redirect('../jugadores/')

def actualizarJugador(request, id):

    jugador = get_object_or_404(Jugador, id=id)

    if request.method == 'POST':

        form = FormJugador(request.POST, instance=jugador)
        if form.is_valid():
            form.save()  
            return redirect('../jugadores/')  
    else:

        form = FormJugador(instance=jugador)
    data = {'form': form,
            'titulo':'Actualizar Jugador',
            'boton':'Actualizar'}
    return render(request, 'modelFormJugadorApp/agregarJugador.html', data)

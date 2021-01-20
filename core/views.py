from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
from core.models import Evento


def get_local(request, titulo_evento):
    evento = Evento.objects.get(titulo=titulo_evento)
    return HttpResponse(evento.local)


def lista_eventos(request):
    usuario = request.user
    evento = Evento.objects.filter(usuario=usuario)
    dados = {'eventos':evento}
    return render(request, 'agenda.html', dados)


def index(request):
    return redirect('/agenda/')
from django.shortcuts import render, HttpResponse

# Create your views here.
from core.models import Evento


def getLocal(request, titulo_evento):
    evento = Evento.objects.get(titulo=titulo_evento)
    return HttpResponse(evento.local)

from django.db import models
from django.contrib.auth.models import User
from datetime import datetime


# Create your models here.


class Evento(models.Model):
    titulo = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    local = models.TextField(verbose_name='Local do evento')
    data_evento = models.DateTimeField(verbose_name='Data do Evento')
    data_criacao = models.DateTimeField(auto_now=True)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'eventos'

    def __str__(self):
        return self.titulo

    def atrasado(self):
        if self.data_evento < datetime.now():
            return True
        return False

    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y %H:%M')
    
    def get_data_from_evento(self):
        return self.data_evento.strftime('%Y-%m-%d')

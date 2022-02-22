from django.db import models

# Create your models here.
class Imovel(models.Model):
    nome_dono = models.CharField(max_length=100)
    contato_dono = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    data_cadastro = models.DateTimeField(auto_now_add=True)

class Acionamento(models.Model):
    switch_bool = models.BooleanField()
    data_request = models.DateTimeField(auto_now_add=True)

class Status(models.Model):
    status_bool = models.BooleanField()
    data_request = models.DateTimeField(auto_now_add=True)

class Sensor(models.Model): #ATIVA NOTIFICACAO DE ALARME
    imovel_sensor = models.CharField(max_length=100)
    data_request = models.DateTimeField(auto_now_add=True)

class Notificacao(models.Model): #IMPRIME acesso suspeito - DADOS IMOVEL
    data_request = models.DateTimeField(auto_now_add=True)
from django.db import models

# Create your models here.
class Imovel(models.Model): # Dados do imovel
    nome_dono = models.CharField(max_length=100)
    contato_dono = models.CharField(max_length=100)
    endereco = models.CharField(max_length=100)
    data_cadastro = models.DateTimeField(auto_now_add=True)

class Acionamento(models.Model): # Liga ou desliga o Status automatico
    switch_bool = models.BooleanField()
    data_request = models.DateTimeField(auto_now_add=True)

class Status(models.Model): # Notificacao a cada 30 segundos do status. Apenas caso ultimo acionamento for true
    status_bool = models.BooleanField()
    data_request = models.DateTimeField(auto_now_add=True)

class Sensor(models.Model): # Cria ums notificacao, passando o Sensor e Imovel
    imovel_id = models.CharField(max_length=5)
    imovel_sensor = models.CharField(max_length=100)
    data_request = models.DateTimeField(auto_now_add=True)

class Notificacao(models.Model): #IMPRIME acesso suspeito com dados do imovel e sensor
    imovel_id = models.CharField(max_length=5)
    data_request = models.DateTimeField(auto_now_add=True)
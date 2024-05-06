from django.db import models
from django.conf import settings

# Create your models here.
class Funcionario(models.Model):
    nome_funcionario = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_funcionario

class Cliente(models.Model):
    nome_cliente = models.CharField(max_length=100)
    cnpj = models.CharField(max_length=25, blank=True)
    telefone = models.CharField(max_length=25, blank=True)
    empresa = models.CharField(max_length=100, default='', blank=True)

    def __str__(self):
        return self.nome_cliente

class Sistema(models.Model):
    nome_sistema = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_sistema

class Prioridade(models.Model):
    nome_prioridade = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_prioridade

class Status(models.Model):
    nome_status = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_status    

class TipoChamado(models.Model):
    nome_tipo = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_tipo    

class Chamado(models.Model):
    titulo = models.CharField(max_length=100)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    prioridade = models.ForeignKey(Prioridade, on_delete=models.CASCADE, default=2)
    data = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    descricao = models.TextField(max_length=1000)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=1)
    tipo_chamado = models.ForeignKey(TipoChamado, on_delete=models.CASCADE, default=2)
    resolucao = models.TextField(max_length=1000, blank=True)
    sistema = models.ForeignKey(Sistema, on_delete=models.CASCADE)
    solicitante = models.CharField(max_length=100, blank=True)


class EventoCalendario(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100)
    funcionario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE)
    data_inicio = models.DateField(auto_now=False, auto_now_add=False, blank=True)
    data_final = models.DateField(auto_now=False, auto_now_add=False, blank=True)

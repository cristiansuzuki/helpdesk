from django.db import models

# Create your models here.

class Funcionario(models.Model):
    nome_funcionario = models.CharField(max_length=100)


class Cliente(models.Model):
    nome_cliente = models.CharField(max_length=100)
    cnpj = models.IntegerField(max_length=20)
    telefone = models.IntegerField(max_length=20)

class Sistema(models.Model):
    nome_sistema = models.CharField(max_length=100)

class Prioridade(models.Model):
    nome_prioridade = models.CharField(max_length=100)

class Status(models.Model):
    nome_status = models.CharField(max_length=100)

class TipoChamado(models.Model):
    nome_tipo = models.CharField(max_length=100)

class Chamado(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE)
    prioridade = models.ForeignKey(Prioridade, on_delete=models.CASCADE)
    data = models.DateTimeField(auto_now=True)
    descricao = models.CharField(max_length=1000)
    status = models.ForeignKey(Status, on_delete=models.CASCADE)
    tipo = models.ForeignKey(TipoChamado, on_delete=models.CASCADE)
    resolução = models.CharField(max_length=1000)
    sistema = models.ForeignKey(Sistema, on_delete=models.CASCADE)
    solicitante = models.CharField(max_length=100)
    





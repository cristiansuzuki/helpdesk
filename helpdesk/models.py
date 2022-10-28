from django.db import models
from django.conf import settings

# Create your models here.
class Funcionario(models.Model):
    nome_funcionario = models.CharField(max_length=100)

    def __str__(self):
        return self.nome_funcionario

class Cliente(models.Model):
    nome_cliente = models.CharField(max_length=100)
    cnpj = models.IntegerField()
    telefone = models.IntegerField()
    empresa = models.CharField(max_length=100, default='')

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
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    funcionario = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,)
    prioridade = models.ForeignKey(Prioridade, on_delete=models.CASCADE, default=2)
    data = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    descricao = models.TextField(max_length=1000)
    status = models.ForeignKey(Status, on_delete=models.CASCADE, default=1)
    tipo_chamado = models.ForeignKey(TipoChamado, on_delete=models.CASCADE, default=1)
    resolucao = models.TextField(max_length=1000)
    sistema = models.ForeignKey(Sistema, on_delete=models.CASCADE)
    solicitante = models.CharField(max_length=100)

from django import forms
from .models import *
from django.contrib.auth.models import User


class ClienteForm(forms.Form):
    class Meta:
        model = Cliente
        fields = ('nome_cliente', 'cnpj', 'telefone', 'empresa')
        widgets = {
            'nome_cliente':forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'id': 'exampleInputName', 'placeholder': 'Nome do Cliente'}),
            'cnpj':forms.TextInput(
                attrs={'type':'number', 'class':'form-control', 'id': 'exampleInputNumber', 'placeholder': 'CNPJ do Cliente'}),
            'telefone':forms.TextInput(
                attrs={'type':'number', 'class':'form-control', 'id': 'exampleInputNumber', 'placeholder': 'Numero do Cliente'}),
            'empresa':forms.TextInput(
                attrs={'type':'text', 'class':'form-control', 'id': 'exampleInputName', 'placeholder': 'Empresa'}),    
        }

class ChamadoForm(forms.Form):
    class Meta:
        fields = ('cliente', 'funcionario', 'prioridade', 'data', 'descricao', 'status', 'tipo_chamado', 'resolucao', 'sistema', 'solicitante')
        widgets = {
            'cliente':forms.Select(
                attrs={'type': 'select', 'class': 'form-control', 'id': 'exampleInputSelect',
                       'placeholder': '', 'value': '10'}),
            'funcionario':forms.Select(
                attrs={'type': 'select', 'class': 'form-control', 'id': 'exampleInputSelect',
                       'placeholder': '', 'value': '10'}),
            'prioridade':forms.Select(
                attrs={'type': 'select', 'class': 'form-control', 'id': 'exampleInputSelect',
                       'placeholder': '', 'value': '10'}),
            'data': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control form-control-user', 'id': 'exampleInputDate',
                       'placeholder': 'Data de criação do chamado'}),
            'descricao': forms.TextInput(
                  attrs={'type': 'text', 'class': 'form-control', 'id': 'exampleInputName', 'placeholder': 'Descricao do chamado'}),
            'status': forms.Select(
                attrs={'type': 'select', 'class': 'form-control', 'id': 'exampleInputSelect',
                       'placeholder': '', 'value': '10'}),                
            'tipo_chamado': forms.Select(
                attrs={'type': 'select', 'class': 'form-control', 'id': 'exampleInputSelect',
                       'placeholder': '', 'value': '10'}),
            'resolucao': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'id': 'exampleInputName', 'placeholder': 'Resolução do chamado'}),     
            'sistema': forms.Select(
                attrs={'type': 'select', 'class': 'form-control', 'id': 'exampleInputSelect', 'placeholder': '', 'value': '10'}),
            'solicitante': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'id': 'exampleInputName', 'placeholder': 'Solicitante do chamado'})
}
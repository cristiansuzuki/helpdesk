from django import forms
from .models import Cliente, Chamado

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nome_cliente', 'cnpj', 'telefone', 'empresa')
        widgets = {
            'nome_cliente': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control form-control-user', 'id': 'exampleFirstName', 'placeholder': 'Nome do Cliente'}),
            'cnpj': forms.NumberInput(
                attrs={'type':'number', 'class':'form-control form-control-user', 'id': 'exampleInputNumber', 'placeholder': 'CNPJ do Cliente'}),
            'telefone': forms.NumberInput(
                attrs={'type':'number', 'class':'form-control form-control-user', 'id': 'exampleInputNumber', 'placeholder': 'Numero do Cliente'}),
            'empresa': forms.TextInput(
                attrs={'type':'text', 'class':'form-control form-control-user', 'id': 'exampleInputName', 'placeholder': 'Empresa'}),    
        }

class ChamadoForm(forms.ModelForm):

    class Meta:
        model = Chamado
        fields = ('cliente', 'funcionario', 'prioridade', 'descricao', 'status', 'tipo_chamado', 'resolucao', 'sistema', 'solicitante')
        widgets = {
            'cliente':forms.Select(
                attrs={'type': 'select', 'class': 'form-control', 'id': 'exampleFormControlSelect1', 'placeholder': '', 'value': ''}),
            'funcionario':forms.Select(
                attrs={'type': 'select', 'class': 'form-control', 'id': 'exampleInputSelect', 'placeholder': '', 'value': '10'}),
            'prioridade':forms.Select(
                attrs={'type': 'select', 'class': 'form-control', 'id': 'exampleInputSelect', 'placeholder': '', 'value': '10'}),
            'descricao': forms.Textarea(
                  attrs={'type': 'text', 'class': 'form-control', 'id': 'exampleInputName', 'placeholder': 'Descrição do chamado!'}),
            'status': forms.Select(
                attrs={'type': 'select', 'class': 'form-control', 'id': 'exampleInputSelect', 'placeholder': '', 'value': '10'}),                
            'tipo_chamado': forms.Select(
                attrs={'type': 'select', 'class': 'form-control', 'id': 'exampleInputSelect', 'placeholder': '', 'value': '10'}),
            'resolucao': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'id': 'exampleInputName', 'placeholder': ''}),     
            'sistema': forms.Select(
                attrs={'type': 'select', 'class': 'form-control', 'id': 'exampleInputSelect', 'placeholder': '', 'value': '10'}),
            'solicitante': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'id': 'exampleInputName', 'placeholder': ''}),
        }

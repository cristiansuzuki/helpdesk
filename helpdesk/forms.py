from django import forms
from .models import Cliente, Chamado, EventoCalendario

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ('nome_cliente', 'cnpj', 'telefone', 'empresa')
        widgets = {
            'nome_cliente': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control form-control-user', 'id': 'exampleFirstName', 'placeholder': 'Nome do Cliente'}),
            'cnpj': forms.NumberInput(
                attrs={'type':'text', 'class':'form-control form-control-user', 'id': 'id_cnpj', 'placeholder': 'CNPJ do Cliente'}),
            'telefone': forms.NumberInput(
                attrs={'type':'text', 'class':'form-control form-control-user', 'id': 'id_telefone', 'placeholder': 'Numero do Cliente'}),
            'empresa': forms.TextInput(
                attrs={'type':'text', 'class':'form-control form-control-user', 'id': 'exampleInputName', 'placeholder': 'Empresa'}),    
        }

        def __init__(self, *args, **kwargs):
            super(ClienteForm, self).__init__(*args, **kwargs)
            self.fields['cnpj', 'telefone','empresa'].required = False

class ChamadoForm(forms.ModelForm):

    class Meta:
        model = Chamado
        fields = ('titulo', 'cliente', 'funcionario', 'prioridade', 'descricao', 'status', 'tipo_chamado', 'resolucao', 'sistema', 'solicitante')
        widgets = {
            'titulo': forms.TextInput(
                  attrs={'type': 'text', 'class': 'form-control', 'id': 'exampleInputName', 'placeholder': 'Titulo do chamado'}),
            'cliente':forms.Select(
                attrs={'type': 'select', 'class': 'form-control', 'id': 'exampleFormControlSelect1', 'placeholder': '', 'value': ''}),
            'funcionario':forms.Select(
                attrs={'type': 'select', 'class': 'form-control', 'id': 'exampleInputSelect', 'placeholder': '', 'value': '10'}),
            'prioridade':forms.Select(
                attrs={'type': 'select', 'class': 'form-control', 'id': 'exampleInputSelect', 'placeholder': '', 'value': '10'}),
            'descricao': forms.Textarea(
                  attrs={'type': 'text', 'class': 'form-control', 'id': 'exampleInputName', 'placeholder': 'Descrição do chamado'}),
            'status': forms.Select(
                attrs={'type': 'select', 'class': 'form-control', 'id': 'exampleInputSelect', 'placeholder': '', 'value': '10'}),                
            'tipo_chamado': forms.Select(
                attrs={'type': 'select', 'class': 'form-control', 'id': 'exampleInputSelect', 'placeholder': '', 'value': '10'}),
            'resolucao': forms.Textarea(
                attrs={'type': 'text', 'class': 'form-control', 'id': 'exampleInputName', 'placeholder': 'Resolução do chamado'}),     
            'sistema': forms.Select(
                attrs={'type': 'select', 'class': 'form-control', 'id': 'exampleInputSelect', 'placeholder': '', 'value': '10'}),
            'solicitante': forms.TextInput(
                attrs={'type': 'text', 'class': 'form-control', 'id': 'exampleInputName', 'placeholder': ''}),
        }

class EventoForm(forms.ModelForm):

    class Meta:
        model = EventoCalendario
        fields = ('titulo', 'funcionario', 'data_inicio', 'data_final')
        widgets = {
            'titulo': forms.TextInput(
                  attrs={'type': 'text', 'class': 'form-control', 'id': 'exampleInputName', 'placeholder': 'Titulo do evento'}), 
            'funcionario':forms.Select(
                attrs={'type': 'select', 'class': 'form-control', 'id': 'exampleInputSelect', 'placeholder': '', 'value': '10'}),
            'data_inicio': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control', 'id': 'exampleInputName', 'placeholder': ''}),
            'data_final': forms.DateInput(
                attrs={'type': 'date', 'class': 'form-control', 'id': 'exampleInputName', 'placeholder': ''}),         
        }

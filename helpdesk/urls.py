from django.urls import path
from .views import home, lista_chamados, cadastro_cliente, cadastro_chamados, buttons, cards, login, register, forgot_password, error_404, blank

urlpatterns = [
    path('', home, name='home'),
    path('lista-chamados', lista_chamados, name='lista-chamados'),
    path('cadastro-cliente', cadastro_cliente, name='cadastro-cliente'),
    path('cadastro-chamados', cadastro_chamados, name='cadastro-chamados'),
    path('buttons', buttons, name='buttons'),
    path('cards', cards, name='cards'),
    path('login', login, name='login'),
    path('register', register, name='register'),
    path('forgot-password', forgot_password, name='forgot-password'),
    path('error_404', error_404, name='error_404'),
    path('blank', blank, name='blank'),
]

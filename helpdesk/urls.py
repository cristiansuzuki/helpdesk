from django.urls import path
from .views import home, calendario, lista_chamados, chamado, cadastro_cliente, cadastro_chamados, register, forgot_password, error_404, blank, lista_chamados_fechados, lista_chamados_andamento

urlpatterns = [
    path('', home, name='home'),
    path('lista-chamados', lista_chamados, name='lista-chamados'),
    path('lista-chamados-fechados', lista_chamados_fechados, name='lista-chamados-fechados'),
    path('lista-chamados-andamento', lista_chamados_andamento, name='lista-chamados-andamento'),
    path('chamado/<int:id>', chamado, name='chamado'),
    path('cadastro-cliente', cadastro_cliente, name='cadastro-cliente'),
    path('cadastro-chamados', cadastro_chamados, name='cadastro-chamados'),
    path('calendario', calendario, name='calendario'),
    path('register', register, name='register'),
    path('forgot-password', forgot_password, name='forgot-password'),
    path('error_404', error_404, name='error_404'),
]

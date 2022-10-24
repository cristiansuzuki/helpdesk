from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Cliente)
admin.site.register(Funcionario)
admin.site.register(Prioridade)
admin.site.register(Sistema)
admin.site.register(Status)
admin.site.register(TipoChamado)
admin.site.register(Chamado)

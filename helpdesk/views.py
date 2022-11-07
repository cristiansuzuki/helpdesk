from django.shortcuts import render
from .forms import ClienteForm, ChamadoForm
from .models import Chamado
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.
def home(request):
    chamados = Chamado.objects.all()
    num_chamados_abertos = len(Chamado.objects.filter(status__nome_status="ABERTO"))
    num_chamados_inicio = len(Chamado.objects.filter(status__nome_status="ANDAMENTO"))
    num_chamados_finalizado = len(Chamado.objects.filter(status__nome_status="FECHADO"))
    num_chamados_pendentes = len(Chamado.objects.filter(status__nome_status="PENDENTE"))
    return render(request, 'home.html', {'chamados': chamados, 'num_chamados_abertos':num_chamados_abertos, 'num_chamados_inicio':num_chamados_inicio, 'num_chamados_finalizado':num_chamados_finalizado, 'num_chamados_pendentes':num_chamados_pendentes})

def calendario(request):
    return render(request, 'calendario.html')

def lista_chamados(request):
    chamados = Chamado.objects.all()
    chamados_abertos = Chamado.objects.filter(status__nome_status="ABERTO")
    return render(request, 'lista-chamados.html', {'chamados': chamados, 'chamados_abertos': chamados_abertos})

def lista_chamados_fechados(request):
    chamados = Chamado.objects.all()
    chamados_fechados = Chamado.objects.filter(status__nome_status="FECHADO")
    return render(request, 'lista-chamados-fechados.html', {'chamados': chamados, 'chamados_fechados': chamados_fechados})

def lista_chamados_andamento(request):
    chamados = Chamado.objects.all()
    chamados_andamento = Chamado.objects.filter(status__nome_status="ANDAMENTO")
    return render(request, 'lista-chamados-andamento.html', {'chamados': chamados, 'chamados_andamento': chamados_andamento})

def chamado(request, id):
    chamado = Chamado.objects.get(pk=id)
    form = ChamadoForm(request.POST or None, instance=chamado)
    if form.is_valid():
        form.save()
        return redirect(home)
    return render(request, 'chamado.html', {'chamado':chamado, 'form':form})

def cadastro_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Cliente criado com sucesso !')
            return redirect('cadastro-cliente')
    else:
        form = ClienteForm()
    return render(request, 'cadastro-cliente.html', {'form': form})

def cadastro_chamados(request):
    if request.method == 'POST':
        form = ChamadoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Chamado criado com sucesso !')
            return redirect('cadastro-chamados')
    else:
        form = ChamadoForm()
    return render(request, 'cadastro-chamados.html', {'form': form})

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def error_404(request):
    return render(request, '404.html')

def blank(request):
    return render(request, 'blank.html')

def forgot_password(request):
    return render(request, 'forgot-password.html')

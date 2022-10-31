from django.shortcuts import render
from .forms import ClienteForm, ChamadoForm
from .models import Chamado
from django.shortcuts import redirect

# Create your views here.
def home(request):
    chamados = Chamado.objects.all()
    num_chamados_abertos = len(Chamado.objects.filter(status__nome_status="Aberto"))
    num_chamados_inicio = len(Chamado.objects.filter(status__nome_status="Início"))
    num_chamados_finalizado = len(Chamado.objects.filter(status__nome_status="Finalizado"))
    num_chamados_pendentes = len(Chamado.objects.filter(status__nome_status="Pendentes"))
    return render(request, 'home.html', {'chamados': chamados, 'num_chamados_abertos':num_chamados_abertos, 'num_chamados_inicio':num_chamados_inicio, 'num_chamados_finalizado':num_chamados_finalizado, 'num_chamados_pendentes':num_chamados_pendentes})

def lista_chamados(request):
    chamados = Chamado.objects.all()
    chamados_abertos = Chamado.objects.filter(status__nome_status="Aberto")
    return render(request, 'lista-chamados.html', {'chamados': chamados, 'chamados_abertos': chamados_abertos})

def cadastro_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
    else:
        form = ClienteForm()
    return render(request, 'cadastro-cliente.html', {'form': form})

def cadastro_chamados(request):
    if request.method == 'POST':
        form = ChamadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(home)
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

def buttons(request):
    return render(request, 'buttons.html')

def cards(request):
    return render(request, 'cards.html')

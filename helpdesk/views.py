from django.shortcuts import render
from .forms import ClienteForm, ChamadoForm
from .models import Chamado
from django.shortcuts import redirect

# Create your views here.
def home(request):
    return render(request, 'home.html')

def lista_chamados(request):
    chamados = Chamado.objects.all()
    return render(request, 'lista-chamados.html', {'chamados': chamados})

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

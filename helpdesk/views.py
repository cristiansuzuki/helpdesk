from django.shortcuts import render
from .forms import *
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User
from django.views.decorators.http import require_POST

# Views de CADASTRO

def cadastro_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, '', {'form': form})
    # alterar caminho de cadastro do cliente aqui e na URL
    # criar ELSE

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def error_404(request):
    return render(request, '404.html')

def blank(request):
    return render(request, 'blank.html')

def tables(request):
    return render(request, 'tables.html')

def forgot_password(request):
    return render(request, 'forgot-password.html')

def buttons(request):
    return render(request, 'buttons.html')

def cards(request):
    return render(request, 'cards.html')
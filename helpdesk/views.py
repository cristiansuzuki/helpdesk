from django.shortcuts import render
from .forms import ClienteForm
from .models import Cliente
from django.shortcuts import redirect

# Create your views here.
def home(request):
    return render(request, 'home.html')

def cadastro_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            newform = Cliente(
                nome_cliente=form.changed_data['nome_cliente'],
                cnpj=form.changed_data['cnpj'],
                telefone=form.changed_data['telefone'],
                empresa=form.changed_data['empresa']
            )
            newform.save()
            return redirect(home)
    else:
        form = ClienteForm()
    return render(request, 'cadastro-cliente.html', {'form': form})

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

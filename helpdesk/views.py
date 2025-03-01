from django.shortcuts import render
from .forms import ClienteForm, ChamadoForm, EventoForm, ClienteForm, EventoForm
from .models import Chamado, EventoCalendario, Cliente, EventoCalendario
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import JsonResponse

@login_required
def home(request):
    chamados = Chamado.objects.filter(Q(status__nome_status="PENDENTE") | Q(status__nome_status="ANDAMENTO")).order_by('data')
    for chamado in chamados:
        if chamado.status.id == 3:
            chamado.color_class = 'text-success'
        elif chamado.status.id == 2:
            chamado.color_class = 'text-warning'
        else:
            chamado.color_class = 'text-primary'
    chamados_fechados_usuario = len(Chamado.objects.filter(funcionario=request.user).filter(status__nome_status="CONCLUIDO"))
    chamados_pendentes_usuario = len(Chamado.objects.filter(funcionario=request.user).filter(status__nome_status="PENDENTE"))
    chamados_andamento_usuario = len(Chamado.objects.filter(funcionario=request.user).filter(status__nome_status="ANDAMENTO"))
    num_chamados_abertos = len(Chamado.objects.filter(status__nome_status="ABERTO"))
    num_chamados_inicio = len(Chamado.objects.filter(status__nome_status="ANDAMENTO"))
    num_chamados_finalizado = len(Chamado.objects.filter(status__nome_status="CONCLUIDO"))
    num_chamados_pendentes = len(Chamado.objects.filter(status__nome_status="PENDENTE"))
    return render(request, 'home.html', {'chamados': chamados, 'chamados_fechados_usuario' : chamados_fechados_usuario , 'chamados_pendentes_usuario' : chamados_pendentes_usuario , 'chamados_andamento_usuario' : chamados_andamento_usuario , 'num_chamados_abertos':num_chamados_abertos, 'num_chamados_inicio':num_chamados_inicio, 'num_chamados_finalizado':num_chamados_finalizado, 'num_chamados_pendentes':num_chamados_pendentes})

@login_required
def calendario(request):
    return render(request, 'calendario.html')

@login_required
def lista_chamados(request):
    chamados = Chamado.objects.all()
    chamados_abertos = Chamado.objects.filter(status__nome_status="PENDENTE")
    return render(request, 'lista-chamados.html', {'chamados': chamados, 'chamados_abertos': chamados_abertos})

@login_required
def lista_chamados_fechados(request):
    chamados = Chamado.objects.all()
    chamados_fechados = Chamado.objects.filter(status__nome_status="CONCLUIDO")
    return render(request, 'lista-chamados-fechados.html', {'chamados': chamados, 'chamados_fechados': chamados_fechados})

@login_required
def lista_chamados_andamento(request):
    chamados = Chamado.objects.all()
    chamados_andamento = Chamado.objects.filter(status__nome_status="ANDAMENTO")
    return render(request, 'lista-chamados-andamento.html', {'chamados': chamados, 'chamados_andamento': chamados_andamento})

@login_required
def chamado(request, id):
    chamado = Chamado.objects.get(pk=id)
    form = ChamadoForm(request.POST or None, instance=chamado)
    if form.is_valid():
        form.save()
        messages.success(request, f'Chamado editado com sucesso !')
        return redirect(home)
    return render(request, 'chamado.html', {'chamado':chamado, 'form':form})

@login_required
def cadastro_chamados(request):
    if request.method == 'POST':
        form = ChamadoForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, f'Chamado criado com sucesso !')
            return redirect(home)
    else:
        form = ChamadoForm()
    return render(request, 'cadastro-chamados.html', {'form': form})

@login_required
def register(request):
    return render(request, 'register.html')

@login_required
def error_404(request):
    return render(request, '404.html')

@login_required
def blank(request):
    return render(request, 'blank.html')

@login_required
def forgot_password(request):
    return render(request, 'forgot-password.html')

@login_required
def calendario(request):  
    all_events = EventoCalendario.objects.all()
    context = {
        "events":all_events,
    }
    return render(request,'calendario.html',context)

@login_required
def lista_clientes(request):
    clientes = Cliente.objects.all().order_by('nome_cliente')
    return render(request, 'lista-clientes.html', {'clientes': clientes})

@login_required
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

@login_required
def cliente(request, id):
    cliente = Cliente.objects.get(pk=id)
    form = ClienteForm(request.POST or None, instance=cliente)
    if form.is_valid():
        form.save()
        messages.success(request, f'Cliente editado com sucesso !')
        return redirect(home)
    return render(request, 'cliente.html', {'cliente':cliente, 'form':form})

@login_required
def cadastro_eventos(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(calendario)
    else:
        form = EventoForm()
    return render(request, 'cadastro-eventos.html', {'form':form})

@login_required
def lista_evento(request):
    eventos = EventoCalendario.objects.all().order_by('-id')
    return render(request, 'lista-eventos.html', {'eventos': eventos})

@login_required
def delete_evento(request, id):
    delete_evento = EventoCalendario.objects.get(pk=id)
    delete_evento.delete()
    messages.success(request, f'Evento deletado com sucesso')
        
    return render(request, 'home.html', {'delete_evento':delete_evento})
from django.shortcuts import render, redirect, HttpResponse
from .models import Cliente
from .entidades import cliente
from .forms import ClienteForm
from .services import cliente_service
# Create your views here.

def listarClientes(request):
    clientes = cliente_service.listar_clientes()
    context = {'clientes': clientes}
    return render(request, 'listaClientes.html', context)

def inserir_cliente(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        if form.is_valid():
            nome = form.cleaned_data["nome"]
            sexo = form.cleaned_data["sexo"]
            date = form.cleaned_data["date"]
            email = form.cleaned_data["email"]
            profissao = form.cleaned_data["profissao"]
            cliente_novo = cliente.Cliente(nome=nome, sexo=sexo, date=date, email=email, 
                                           profissao=profissao)
            cliente_service.cadastrar_cliente(cliente_novo)
            #form.save()
            #form = ClienteForm()
            return redirect('listarClientes')
    else:
        form = ClienteForm()
    context = {'form': form}
    return render(request, 'formCliente.html', context)

def listar_cliente_id(request, id):
    cliente = cliente_service.listar_cliente_id(id)
    context = {'cliente': cliente}
    return render(request, 'listaCliente.html' ,context)

def editar_cliente_id(request, id):
    cliente_encontrado = cliente_service.listar_cliente_id(id)
    form = ClienteForm(request.POST or None, instance=cliente_encontrado)
    if form.is_valid():
        nome = form.cleaned_data["nome"]
        sexo = form.cleaned_data["sexo"]
        date = form.cleaned_data["date"]
        email = form.cleaned_data["email"]
        profissao = form.cleaned_data["profissao"]
        cliente_novo = cliente.Cliente(nome=nome, sexo=sexo, date=date, email=email, 
                                       profissao=profissao)
        cliente_service.editar_cliente(cliente_encontrado, cliente_novo)
        return redirect('listarClientes')
    context = {'form': form}
    return render(request, 'formCliente.html', context)

def remover_cliente(request, id):
    cliente = cliente_service.listar_cliente_id(id)
    if request.method == 'POST':
        cliente_service.remover_cliente(cliente)
        return redirect('listarClientes')
    context = {'cliente': cliente}
    return render(request, 'excluirCliente.html', context)
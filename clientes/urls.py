from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('listar', listarClientes, name='listarClientes'),
    path('cadastrar', inserir_cliente, name="cadastrarCliente"),
    path('listar/<int:id>', listar_cliente_id, name="listarClienteId"),
    path('editar/<int:id>', editar_cliente_id, name="editarClienteId"),
    path('remover/<int:id>', remover_cliente, name="excluirClienteId")
    ]
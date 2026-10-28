"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from lava_jato.views import(ServicoListView, ServicoCreateView, ServicoUpdateView, ServicoDeleteView, 
PessoaFisicaListView, PessoaFisicaCreateView, PessoaFisicaUpdateView, PessoaFisicaDeleteView,
PessoaJuridicaListView, PessoaJuridicaCreateView, PessoaJuridicaUpdateView, PessoaJuridicaDeleteView, 
VeiculoListView, VeiculoCreateView, VeiculoUpdateView, VeiculoDeleteView, MovimentoListView, 
MovimentoCreateView, MovimentoUpdateView, MovimentoDeleteView, painel_pagamentos, dashboard)
from django.urls import include
from django.contrib import admin
from django.urls import path
from django.views.generic.base import TemplateView

urlpatterns = [
    path('', TemplateView.as_view(template_name='base.html'), name='home'),
    path('admin/', admin.site.urls),
    path('contas/', include('django.contrib.auth.urls')),
    path('servicos/', ServicoListView.as_view(), name='servico_list'),
    path('servico/novo/', ServicoCreateView.as_view(), name='servico_create'),
    path('servicos/editar/<uuid:pk>/', ServicoUpdateView.as_view(), name='servico_update'),
    path('servicos/excluir/<uuid:pk>/', ServicoDeleteView.as_view(), name='servico_delete'), 
    path('clientes/fisica/', PessoaFisicaListView.as_view(), name='pessoafisica_list'),
    path('clientes/fisica/novo/', PessoaFisicaCreateView.as_view(), name='pessoafisica_create'),
    path('clientes/fisica/editar/<uuid:pk>/', PessoaFisicaUpdateView.as_view(), name='pessoafisica_update'),
    path('clientes/fisica/excluir/<uuid:pk>/', PessoaFisicaDeleteView.as_view(), name='pessoafisica_delete'),
    path('clientes/juridica/', PessoaJuridicaListView.as_view(), name='pessoajuridica_list'),
    path('clientes/juridica/novo/', PessoaJuridicaCreateView.as_view(), name='pessoajuridica_create'),
    path('clientes/juridica/editar/<uuid:pk>/', PessoaJuridicaUpdateView.as_view(), name='pessoajuridica_update'),
    path('clientes/juridica/excluir/<uuid:pk>/', PessoaJuridicaDeleteView.as_view(), name='pessoajuridica_delete'),
    path('veiculos/', VeiculoListView.as_view(), name='veiculo_list'),
    path('veiculo/novo/', VeiculoCreateView.as_view(), name='veiculo_create'),
    path('veiculo/editar/<uuid:pk>/', VeiculoUpdateView.as_view(), name='veiculo_update'),
    path('veiculo/excluir/<uuid:pk>/', VeiculoDeleteView.as_view(), name='veiculo_delete'),
    path('movimentos/', MovimentoListView.as_view(), name='movimento_list'),
    path('movimento/novo/', MovimentoCreateView.as_view(), name='movimento_create'),
    path('movimento/editar/<uuid:pk>/', MovimentoUpdateView.as_view(), name='movimento_update'),
    path('movimento/excluir/<uuid:pk>/', MovimentoDeleteView.as_view(), name='movimento_delete'),
    path('caixa/baixar/', painel_pagamentos, name='painel_pagamentos'),
    path('dashboard/', dashboard, name='dashboard'),
]

from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.lista_lancamentos, name='lista_lancamentos'),
    path ('despesa/nova/', views.nova_despesa, name='nova_despesa'),
    path('receita/nova/', views.nova_receita, name='nova_receita'),
]

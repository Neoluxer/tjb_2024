from django.urls import path
from . import views

urlpatterns = [
    path('', views.u_c_f_private, name='contract_private'),
    path('result_contract/', views.result_contract, name='result_contract'),
]
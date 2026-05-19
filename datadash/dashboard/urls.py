from django.urls import path
from . import views

app_name = 'dashboard'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('upload/', views.upload, name='upload'),
    path('dados/', views.dados, name='dados'),
    path('limpar/', views.confirmar_limpeza, name='limpar'),
]

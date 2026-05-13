from django.urls import path
from . import views

app_name = 'gym'

urlpatterns = [
    path('', views.home, name='home'),
    path('miembros/', views.miembro_list, name='miembro_list'),
    path('miembros/nuevo/', views.miembro_create, name='miembro_create'),
    path('miembros/<int:pk>/eliminar/', views.miembro_delete, name='miembro_delete'),
]

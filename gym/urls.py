from django.urls import path
from . import views

app_name = 'gym'

urlpatterns = [
    path('', views.home, name='home'),
    path('miembros/', views.miembro_list, name='miembro_list'),
    path('miembros/nuevo/', views.miembro_create, name='miembro_create'),
    path('miembros/<int:pk>/editar/', views.miembro_update, name='miembro_update'),
    path('miembros/<int:pk>/eliminar/', views.miembro_delete, name='miembro_delete'),
    path('nutricion/', views.plan_nutricional_list, name='plan_nutricional_list'),
    path('nutricion/nuevo/', views.plan_nutricional_create, name='plan_nutricional_create'),
    path('mi-plan/', views.mi_plan, name='mi_plan'),
]

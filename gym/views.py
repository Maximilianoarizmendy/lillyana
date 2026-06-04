from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Miembro, PlanNutricional
from .forms import MiembroForm, PlanNutricionalForm

@login_required
def home(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'gym/partials/home.html')
    return render(request, 'gym/home.html')

@login_required
def miembro_list(request):
    miembros = Miembro.objects.all()
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'gym/partials/miembro_list.html', {'miembros': miembros})
    return render(request, 'gym/miembro_list.html', {'miembros': miembros})

@login_required
def miembro_create(request):
    if request.method == 'POST':
        form = MiembroForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Miembro creado exitosamente.")
            return redirect('gym:miembro_list')
        else:
            messages.error(request, "Error al crear el miembro. Revisa los datos.")
    else:
        form = MiembroForm()
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'gym/partials/miembro_form.html', {'form': form})
    return render(request, 'gym/miembro_form.html', {'form': form})

@login_required
def miembro_delete(request, pk):
    miembro = get_object_or_404(Miembro, pk=pk)
    if request.method == 'POST':
        miembro.delete()
        messages.success(request, "Miembro eliminado.")
    return redirect('gym:miembro_list')

@login_required
def plan_nutricional_list(request):
    planes = PlanNutricional.objects.all()
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'gym/partials/plan_nutricional_list.html', {'planes': planes})
    return render(request, 'gym/plan_nutricional_list.html', {'planes': planes})

@login_required
def plan_nutricional_create(request):
    if request.method == 'POST':
        form = PlanNutricionalForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Plan nutricional creado.")
            return redirect('gym:plan_nutricional_list')
        else:
            messages.error(request, "Error al crear el plan.")
    else:
        form = PlanNutricionalForm()
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'gym/partials/plan_nutricional_form.html', {'form': form})
    return render(request, 'gym/plan_nutricional_form.html', {'form': form})

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.models import User, Group
from .models import Miembro, PlanNutricional
from .forms import MiembroForm, PlanNutricionalForm, RegistroForm

def registro(request):
    if request.user.is_authenticated:
        return redirect('gym:home')
        
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data.get('nombre')
            apellido = form.cleaned_data.get('apellido')
            email = form.cleaned_data.get('email')
            telefono = form.cleaned_data.get('telefono')
            password = form.cleaned_data.get('password')
            
            # Crear cuenta de User
            user, created = User.objects.get_or_create(username=email, defaults={'email': email})
            if created:
                user.set_password(password)
                user.save()
                grupo, _ = Group.objects.get_or_create(name='Usuario')
                user.groups.add(grupo)
                
                # Crear Miembro
                Miembro.objects.create(
                    user=user,
                    nombre=nombre,
                    apellido=apellido,
                    email=email,
                    telefono=telefono
                )
                messages.success(request, "¡Tu cuenta ha sido creada con éxito! Ahora puedes iniciar sesión.")
                return redirect('login')
            else:
                messages.error(request, "Ya existe una cuenta con este correo electrónico.")
    else:
        form = RegistroForm()
    
    return render(request, 'registration/registro.html', {'form': form})

@login_required
def home(request):
    if request.user.groups.filter(name='Usuario').exists():
        return redirect('gym:mi_plan')
        
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
            miembro = form.save(commit=False)
            
            username = miembro.email
            password = miembro.telefono if miembro.telefono else "usuario123"
            user, created = User.objects.get_or_create(username=username, email=miembro.email)
            if created:
                user.set_password(password)
                user.save()
                grupo, _ = Group.objects.get_or_create(name='Usuario')
                user.groups.add(grupo)
            
            miembro.user = user
            miembro.save()
            
            messages.success(request, f"Miembro creado exitosamente. Clave de acceso: {password}")
            return redirect('gym:miembro_list')
        else:
            messages.error(request, "Error al crear el miembro. Revisa los datos.")
    else:
        form = MiembroForm()
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'gym/partials/miembro_form.html', {'form': form})
    return render(request, 'gym/miembro_form.html', {'form': form})

@login_required
def miembro_update(request, pk):
    miembro = get_object_or_404(Miembro, pk=pk)
    if request.method == 'POST':
        form = MiembroForm(request.POST, instance=miembro)
        if form.is_valid():
            form.save()
            messages.success(request, "Datos del cliente actualizados exitosamente.")
            return redirect('gym:miembro_list')
    else:
        form = MiembroForm(instance=miembro)
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'gym/partials/miembro_form.html', {'form': form, 'edit_mode': True})
    return render(request, 'gym/miembro_form.html', {'form': form, 'edit_mode': True})

@login_required
def miembro_delete(request, pk):
    miembro = get_object_or_404(Miembro, pk=pk)
    if request.method == 'POST':
        if miembro.user:
            miembro.user.delete()
        miembro.delete()
        messages.success(request, "Miembro y cuenta de usuario eliminados.")
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

@login_required
def mi_plan(request):
    plan = None
    try:
        if hasattr(request.user, 'miembro'):
            plan = request.user.miembro.plannutricional
    except Exception:
        pass
        
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'gym/partials/mi_plan.html', {'plan': plan})
    return render(request, 'gym/mi_plan.html', {'plan': plan})

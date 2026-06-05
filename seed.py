import os
import django
import random

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.contrib.auth.models import User, Group
from gym.models import Miembro, Clase, Membresia, PlanNutricional

def run():
    print("Iniciando sembrado de datos...")
    
    # Crear Usuarios Admin y Nutricionista
    admin_group, _ = Group.objects.get_or_create(name='Admin')
    nutri_group, _ = Group.objects.get_or_create(name='Nutricionista')
    
    if not User.objects.filter(username='admin').exists():
        admin = User.objects.create_superuser('admin', 'admin@example.com', 'admin123')
        admin.groups.add(admin_group)
        print("Admin user created")
        
    if not User.objects.filter(username='nutricionista').exists():
        nutri = User.objects.create_user('nutricionista', 'nutri@example.com', 'nutri123')
        nutri.groups.add(nutri_group)
        print("Nutricionista user created")

    # Limpiar datos
    PlanNutricional.objects.all().delete()
    Miembro.objects.all().delete()
    Clase.objects.all().delete()
    Membresia.objects.all().delete()

    # Membresías
    mem_basica = Membresia.objects.create(nombre="Básica", precio=50000, duracion_dias=30)
    mem_pro = Membresia.objects.create(nombre="Pro", precio=90000, duracion_dias=30)
    mem_premium = Membresia.objects.create(nombre="Premium", precio=150000, duracion_dias=30)
    membresias = [mem_basica, mem_pro, mem_premium]

    # Miembros
    nombres = ['Carlos', 'Andrés', 'María', 'Laura', 'Juan', 'Diego', 'Camila', 'Sofía']
    apellidos = ['Gómez', 'Pérez', 'Rodríguez', 'López', 'Martínez', 'Hernández']
    miembros = []
    
    for i in range(10):
        nombre = random.choice(nombres)
        apellido = random.choice(apellidos)
        miembro = Miembro.objects.create(
            nombre=nombre,
            apellido=apellido,
            email=f"{nombre.lower()}.{apellido.lower()}@example.com",
            telefono=f"300{random.randint(1000000, 9999999)}",
            membresia=random.choice(membresias)
        )
        miembros.append(miembro)
        print(f"Creado Miembro: {miembro.nombre} {miembro.apellido}")

    # Clases
    Clase.objects.create(nombre="Yoga", instructor="Marta", horario="Lunes 8:00 AM", capacidad_maxima=20)
    Clase.objects.create(nombre="Crossfit", instructor="Luis", horario="Martes 6:00 PM", capacidad_maxima=15)
    Clase.objects.create(nombre="Zumba", instructor="Diana", horario="Miércoles 7:00 PM", capacidad_maxima=25)
    
    # Planes Nutricionales
    for miembro in miembros[:5]: # Solo algunos miembros
        peso = random.uniform(50.0, 90.0)
        altura = random.randint(150, 190)
        PlanNutricional.objects.create(
            miembro=miembro,
            peso_kg=peso,
            altura_cm=altura,
            dieta_recomendada="Consumir alto contenido en proteínas, vegetales verdes, y evitar azúcares refinados. Hidratación: 2.5 L diarios."
        )
        print(f"Plan Nutricional creado para {miembro.nombre}")

    print("Sembrado completo.")

if __name__ == '__main__':
    run()

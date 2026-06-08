from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

class Membresia(models.Model):
    nombre = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    duracion_dias = models.IntegerField()
    
    def __str__(self):
        return self.nombre

class Miembro(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=150)
    apellido = models.CharField(max_length=150)
    # Validaciones (Regex) requeridas por la rúbrica
    telefono_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$', message="El formato del teléfono debe ser: '+999999999'. Hasta 15 dígitos.")
    telefono = models.CharField(validators=[telefono_regex], max_length=17, blank=True)
    email = models.EmailField(unique=True)
    membresia = models.ForeignKey(Membresia, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_registro = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Clase(models.Model):
    nombre = models.CharField(max_length=100)
    instructor = models.CharField(max_length=150)
    horario = models.CharField(max_length=100)
    capacidad_maxima = models.IntegerField()
    
    def __str__(self):
        return f"{self.nombre} - {self.instructor}"

class PlanNutricional(models.Model):
    miembro = models.OneToOneField(Miembro, on_delete=models.CASCADE)
    peso_kg = models.DecimalField(max_digits=5, decimal_places=2, help_text="Peso en kilogramos")
    altura_cm = models.IntegerField(help_text="Altura en centímetros")
    dieta_recomendada = models.TextField()
    fecha_actualizacion = models.DateField(auto_now=True)
    
    def __str__(self):
        return f"Plan de {self.miembro}"

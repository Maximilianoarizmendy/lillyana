from django import forms
from .models import Miembro, Clase, Membresia
from django.core.validators import RegexValidator

class MiembroForm(forms.ModelForm):
    # Ya incluimos regex en el modelo, pero podemos validarlo aquí también para mayor seguridad
    telefono = forms.CharField(
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="El formato del teléfono debe ser: '+999999999'. Hasta 15 dígitos.")],
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. +573001234567'})
    )
    class Meta:
        model = Miembro
        fields = ['nombre', 'apellido', 'telefono', 'email', 'membresia']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'membresia': forms.Select(attrs={'class': 'form-select'}),
        }

class ClaseForm(forms.ModelForm):
    class Meta:
        model = Clase
        fields = '__all__'
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'instructor': forms.TextInput(attrs={'class': 'form-control'}),
            'horario': forms.TextInput(attrs={'class': 'form-control'}),
            'capacidad_maxima': forms.NumberInput(attrs={'class': 'form-control'}),
        }

from .models import PlanNutricional

class PlanNutricionalForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:
            # Solo mostrar miembros que NO tienen plan
            self.fields['miembro'].queryset = Miembro.objects.filter(plannutricional__isnull=True)

    class Meta:
        model = PlanNutricional
        fields = '__all__'
        widgets = {
            'miembro': forms.Select(attrs={'class': 'form-select'}),
            'peso_kg': forms.NumberInput(attrs={'class': 'form-control'}),
            'altura_cm': forms.NumberInput(attrs={'class': 'form-control'}),
            'dieta_recomendada': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }

class RegistroForm(forms.Form):
    nombre = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Juan'}))
    apellido = forms.CharField(max_length=150, widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. Pérez'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'correo@ejemplo.com'}))
    telefono = forms.CharField(
        validators=[RegexValidator(regex=r'^\+?1?\d{9,15}$', message="El formato del teléfono debe ser: '+999999999'. Hasta 15 dígitos.")],
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ej. 3001234567'})
    )
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Contraseña segura'}))

from django import forms
from .models import Productos

class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields= '__all__'

class ProductoForm2(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['nombre', 'categoria','descripcion', 'idjuego', 'existencias', 'precio', 'activo'] 
        labels= {
            'nombre' : "NOMBRE",
            'idjuego' : "IDENTIFICADOR"
        }

        widgets={
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'categoria': forms.Select(attrs={'class': 'form-control'}),
            'descripcion': forms.TextInput(attrs={'class': 'form-control'}),
            'idjuego': forms.NumberInput(attrs={'class': 'form-control'}),
            'existencias': forms.NumberInput(attrs={'class': 'form-control'}),
            'precio': forms.NumberInput(attrs={'class': 'form-control'}),
            'activo': forms.CheckboxInput(attrs={'class': 'form-check-input', 'style': 'margin-left: 0;'})    
        }

from django.shortcuts import render, HttpResponse, redirect
from .models import Productos
from .forms import ProductoForm, ProductoForm2
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request,'catalogos.html')

class ProductosListar(ListView):
    model = Productos
    template_name = 'productos.html'
    context_object_name = 'productos'
    success_url = 'productos'

    login_url = 'login'  # URL de inicio de sesión
    redirect_field_name = 'next' 

class ProductosCrearView(CreateView):
    model = Productos
    template_name = 'crear_producto.html'
    context_object_name = 'productos'
    form_class = ProductoForm2
    success_url = 'productos'
    login_url = 'login'  # URL de inicio de sesión
    redirect_field_name = 'next' 

    def form_valid(self, form):
        messages.success(self.request, 'El objeto se ha Creado exitosamente.')
        return super().form_valid(form)

class ProductosEditarView(UpdateView):
    model = Productos
    template_name = 'crear_producto.html'
    form_class = ProductoForm
    success_url = reverse_lazy('productos')

    login_url = 'login'  # URL de inicio de sesión
    redirect_field_name = 'next'

    def form_valid(self, form):
        messages.success(self.request, 'El objeto se ha actualizado exitosamente.')
        return super().form_valid(form) 

class ProductosEliminarView(DeleteView):
    model = Productos
    template_name = 'eliminar_producto.html'
    success_url = reverse_lazy('productos')

    login_url = 'login'  # URL de inicio de sesión
    redirect_field_name = 'next'

    def delete(self, request, *args, **kwargs):
        messages.error(self.request, 'El objeto se ha eliminado exitosamente.')
        return super().delete(request, *args, **kwargs)
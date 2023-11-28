from django.urls import path
from . import views
from .views import ProductosListar, ProductosCrearView, ProductosEditarView, ProductosEliminarView

urlpatterns = [
    path('', views.home, name='home' ),
    path('productos/', ProductosListar.as_view(), name='productos' ),
    path('productosCrear', ProductosCrearView.as_view(), name= 'productosCrear'),
    path('productosEditar/<int:pk>/', ProductosEditarView.as_view(), name="productosEditar"),
    path('productosEliminar/<int:pk>/', ProductosEliminarView.as_view(), name='productosEliminar'),
] 
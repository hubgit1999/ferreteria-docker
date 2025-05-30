from django.urls import path
from . import views

urlpatterns = [
    # PRODUCTO
    path('productos/', views.listar_productos, name='listar_productos'),
    path('productos/crear/', views.crear_producto, name='crear_productos'),
    path('productos/editar/<int:id>/', views.editar_producto, name='editar_productos'),
    path('productos/eliminar/<int:id>/', views.eliminar_producto, name='eliminar_productos'),

    # PROVEEDOR
    path('proveedores/', views.listar_proveedores, name='listar_proveedores'),
    path('proveedores/crear/', views.crear_proveedor, name='crear_proveedores'),
    path('proveedores/editar/<int:id>/', views.editar_proveedor, name='editar_proveedores'),
    path('proveedores/eliminar/<int:id>/', views.eliminar_proveedor, name='eliminar_proveedores'),

    # FACTURA
    path('facturas/', views.listar_facturas, name='listar_facturas'),
    path('facturas/crear/', views.crear_factura, name='crear_facturas'),
    path('facturas/editar/<int:id>/', views.editar_factura, name='editar_facturas'),
    path('facturas/eliminar/<int:id>/', views.eliminar_factura, name='eliminar_facturas'),
]

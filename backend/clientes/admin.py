
from django.contrib import admin
from .models import Cliente, Categoria, Proveedor, Producto, Factura, DetalleFactura

admin.site.register(Cliente)
admin.site.register(Categoria)
admin.site.register(Proveedor)
admin.site.register(Producto)
admin.site.register(Factura)
admin.site.register(DetalleFactura)

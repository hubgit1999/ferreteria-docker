from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto, Proveedor, Factura
from .forms import ProductoForm, ProveedorForm, FacturaForm

# PRODUCTO
def listar_productos(request):
    productos = Producto.objects.all()
    return render(request, 'clientes/listar.html', {'items': productos, 'titulo': 'Productos'})

def crear_producto(request):
    form = ProductoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_productos')
    return render(request, 'clientes/formulario.html', {'form': form, 'titulo': 'Crear Producto'})

def editar_producto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    form = ProductoForm(request.POST or None, instance=producto)
    if form.is_valid():
        form.save()
        return redirect('listar_productos')
    return render(request, 'clientes/formulario.html', {'form': form, 'titulo': 'Editar Producto'})

def eliminar_producto(request, id):
    producto = get_object_or_404(Producto, pk=id)
    producto.delete()
    return redirect('listar_productos')

# PROVEEDOR
def listar_proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'clientes/listar.html', {'items': proveedores, 'titulo': 'Proveedores'})

def crear_proveedor(request):
    form = ProveedorForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_proveedores')
    return render(request, 'clientes/formulario.html', {'form': form, 'titulo': 'Crear Proveedor'})

def editar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, pk=id)
    form = ProveedorForm(request.POST or None, instance=proveedor)
    if form.is_valid():
        form.save()
        return redirect('listar_proveedores')
    return render(request, 'clientes/formulario.html', {'form': form, 'titulo': 'Editar Proveedor'})

def eliminar_proveedor(request, id):
    proveedor = get_object_or_404(Proveedor, pk=id)
    proveedor.delete()
    return redirect('listar_proveedores')

# FACTURA
def listar_facturas(request):
    facturas = Factura.objects.select_related('cliente').all()
    return render(request, 'clientes/listar.html', {'facturas': facturas, 'titulo': 'Facturas'})

def crear_factura(request):
    form = FacturaForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('listar_facturas')
    return render(request, 'clientes/formulario.html', {'form': form, 'titulo': 'Crear Factura'})

def editar_factura(request, id):
    factura = get_object_or_404(Factura, pk=id)
    form = FacturaForm(request.POST or None, instance=factura)
    if form.is_valid():
        form.save()
        return redirect('listar_facturas')
    return render(request, 'clientes/formulario.html', {'form': form, 'titulo': 'Editar Factura'})

def eliminar_factura(request, id):
    factura = get_object_or_404(Factura, pk=id)
    factura.delete()
    return redirect('listar_facturas')

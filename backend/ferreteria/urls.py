from django.contrib import admin
from django.urls import path, include
from django.http import JsonResponse

urlpatterns = [
    path('', lambda request: JsonResponse({'mensaje': 'API de Ferretería activa'})),
    path('admin/', admin.site.urls),
    path('clientes/', include('clientes.urls')),
]

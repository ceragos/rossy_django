from django.contrib import admin

# Register your models here.
from aplicacion.bodega.models import Insumo, InventarioInsumo, Producto, InventarioProducto

admin.site.register(Insumo)
admin.site.register(InventarioInsumo)
admin.site.register(Producto)
admin.site.register(InventarioProducto)
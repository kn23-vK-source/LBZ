from django.contrib import admin

from .models import Supplier, Material, Delivery

admin.site.register(Supplier)
admin.site.register(Material)
admin.site.register(Delivery)

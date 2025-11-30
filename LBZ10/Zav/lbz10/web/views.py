from django.shortcuts import render
from django.http import HttpResponse
from DB_addition.models import Material
from DB_addition.models import Supplier
from DB_addition.models import Delivery

def index(request):
    return render(request, "index.html")

def supplier(request):
    suppliers = Supplier.objects.all()
    return render(request, 'supplier.html', {'suppliers': suppliers})

def material(request):
    materials = Material.objects.all()
    return render(request, 'material.html', {'materials': materials})

def delivery(request):
    deliveries = Delivery.objects.all()
    return render(request, 'delivery.html', {'deliveries': deliveries})

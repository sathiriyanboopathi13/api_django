from django.shortcuts import render
from django.http import JsonResponse
from .models import Inventory
# Create your views here.

def GetItems(request):
    items = Inventory.objects.all()
    data = {'items' : list(items.values())}
    return JsonResponse(data)

def Item(request,pk):
    item = Inventory.objects.get(pk=pk)
    data = {
        'name':item.name,
        'category':item.category,
        'quantity':item.quantity,
        'price':item.price,
    }
    return JsonResponse(data)



from django.contrib import admin
from django.urls import path
from .views import GetItems,Item
urlpatterns = [
    path('allitems',GetItems,name='get_items'),
    path('item/<int:pk>',Item,name='item'),
]
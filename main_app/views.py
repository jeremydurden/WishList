from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView
from .models import Item

# Create your views here.
class WishList(ListView):
    model = Item

class CreateWish(CreateView):
    model = Item
    fields = '__all__'

class DeleteWish(DeleteView):
    model = Item
    success_url = "/"
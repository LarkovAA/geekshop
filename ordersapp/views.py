from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView


class OrderList(ListView):
    pass

class OrderCreate(CreateView):
    pass

class OrderUpdate(UpdateView):
    pass

class OrderDelete(DeleteView):
    pass

class OrderDetail(DetailView):
    pass

def order_forming_complete(request, pk):
    pass

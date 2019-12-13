from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from product.models import Product
from product.forms import ProductForm


class ProductList(ListView):
    template_name = 'product/product_list.html'
    model = Product
    context_object_name = 'product_list'


class ProductAdd(CreateView):
    template_name = 'product/product_add.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product_list')


class ProductEdit(UpdateView):
    template_name = 'product/product_edit.html'
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('product_list')


class ProductDel(DeleteView):
    template_name = 'product/product_del.html'
    model = Product
    success_url = reverse_lazy('product_list')
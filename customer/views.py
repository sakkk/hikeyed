from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from customer.forms import CustomerForm
from customer.models import Customer


class CustomerList(ListView):
    template_name = 'customer/customer_list.html'
    model = Customer
    context_object_name = 'customer_list'


class CustomerAdd(CreateView):
    template_name = 'customer/customer_add.html'
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('customer_list')


class CustomerEdit(UpdateView):
    template_name = 'customer/customer_edit.html'
    model = Customer
    form_class = CustomerForm
    success_url = reverse_lazy('customer_list')


class CustomerDel(DeleteView):
    template_name = 'customer/customer_del.html'
    model = Customer
    success_url = reverse_lazy('customer_list')

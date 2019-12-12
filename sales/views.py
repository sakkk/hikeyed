from django.db.models import Sum
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from sales.forms import SalesDetailForm
from sales.models import SalesDetail


class SalesDetailList(ListView):
    template_name = 'sales/detail_list.html'
    model = SalesDetail
    context_object_name = 'detail_list'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total'] = SalesDetail.objects.all().aggregate(Sum('sub_total'))
        return context


class SalesDetailAdd(CreateView):
    template_name = 'sales/detail_add.html'
    model = SalesDetail
    form_class = SalesDetailForm
    success_url = reverse_lazy('detail_list')


class SalesDetailEdit(UpdateView):
    template_name = 'sales/detail_edit.html'
    model = SalesDetail
    form_class = SalesDetailForm
    success_url = reverse_lazy('detail_list')


class SalesDetailDel(DeleteView):
    template_name = 'sales/detail_del.html'
    model = SalesDetail
    success_url = reverse_lazy('detail_list')
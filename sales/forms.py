from django import forms

from sales.models import SalesDetail


class SalesDetailForm(forms.ModelForm):
    class Meta:
        model = SalesDetail
        fields = ('sales', 'product', 'price', 'amount', 'sub_total')


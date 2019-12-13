from django import forms

from customer.models import Customer


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ('name', 'tel', 'email', 'postal_code', 'address')

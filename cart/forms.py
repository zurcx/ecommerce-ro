from tkinter import Widget

from django import forms
from django.forms import HiddenInput

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]


class CartAddProductForm(forms.Form):
    quantity = forms.TypedChoiceField(
        label="Quantidade", choices=PRODUCT_QUANTITY_CHOICES, coerce=int
    )

    override = forms.BooleanField(
        initial=False, required=False, widget=HiddenInput
    )

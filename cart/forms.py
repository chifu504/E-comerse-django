from django import forms

PRODUCT_QUANTITY_CHOICES = [(i, str(i)) for i in range(1, 21)]
TALLA_CHOICES = [ ('S', 'S'),('M', 'M'),('L', 'L'),]


class CartAddProductForm(forms.Form):
    talla = forms.ChoiceField(choices=TALLA_CHOICES)
    quantity = forms.TypedChoiceField(choices=PRODUCT_QUANTITY_CHOICES,coerce=int)
    override = forms.BooleanField(required=False,initial=False,widget=forms.HiddenInput)
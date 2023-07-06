from django import forms

choice_list=[(i, str(i)) for i in range(1,21)]

class CartAddProductForm(forms.Form):
    quantity=forms.TypedChoiceField(choices=choice_list, coerce=int, label='Количество')
    update=forms.BooleanField(required=False, widget=forms.HiddenInput, initial=False)

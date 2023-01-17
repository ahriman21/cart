from django import forms
# 

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(widget=forms.NumberInput(),initial=1,label='تعداد',min_value=1,max_value=10)
    product_id = forms.IntegerField(widget=forms.HiddenInput())

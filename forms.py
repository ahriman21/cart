from django import forms
# 

class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(widget=forms.NumberInput(),initial=1,label='تعداد',min_value=1,max_value=10)
    product_id = forms.IntegerField(widget=forms.HiddenInput())


# use in product-detail-view.html :

  <form action="{% url 'cart:add' %}" method="post">
    {% csrf_token %}
    {{add_to_cart_form}}
     <div >
        <input type="submit" value="افزودن به سبدخرید" class="btn-single" >
    </div>
 </form>

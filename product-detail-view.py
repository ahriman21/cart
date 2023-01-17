  class GetProductView(View):
    template_name = 'product/detail.html'
    form_class = AddToCartForm
    
    def get(self, request, slug, id):
        product = get_object_or_404(Product, slug=slug, id=id ,is_active=True)
        add_to_cart_form = self.form_class(initial={'product_id':product.id}) # <------ *
        product_tags = product.tag.split(' ')
        context = {'product':product,
                'product_tags':product_tags,
                'add_to_cart_form':add_to_cart_form} # <------- *
        return render(request,self.template_name,context)

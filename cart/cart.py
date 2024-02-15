class Cart:
    def __init__(self, request):
        self.session = request.session
        cart = self.session.get('session_key')
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}

        self.cart = cart
    

    def add(self, product):
        product_id = str(product_id)

        if product_id in self.cart:
            pass
        else:
            self.cart[product_id] = {'price':str(product.price)}
        
        self.session.modified = True

    def __len__(self):
        return len(self.cart)

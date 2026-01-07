class Cart:
    def __init__(self, request):
        self.session = request.session
        self.cart = self.session.get('cart', {})
        self.session['cart'] = self.cart

    def add(self, product_id, product_name, price, quantity=1):
        product_id = str(product_id)
        if product_id not in self.cart:
            self.cart[product_id] = {
                'name': product_name,
                'price': price,
                'quantity': 0
            }
        self.cart[product_id]['quantity'] += quantity
        self.session.modified = True

    def remove(self, product_id):
        product_id = str(product_id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.session.modified = True

    def clear(self):
        self.session['cart'] = {}
        self.session.modified = True

    def get_items(self):
        return self.cart.values()

    def get_total_price(self):
        return sum(
            item['price'] * item['quantity']
            for item in self.cart.values()
        )

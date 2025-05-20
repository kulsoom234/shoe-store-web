from shoe import shoe
from order import Order
from payment import Payment

class ShoeStore:
    def __init__(self):
        self.shoes = []
        self.orders = []
        self.payments = []

    def add_shoe(self , shoe):
        self.shoes.append(shoe)

    def remove_shoe(self, id):
        for shoe in self.shoes:
            if shoe.id == id:
                self.shoes.remove(shoe)
                return
            print("Shoe not found")

        def get_shoes(self):
            return self.shoes
        
        def search_shoes(self, name):
            for shoe in self.shoes:
                if shoe.name.lower() == name.lower():
                    return shoe
                return None
            
    def place_order(self, customer_name, shoe_id, quantity):
        shoe = next((s for s in self.shoes if s.id == shoe_id), None)
        if shoe:
            total_price = shoe.price * quantity
            order = order(len(self.orders) + 1, customer_name, shoe_id, quantity, total_price)
            self.orders.append(order)
            return Order
        else:
            return None
        
    def make_payment(self, order_id, payment_method, amount):
        order = next((o for o in self.orders if o.id == order_id), None)
        if order:
            Payment = Payment(order_id, payment_method, amount)
            self.payments.append(Payment)
            return Payment
        else:
            return None 
        
        
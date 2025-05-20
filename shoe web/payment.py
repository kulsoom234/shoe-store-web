class Payment:
    def __init__(self, order_id, payment_method, amount):
        self.order_id = order_id
        self.payment_method = payment_method
        self.amount = amount

    def __str__(self):
        return f"Order ID: {self.order_id}, Payment Method: {self.payment_method}, Amount: {self.amount}"
    

        
class Order:
    def __init__(self, id, customer_name, shoe_id, quantity, total_price):
        self.id = id
        self.customer_name = customer_name
        self.shoe_id = shoe_id
        self.quantity = quantity
        self.total_price = total_price

    def __str__(self):
        return f"Order ID: {self.id}, Customer Name: {self.customer_name}, Shoe ID: {self.shoe_id}, Quantity: {self.quantity}, Total Price: {self.total_price}"
        
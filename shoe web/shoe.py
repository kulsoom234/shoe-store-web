class shoe:
    def __init__(self , id , name , price, quantity, image_url):
        self.id = id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.image_url = image_url


    def __str__(self):
        return f"Shoe ID: {self.id}, Name: {self.name}, Price: {self.price}, Quantity: {self.quantity}"
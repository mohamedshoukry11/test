class Product:
    def __init__(self, id, name, category, price):
        self.id = id
        self.name = name
        self.category = category
        self.price = price

class Cart:
    def __init__(self, id, user_id):
        self.id = id
        self.user_id = user_id
        self.items = []

    def add_product(self, product, quantity):
        self.items.append((product, quantity))

    def get_total(self):
        total = 0
        for product, quantity in self.items:
            total += product.price * quantity
        return total

class User:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.cart = Cart(id, id) 

product1 = Product(1, "t_shirt", "snikker", 150)
product2 = Product(2, "shirt", "perfume", 50)

user1 = User(1,"mohamed")

user1.cart.add_product(product1, 2)
user1.cart.add_product(product2, 3)


print(f"full_inside_basket {user1.name}: {user1.cart.get_total()}")
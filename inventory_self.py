class Customer:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.purchases = []

    def purchase(self, inventory, product):
        inventory_dict = inventory.inventory
        if product in inventory_dict:
            if inventory_dict[product] > 0:
                self.purchases.append(product)
            else:
                print("Sorry! We are out of stock!")
        else:
            print("Sorry! We don't carry that product!")


    def print_purchases(self):
        print("""The customer has purchased:
        """)
        for item in self.purchases:
            print(item.name)

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_product(self, product, quantity):
        if product not in self.inventory:
            self.inventory[product] = quantity
        else:
            self.inventory[product] += quantity


    def print_inventory(self):
        for key, value in self.inventory.items():
            print(key.name + ":" + str(value))
        print()


customer = Customer ('Joe', 'joe@gmail.com')
print(customer.name)
print(customer.email)

customer.print_purchases()
vibrating_bunny = Product('Bunny', 99)
print(vibrating_bunny.name)
print(vibrating_bunny.price)

dickleberry = Product('Dickleberry', 299)
print(dickleberry.name)
print(dickleberry.price)


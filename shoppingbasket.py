from item import Item


class ShoppingBasket:
    # Constructor
    def __init__(self):
        self.items : dict = {}

    # A method to add an item to the shopping basket
    def addItem(self, item: Item, quantity=1):
        if quantity <= item.stock:
            self.items[item] = quantity
            item.stock -= quantity

        else:
            raise ValueError

    # A method to remove an item from the shopping basket (or reduce its quantity)
    def remove_item(self, item: Item, quantity=0):
        try:
            item.stock += self.items[item].value()
            self.items.pop(item)
        except:
            raise KeyError

    # A method to update the quantity of an item from the shopping basket
    def updateItem(self, item: Item, quantity: int):
        try:
            item.stock += self.items[1]
            self.items[item] = quantity
            item.stock -= quantity
        except:
            raise KeyError

    # A method to view/list the content of the basket.
    def view(self):
        for key, value in self.items.items():
            print(f'{key}: {value}')

    # A method to calculate the total cost of the basket.
    def get_total_cost(self):
        return sum(item.price * quantity for item,quantity in self.items.items())

    # A method to empty the content of the basket
    def reset(self):
        for key,value in self.items.items():
            key.stock += value
        self.items: dict = {}

    # A method to return whether the basket is empty or not:
    def is_empty(self):
        return True if len(self.items) == 0 else False

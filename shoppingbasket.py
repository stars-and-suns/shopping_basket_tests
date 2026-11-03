from item import Item


class ShoppingBasket:
    # Constructor
    def __init__(self):
        raise NotImplementedError

    # A method to add an item to the shopping basket
    def addItem(self, item: Item, quantity=1):
        raise NotImplementedError

    # A method to remove an item from the shopping basket (or reduce its quantity)
    def remove_item(self, item: Item, quantity=0):
        raise NotImplementedError

    # A method to update the quantity of an item from the shopping basket
    def updateItem(self, item: Item, quantity: int):
        raise NotImplementedError

    # A method to view/list the content of the basket.
    def view(self):
        raise NotImplementedError

        # A method to calculate the total cost of the basket.
    def get_total_cost(self):
        raise NotImplementedError

    # A method to empty the content of the basket
    def reset(self):
        raise NotImplementedError

    # A method to return whether the basket is empty or not:
    def is_empty(self):
        raise NotImplementedError

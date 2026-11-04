class Item:
  # Constructor
  def __init__(self,name,description,price,stock=10):
    self.name = name
    self.description = description
    self.price = price
    self.stock = stock

  def __repr__(self):
    return f'{self.name} - {self.description} - {self.price} - {self.stock}'


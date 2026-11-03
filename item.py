class Item:
  # Constructor
  def __init__(self,name,description,price):
    self.name = name
    self.description = description
    self.price = price

  def __repr__(self):
    return f'{self.name} - {self.description} - {self.price}'


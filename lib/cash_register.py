#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount = 0) -> None:
    self.discount = discount
    self.total = 0
    self.items = []

  def add_item(self, title, price, quantity = 1):
    self.total += (price * quantity)
    for i in range(quantity):
      self.items.append(title)

    self.last_transaction = {
      'title': title,
      'price':price,
      'quantity': quantity
    }

  def apply_discount(self):
    self.total = self.total - ((self.total * 20) / 100)
    if self.discount > 0:
      print(f'After the discount, the total comes to ${int(self.total)}.')
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):
    for i in range(self.last_transaction['quantity']):
      self.total -= self.last_transaction['price']
      self.items.pop()

  

  


  



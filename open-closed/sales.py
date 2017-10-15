from math import pi
from abc import ABCMeta, abstractproperty

# Instead of updating a single class Client, each type of client has a class and a method to get the total with the discount percentage. 
# If there's a new type of client, we will not modify the current code but create a new class to extend the functionality
class Client(object):
	__metaclass__ = ABCMeta

	def __init__(self, subtotal):
		self.subtotal = subtotal
		self.total =  0

	@abstractproperty
	def total_with_discount(self):
		pass

class SilverClient(Client):
	@property
	def total_with_discount(self):
		self.total =  0.90 * self.subtotal
		return self.total

class GoldClient(Client):
	@property
	def total_with_discount(self):
		self.total = 0.70 * self.subtotal
		return self.total

class Calculator(object):
	def __init__(self, clients):
		self.clients = clients

	@property 
	def total_sales(self):
		total = 0.0
		for client in self.clients:
			total += client.total_with_discount
		return total

class main(object):
	clients = [SilverClient(500), GoldClient(1500)]
	calculator = Calculator(clients)

	print "The total sales in the day is: ", calculator.total_sales


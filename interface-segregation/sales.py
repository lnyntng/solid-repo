from math import pi, floor
from abc import ABCMeta, abstractproperty

# Clients may get a receipt. However, only gold clients can accumulate points for their purcharse. Instead of 
# adding both methods in Client, they are in interfaces. Only gold clients inherits from the AccumulablePoints
# interface.

class Receiptable(object):
	__metaclass__ = ABCMeta

	@abstractproperty
	def receipt(self):
		pass

class AccumulablePoints(object):
	__metaclass__ = ABCMeta

	@abstractproperty
	def points(self):
		pass

class Client(Receiptable):
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

	@property
	def receipt(self):
		return "The total is ", self.total_with_discount, ". Thank you for your purcharse!"

class GoldClient(Client, AccumulablePoints):
	@property
	def total_with_discount(self):
		return 0.70 * self.subtotal

	@property
	def points(self):
		return floor(self.total_with_discount / 20)

	@property
	def receipt(self):
		return "The total is ", self.total_with_discount, ". You have accumulated ", self.points, "points. See you soon!"

class CashRegister(object):
	def __init__(self, clients):
		self.clients = clients

	@property 
	def total_sales(self):
		total = 0.0
		for client in self.clients:
			total += client.total_with_discount
		return total

class main(object):
	client1 = SilverClient(500)
	client2 = GoldClient(1500)

	clients = [client1, client2]

	cashRegister = CashRegister(clients)

	print client1.receipt
	print client2.receipt

	print "The total sales in the day is: ", cashRegister.total_sales


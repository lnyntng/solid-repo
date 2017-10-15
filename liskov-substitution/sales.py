from math import pi
from abc import ABCMeta, abstractproperty

class Client(object):
	__metaclass__ = ABCMeta

	def __init__(self, subtotal):
		self.subtotal = subtotal

	@abstractproperty
	def total_with_discount(self):
		pass

class SilverClient(Client):
	@property
	def total_with_discount(self):
		return 0.90 * self.subtotal

class GoldClient(Client):
	@property
	def total_with_discount(self):
		return 0.70 * self.subtotal

# An enquiry is someone who is just doing a quote or is checking prices. This is not yet a client and should not be
# able to be included in the total sales. Enquiry should not be a child of Client because it is not seamlessly replaceable 
class Enquiry(object):
	def __init__(self, subtotal):
		self.subtotal = subtotal

	@property
	def total_with_discount(self, discount):
		return (1 - discount) * self.subtotal

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
	clients = [SilverClient(500), GoldClient(1500)]
	cashRegister = CashRegister(clients)

	print "The total sales in the day is: ", cashRegister.total_sales


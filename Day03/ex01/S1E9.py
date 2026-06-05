from abc import ABC, abstractmethod

class Character(ABC):
	"""Abstract method creation"""
	@abstractmethod
	def __init__(self, first_name, is_alive=True):
		''' Init method using mandatory first_name and optional is_alive'''
		self.first_name = first_name
		self.is_alive = is_alive
	def die(self):
		''' abstract dying method'''
		self.is_alive = False
		pass
	


class Stark(Character):
	"""Class heriting from Character method"""
	def __init__(self, first_name, is_alive = True):
		''' Initi of Stark class using mandatory first_name and optionnal is_alive set to True by default'''
		self.first_name = first_name
		self.is_alive = is_alive

	def die(self):
		''' Die function which change is_alive of character to False'''
		self.is_alive = False
from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
	''' King classe creation '''

	def __init__(self, first_name, is_alive = True):
		''' Init king object using super to go into next init in MRO '''
		super().__init__(first_name, is_alive)

	def set_eyes(self, colors):
		''' set object eyes variable colors ''' 
		self.eyes = colors
	
	def set_hairs(self, colors):
		''' set object hair variable colors ''' 
		self.hairs = colors
	
	def get_eyes(self):
		''' return object eyes variable colors ''' 
		return self.eyes

	def get_hairs(self):
		''' return object eyes variable colors ''' 
		return self.hairs
class NLUModel():
	
	def __init__( self, rasa_nlu_data = [] ):
		self.rasa_nlu_data = rasa_nlu_data
	
	def __del__(self):
		self.__class__.__name__
		#class_name = self.__class__.__name__
		#print (class_name, "destroyed")



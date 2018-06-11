class NLUCommonExample():
	
	def __init__( self, text = '', intent = '', entities = []):
		self.text = text
		self.intent  = intent
		self.entities = entities

	def __del__(self):
		self.__class__.__name__
		#class_name = self.__class__.__name__
		#print (class_name, "destroyed")
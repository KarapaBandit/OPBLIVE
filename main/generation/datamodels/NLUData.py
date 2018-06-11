class NLUData():
	
	def __init__( self, common_examples = [], regex_features = [], entity_synonyms = []):
		self.common_examples = common_examples
		self.regex_features  = regex_features
		self.entity_synonyms = entity_synonyms

	def __del__(self):
		self.__class__.__name__
		#class_name = self.__class__.__name__
		#print (class_name, "destroyed")



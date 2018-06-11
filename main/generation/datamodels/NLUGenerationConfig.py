import json

class NLUGenerationConfig():
	
	def __init__( self, data_file ='',stop_words_file='' ,utterance_file ='',entities_file="" ):
		self.data_file = data_file
		self.utterance_file = utterance_file
		self.intents_file = entities_file

	def loadconfigurations(self, objNLUConfig):

		self.data_file = objNLUConfig["data_file"]
		self.stop_words_file = objNLUConfig["stop_words_file"]
		self.utterance_file = objNLUConfig["utterance_file"]
		self.intents_file = objNLUConfig["intents_file"]

	def __del__(self):
		self.__class__.__name__
		#class_name = self.__class__.__name__
		#print (class_name, "destroyed")


		
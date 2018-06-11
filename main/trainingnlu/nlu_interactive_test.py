from rasa_nlu import config
from rasa_nlu.model import Metadata, Interpreter
import json
import random



def run_nlu(configs,inputvalue,responsermapper,interpreter,verbose):
	result = interpreter.parse(inputvalue)
	intent = result["intent"]["name"]
	confidence = result["intent"]["confidence"]
	replyList = responsermapper[intent]
	length = len(replyList)
	responseIndex = random.randint(0,length-1) if length>1 else 0

	returnValue = "\t\t\t\t\t" +str(replyList[responseIndex]) 
	returnValue = returnValue + "\n\t\t\t\t\t[" + str(confidence) + "]"
	returnValue = returnValue + "\n\t\t\t\t\t[" + str(intent) + "]" 

	if verbose:
		for key in result:
			returnValue = "\n" + key + " :: " + json.dumps(result[key])
	
	return returnValue


def main():
	configs = config.load('./config/config_spacy.yml')
	interpreter = Interpreter.load(configs["path"]+"/default/"+ configs["model_name"]+'/')
	
	with open(configs["responseMatrix"],encoding="UTF-8") as fd: 
		responseMapper = json.loads(fd.read())

	welcomeMessage = "Welcome to testing interface for you NLU system,\nplease start typing to test..\n" + "To leave the testing state type 'exit' in terminal"
	print(welcomeMessage+"\n")

	while (True):
		response = input("YOU=>")
		if "exit" in response: break
		elif(response):
			message = run_nlu(configs,response,responseMapper,interpreter,False)
			print(message)
		

if __name__ == '__main__':
	main()
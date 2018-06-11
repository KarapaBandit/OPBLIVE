from rasa_nlu.training_data import load_data
from rasa_nlu import config
from rasa_nlu.model import Trainer
from rasa_nlu.model import Metadata, Interpreter
import json

def train_nlu(configs):
	training_data = load_data(configs["data"])
	trainer = Trainer(configs)
	trainer.train(training_data)
	model_directory = trainer.persist(configs["path"], fixed_model_name = configs["model_name"])
	print('Model have been created at ' + model_directory)

def main():
	configs = config.load('./config/config_spacy.yml')
	train_nlu(configs)

if __name__ == '__main__':
	main()
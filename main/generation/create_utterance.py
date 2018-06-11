import pandas as pd
import jsonpickle
import re
import string
from rasa_nlu import config
from datamodels.NLUModel import NLUModel
from datamodels.NLUData import NLUData
from datamodels.NLUCommonExample import NLUCommonExample
from datamodels.NLUGenerationConfig import NLUGenerationConfig

def removeStopWords(sentence, stopwords):
    if(stopwords):
        listOfString = [re.sub('^[{0}]+|[{0}]+$'.format(string.punctuation), '', w) for w in sentence.split() if w not in stopwords]
        return " ".join(listOfString)

    return sentence

def writeJsonToFile(path,model):
    with open(path, 'w', encoding="UTF-8") as f:
        f.write(jsonpickle.encode(model,unpicklable=False))

def populateUtterances(data_file,modelWrapper,stopWords):
    datamodel = NLUData()
    modelWrapper.rasa_nlu_data = datamodel

    # use pd.read_csv to load t,he tsv_file
    df = pd.read_csv(data_file,sep="\t")
    dictQNA = df.to_dict()
    indexLen = len(dictQNA["Question"])-1
    insertIndexBuffer = 0
      
    for i in range(0,indexLen):
         sentence = removeStopWords(dictQNA["Question"][i],stopWords)
         if sentence.strip():
            item =  NLUCommonExample(removeStopWords(dictQNA["Question"][i],stopWords), dictQNA["Answer"][i], [])
            modelWrapper.rasa_nlu_data.common_examples.insert(insertIndexBuffer+i,item)
         
    return dictQNA
  
def fetchIntentsAsDictionary(dictQNA):
    entities = sorted(set(dictQNA["Answer"].values()))
    return {
        "count":len(entities),
        "entities": entities
        }

def readStopWords(path):
    all_words=[]
    with open(path, 'r', encoding="UTF-8") as input:
        all_words = [line for line in input.read().splitlines()]
        return set(all_words)

def createUtterancesAndIntents(configs):
    modelWrapper = NLUModel()
    #stopWords = readStopWords(configs.stop_words_file)
    #disabled stop word for NLU are break linguistic analysis
    dictQNA = populateUtterances(configs.data_file, modelWrapper,None)
    writeJsonToFile(configs.utterance_file, modelWrapper)
    writeJsonToFile(configs.intents_file,fetchIntentsAsDictionary(dictQNA))
   

def main():
    configs = NLUGenerationConfig()
    configs.loadconfigurations(config.load("./config/generation_config.yaml"))
    createUtterancesAndIntents(configs)


if __name__ == '__main__':
	main()
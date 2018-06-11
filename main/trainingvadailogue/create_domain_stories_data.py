import pandas as pd
import jsonpickle
import re
import string
from io import StringIO
from rasa_nlu import config

def writeToFile(path,modelString):
    with open(path, 'w', encoding="UTF-8") as f:
        f.write(modelString)

def getDictionaryForQuestionsAndAnswers(data_file):
    # use pd.read_csv to load the tsv_file
    df = pd.read_csv(data_file,sep="\t")
    dictQNA = df.to_dict()
    return dictQNA

def writeTemplates(intents, responses_file, file_str):
    with open(responses_file, 'r') as f:
        utterances = jsonpickle.loads(f.read())
    for  intent in intents:
        file_str.write("\n utter_"+ intent+":")
        for  utter in utterances[intent]:
            file_str.write('\n  - "'+ utter+'"')
        
def createDomainForSmallTalk(dictQNA,domain_file,responses_file):
     file_str = StringIO()
     file_str.write("#slots: null")
     file_str.write("\nintents:")
    
     intents = sorted(set(dictQNA["Answer"].values()))
     for intent in intents:
        file_str.write("\n - "+ intent)
     
     file_str.write("\n#entities: null")
     file_str.write("\ntemplates:")
     writeTemplates(intents,responses_file,file_str)

     file_str.write("\nactions:")
     for intent in intents:
        file_str.write("\n - utter_"+ intent)

     writeToFile(domain_file,file_str.getvalue())

def createStories(dictQNA, story_file):
    intents = sorted(set(dictQNA["Answer"].values()))
    file_str = StringIO()
    
    for idx, intent in enumerate(intents):
        file_str.write("## story " + str(idx) +"\n" 
        + "*"+intent+"\n"+"\t"+"- utter_"+intent+"\n\n")

    writeToFile(story_file,file_str.getvalue())

def createDomainAndStories(configs):
    dictQNA = getDictionaryForQuestionsAndAnswers(configs["data_file"])
    createStories(dictQNA, configs["stories_file"])
    createDomainForSmallTalk(dictQNA, configs["domain_file"], configs["responses_file"])
    
def main():
    configs = config.load("./config/training_va_config.yaml")
    createDomainAndStories(configs)

if __name__ == '__main__':
	main()
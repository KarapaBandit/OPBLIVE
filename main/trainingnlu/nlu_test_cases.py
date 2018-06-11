import pandas as pd
from rasa_nlu import config
from rasa_nlu.model import Metadata, Interpreter
import json
import jsonpickle

def writeToFile(path,model):
    with open(path, 'w', encoding="UTF-8") as f:
        f.write(json.dumps(model,indent=4))

def processUtterance(configs,interpreter):
    # use pd.read_csv to load t,he tsv_file
    df = pd.read_csv(configs["tsvfile"],sep="\t")
    dictQNA = df.to_dict()
    indexLen = len(dictQNA["Question"])-1
    results={
        "test_runs":len(dictQNA["Question"]),
        "passed":0,
        "failed":0,
        "coverage":"0%",
        "failedData":[],
        "passedData":[]
    }
    faileCounter=0
    passedCounter=0

    for i in range(0,indexLen):
        expectedResult=dictQNA["Answer"][i]
        text = dictQNA["Question"][i]
        intent = interpreter.parse(dictQNA["Question"][i])
        actualResult = intent["intent"]["name"]
        actualConfidence = intent["intent"]["confidence"]
        valueInserted = {
              "text":text,
              "expected": expectedResult,
              "actual"  : actualResult,
              "confidence":actualConfidence
            }

        if(expectedResult.strip()==actualResult.strip()):
            results["passedData"].insert(i,valueInserted)
            passedCounter+=1
        else:
            results["failedData"].insert(i,valueInserted)
            faileCounter+=1
        
        
   
    results["passed"]   = passedCounter
    results["failed"]   = faileCounter
    results["coverage"] = str((passedCounter/results["test_runs"])*100)+"%"

    return results


def main():
    configs = config.load('./config/config_spacy.yml')
    interpreter = Interpreter.load(configs["path"]+"/default/"+ configs["model_name"]+'/')
    results = processUtterance(configs,interpreter)
    writeToFile(configs["test_output"]+"test_case_result.json",results)
		
if __name__ == '__main__':
	main()
import json

resultFileName = "_TestResults_.json"
def openTheFile(fileName):
    with open(fileName, 'r') as testResultsFile:
        return testResultsFile.read()
def getJsonData(fileName):
    # Read the file
    try:
        fileRead = openTheFile(fileName)
    except:
        print("ERROR : Unable to read {}".format(fileName))
        return "fileReadError"

    # Load the json
    testResults = json.loads(fileRead)
    return testResults

def readTheValueFromJson(testResults, testType, requiredParameter):
    print("Reading {} {}".format(testType, requiredParameter))
    return testResults['summary'][testType]['_STAT'][requiredParameter]

testResults = getJsonData(resultFileName)

dataRead = int (readTheValueFromJson(testResults, "ITC", "testsPassing"))

print("Data : {}".format(dataRead))
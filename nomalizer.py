from nltk import *

file = open("group8Indexing.txt", "r")
text = file.read()
docs = text.split(".I")
for doc in docs :
    document = doc.split(".W")
    #print(document)
    if(len(document)>1):
        docNum = document[0]
        print(docNum)
        docText = document[1]
        print(docText)


from nltk import *

file = open("group8Indexing.txt", "r")
text = file.read()
docs = text.split(".I")
for doc in docs :
    print(doc)
    print("----------")


from nltk import *

file = open("group8Indexing.txt", "r")
text = file.read()
docs = text.split(".I")
small_docs = []
for doc in docs:
    small_docs.append(doc.split(".W"))

for doc in small_docs:
    if (len(doc) > 1):
        print(doc[1])
        print("----------")

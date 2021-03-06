from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import *
import json

file = open("group8Indexing.txt", "r")
text = file.read()
list = []
docs = text.split(".I")
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()
for doc in docs:
    document = doc.split(".W")
    if (len(document) > 1):
        docNum = document[0]
        docText = document[1]
        with open(docNum.rstrip()+".txt", "w") as output:
            output.write(docText)
      #  docTokens = word_tokenize(docText)
      #  filteredTokens = []
       # for w in docTokens:
        #    if w not in stop_words:
         #       filteredTokens.append(stemmer.stem(w))
       # x = {
        #    "text": filteredTokens
       # }
       # list.append(x)
#with open("normalized.json", "w") as outfile:
 #   json.dump(list, outfile)
  #  outfile.write("\n")

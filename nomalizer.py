from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem.porter import *

file = open("group8Indexing.txt", "r")
text = file.read()
docs = text.split(".I")
stop_words = set(stopwords.words('english'))

for doc in docs :
    document = doc.split(".W")
    if(len(document)>1):
        docNum = document[0]
        docText = document[1]
        docTokens = word_tokenize(docText)
        filteredTokens = []
        for w in docTokens:
            if w not in stop_words:
                filteredTokens.append(w)
        print(docNum)
        print(filteredTokens)


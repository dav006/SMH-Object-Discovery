import os
import pickle
from config import Config

index = 0
dictIndexFile = {}
for file in sorted(os.listdir(Config.WORD_ID_FOLDER+'.')):
	removeExt = ".".join(file.split(".")[:-1])
	removeFirstElement = "_".join(removeExt.split("_")[1:])
	dictIndexFile[index] = removeFirstElement
	index+=1

with open('indexToFile.pickle', 'wb') as handle:
    pickle.dump(dictIndexFile, handle, protocol=pickle.HIGHEST_PROTOCOL)

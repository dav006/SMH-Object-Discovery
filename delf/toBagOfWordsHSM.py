from sklearn.cluster import MiniBatchKMeans
from delf import feature_io
import os
from config import Config
import numpy as np
import hnswlib

stopWords = set()

inputpath = '../../oxford5k_features_attention/'
# Reiniting, loading the index
p = hnswlib.Index(space='l2', dim=40)
p.load_index("10000/hsm_10000_30iter.bin", max_elements = 10000)

#Convert DELF descriptors to visual words for each delf file
print('Convert DELF')
filelist = sorted(os.listdir(inputpath+'.'))
allVisualWords = []
count = 0
for entry in filelist:
	_, _, descriptors, _, _ = feature_io.ReadFromFile(inputpath+entry)
        labels, _ = p.knn_query(descriptors, k=1)
	npArray = labels.flatten()
	visualwords = set(npArray)
	allVisualWords.append(visualwords)
	count+=1
	print(count)

print('Get global count')
# Get global count
globalCount = {}
for wordToFreq in allVisualWords:
	for wordId in wordToFreq:
		if wordId not in globalCount:
			globalCount[wordId] = 1
		else:
			globalCount[wordId] += 1

minCount = 5
maxCount = 1519
#print('Min frecuency : {} and Max frecuency : {}'.format(minFreq,maxFreq))
addStop = 0
for key,value in globalCount.items():
	if value < minCount:
		stopWords.add(key)
		addStop+=1
	elif value > maxCount:
		stopWords.add(key)
		addStop+=1
print('Stop words : {}'.format(addStop))

countVis = 0
for wordToFreq in allVisualWords:
	countVis+=len(wordToFreq)
print('Visual words before stop words : {}'.format(countVis))

#Remove stop words
print('Remove stop words')
allWordToFreqNoStop = []
for wordToFreq in allVisualWords:
	allWordToFreqNoStop.append(wordToFreq.difference(stopWords))

countVis = 0
for wordToFreq in allWordToFreqNoStop:
	countVis+=len(wordToFreq)
print('Visual words after stop words : {}'.format(countVis))

#Remove stop words
print('Save binary BoW without stopWords')
outputFile = open(Config.CORPUS_FILE,'w')
for wordToFreq in allWordToFreqNoStop:
	#Write the dictionary in the default format
	outputFile.write(str(len(wordToFreq)))
	for wordId in wordToFreq:
		outputFile.write(' ')
		outputFile.write(str(wordId)+':1')
	outputFile.write('\n')
outputFile.close

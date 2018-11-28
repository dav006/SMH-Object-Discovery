#!/usr/bin/env python
# -*- coding: utf-8
#
# Description : This script reads the visual words and geometry for every image
# in http://www.robots.ox.ac.uk/~vgg/data/oxbuildings/ and transforms
# the input to a binary bag of words representation. For example:
#
#   [WORD_ID] [X] [Y] [A] [B] [C]
#
#   To:
#     size_of_list_1 item1_1:1 item2_1:1 ...
#     size_of_list_2 item1_2:1 item2_2:1 ...
#     size_of_list_N item1_N:1 item2_N:1 ...
#
#   This scipt also computes stop words and removes them from BoW
import os
from config import Config

stopWords = set()

allWordToFreq = []

print('Generate binary BoW')
# Generates binary bag of words
for file in sorted(os.listdir(Config.WORD_ID_FOLDER+'.')):
	wordToFreq = set()
	f = open(Config.WORD_ID_FOLDER+file,'r')
	index = 0
	for line in f:

		#First 2 lines are not needed
		index+=1
		if index<=2:
			continue

		line = line.strip()
		wordId = str(int(line.split(' ')[0])-1)

		wordToFreq.add(wordId)
	f.close

	allWordToFreq.append(wordToFreq)

print('Get global count')
# Get global count
globalCount = {}
for wordToFreq in allWordToFreq:
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
for wordToFreq in allWordToFreq:
	countVis+=len(wordToFreq)
print('Visual words before stop words : {}'.format(countVis))

#Remove stop words
print('Remove stop words')
allWordToFreqNoStop = []
for wordToFreq in allWordToFreq:
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
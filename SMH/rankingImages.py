import smh
from collections import Counter
import pickle
import operator
from config import Config

model = smh.listdb_load(Config.MODEL_FILE)
ifs = smh.listdb_load(Config.INVERT_INDEX_FILE)
idToFileName = ()
with open('indexToFile.pickle', 'rb') as handle:
    idToFileName= pickle.load(handle)

# Create array with all images associated with a objectDiscovered
allObjets = []
for objectDiscovered in model.ldb:
	imageCount={}
	for visualWord in objectDiscovered:
		visualWordName = visualWord.item
		for image in ifs.ldb[visualWordName]:
			if image.item not in imageCount:
				imageCount[image.item] = 0
			imageCount[image.item] += 1
	allObjets.append(imageCount)

print('Size of allObjets: {}'.format(len(allObjets)))

allObjetsRankingFile = []
for objectDiscovered in allObjets:
	
	# Sort list of images based on number of visual words
	objectDiscoveredSorted = sorted(objectDiscovered.items(), key=lambda x: x[1], reverse=True)
	
	#Convert image id to fileName
	objectDiscoveredRankingFile = []
	for id,_ in objectDiscoveredSorted:
		fileName = idToFileName[id]
		objectDiscoveredRankingFile.append(fileName)
	allObjetsRankingFile.append(objectDiscoveredRankingFile)

with open('allObjetsRankingFile.pickle', 'wb') as handle:
    pickle.dump(allObjetsRankingFile, handle, protocol=pickle.HIGHEST_PROTOCOL)
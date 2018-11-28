import smh
import pickle
import os
from matplotlib import pyplot
import sklearn.metrics
from config import Config

# Folder paths
objectsRankingFile = 'allObjetsRankingFile.pickle'

model = smh.listdb_load(Config.MODEL_FILE)
print(model.size())
ifs = smh.listdb_load(Config.INVERT_INDEX_FILE)
allObjetsToFileRanked = []
with open(objectsRankingFile, 'rb') as handle:
    allObjetsToFileRanked= pickle.load(handle)

print('Size of all objects discovered: {}'.format(len(allObjetsToFileRanked)))

allGroundTruthImages = {}

# Get all images that belong to a landmark (groundtruth)
# E.g :all souls [all_souls_000091, all_souls_000026, oxford_003410, ..]
for file in sorted(os.listdir(Config.GROUND_TRUTH_PATH+'.')):
	groundTruthName = file.split("_")[0]
	if groundTruthName not in allGroundTruthImages:
		allGroundTruthImages[groundTruthName] = []
	groundTruthArray = allGroundTruthImages[groundTruthName]
	f = open(Config.GROUND_TRUTH_PATH+file,'r')
	for line in f:
		fileName = line.rstrip()
		if fileName not in groundTruthArray:
			groundTruthArray.append(fileName)
	f.close

print('Size of allGroundTruthImages: {}'.format(len(allGroundTruthImages)))

allObjetsAP = []
averageAP = 0.0
for key, value in allGroundTruthImages.iteritems():
	print('Name of ground truth: {}'.format(key))
	maxAP = -1
	positiveImages = float(len(value))
	for objectToFile in allObjetsToFileRanked:
		precision = []
		recall = []
		truePositives = 0.0
		retrievedImages = 0.0
		for fileOb in objectToFile:
			if fileOb in value:
				truePositives +=1.0
			retrievedImages+=1.0
			precision.append(truePositives/retrievedImages)
			recall.append(truePositives/positiveImages)

		ap = sklearn.metrics.auc(recall,precision)
		if ap > maxAP:
			maxAP = ap
			'''
			pyplot.plot(recall, precision)
			pyplot.title('AP')
			pyplot.ylabel('Precision')
			pyplot.xlabel('Recall')
			pyplot.show()
			'''
	print('Best AP: {}'.format(maxAP))
	averageAP+=maxAP
print('Average AP: {}'.format(averageAP/11.0))
		
		





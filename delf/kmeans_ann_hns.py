
import numpy as np
import os
import sys
import io
import random
from delf import feature_io
import time
import tqdm
import hnswlib

DIM=40
MAX_ITER = 30
CLUSTER_NUM = 250000
DELF_FEATURES = 3810180

def read_delf_features(inputpath):
    print('Read delf Features')
    start_time = time.time()

    filelist = sorted(os.listdir(inputpath+'.'))
    random.shuffle(filelist)
    allDesc = np.empty((DELF_FEATURES,DIM))
    index = 0
    for entry in filelist:
        # Read features
        _, _, descriptors, _, _ = feature_io.ReadFromFile(inputpath+entry)
        size =descriptors.shape[0] 
        allDesc[index:index+size,:] = descriptors
        index+=size

    print('Read delf fetures Total time: %.3f s' % (time.time() - start_time))
    return allDesc
def get_random_clusters(delf_features):
    print('Get random clusters')
    idx = random.sample(range(DELF_FEATURES), CLUSTER_NUM)
    return delf_features[idx,:]

def kMeans(delf_features,clusters):
	start_time = time.time()

	for i in tqdm.trange(MAX_ITER):
                print('Build Tree')
		p = hnswlib.Index(space='l2', dim=DIM)
                p.init_index(max_elements=CLUSTER_NUM, ef_construction=100, M=16)
                p.add_items(clusters)
		clus_size = np.zeros(CLUSTER_NUM)
		new_centers = np.zeros((CLUSTER_NUM,DIM))
                
                print('Search KNN')
                index = 0
		for feature in delf_features:
		    labels, distances = p.knn_query(feature, k=1)
		    new_centers[labels[0,0]] += feature
		    clus_size[labels[0,0]]+=1
                    index+=1
                    sys.stdout.write("\r Percent : %.3f" % (index/float(DELF_FEATURES)))
                    sys.stdout.flush()
                print('\n')
                print('Re-assing cluster')
                for j in range(CLUSTER_NUM):
		    if clus_size[j] > 0:
			clusters[j] = new_centers[j] / clus_size[j]
		    else:
			rval = random.randint(0, DELF_FEATURES-1)
			clusters[j] = delf_features[rval]
			print('Empty cluster replaced')
                if i==MAX_ITER-1:
                    p.save_index("hsm_250000_30iter.bin")

	print('Total time: %.3f s' % (time.time() - start_time))
    
def main(inputpath):
    if os.path.isdir(inputpath):
        delf_features = read_delf_features(inputpath)
        clusters = get_random_clusters(delf_features)
        kMeans(delf_features,clusters)

    else:
        print "File doesn't exist"
        
if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print "Uso: python kmeans_ann.py features/"

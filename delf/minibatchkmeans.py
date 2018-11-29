# -*- coding: utf-8 -*- 
#
# Código de ejemplo de MiniBatchKMeans
#
# Curso de aprendizaje automatizado
# PCIC, UNAM
#
# Gibran Fuentes-Pineda
# Abril 2017
#
import numpy as np
import matplotlib.pyplot as plt
from zipfile import ZipFile
import os
import sys
import io
import random
import tqdm
from sklearn.cluster import MiniBatchKMeans
from sklearn.externals import joblib

def construct_vocabulary_delf(inputpath, number_of_iterations=100):
    mkm = MiniBatchKMeans(n_clusters = 1000)
    with ZipFile(inputpath) as imagedb:
        filelist = imagedb.infolist()
        random.shuffle(filelist)
        print filelist
        for i in tqdm.trange(number_of_iterations):
            for entry in filelist:
                if entry.filename.startswith('data_tarea/train/') and entry.filename.endswith('.npy'):
                    with io.BufferedReader(imagedb.open(entry)) as file:
                        X = np.load(file)
                        mkm.partial_fit(X)
                            
    return mkm

def main(inputpath):
    if os.path.isfile(inputpath):
        mkm = construct_vocabulary_sift(inputpath)

        # Guarda modelo en disco. Para cargarlo: mkm = joblib.load('vocabulary.pkl')
        joblib.dump(mkm, 'vocabulario.pkl') 
    else:
        print "File doesn't exist"
        
if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(sys.argv[1])
    else:
        print "Uso: python minibatchkmeans.py ruta_a_imagedb.zip"
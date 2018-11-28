import smh
from config import Config

corpus = smh.listdb_load(Config.CORPUS_FILE)
ifs = smh.listdb_load(Config.INVERT_INDEX_FILE)

discoverer = smh.SMHDiscoverer( 
	tuple_size = 4, 
	number_of_tuples =  500, 
	min_set_size = 3, 
	prune=True,
	overlap = 0.6,
	min_cluster_size = 3,
	cluster_tuple_size = 3,
    cluster_number_of_tuples =  255)
print('Iniciar fit')
models = discoverer.fit(ifs, expand = corpus)
print('Terminar fit')
models.save(Config.MODEL_FILE)
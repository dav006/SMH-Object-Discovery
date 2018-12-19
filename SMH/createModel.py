import smh
from smh_prune import SMHD
from config import Config

corpus = smh.listdb_load(Config.CORPUS_FILE)
ifs = smh.listdb_load(Config.INVERT_INDEX_FILE)

discoverer = SMHD( 
    tuple_size = 4, 
    number_of_tuples =  500, 
    min_set_size = 3, 
    overlap = 0.6,
    min_cluster_size = 3,
    cluster_tuple_size = 3,
    cluster_number_of_tuples =  255)
print('Iniciar fit')
models = discoverer.fit(ifs, prune = True, expand = corpus)
print('Terminar fit')
models.save(Config.MODEL_FILE)

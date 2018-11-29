# Uses SMH to create inverted index

import smh
from config import Config

print('open')
corpus = smh.listdb_load(Config.CORPUS_FILE)
print('invert')
ifs = corpus.invert()
ifs.save(Config.INVERT_INDEX_FILE)
# SMH WITH DELF descriptors
Unsupervised object discovery from large-scale image collections using DELF descriptors

Pre-requisits:
1. Follow instructions to build and install SMH https://github.com/gibranfp/Sampled-MinHashing
2. Modify the following files in SMH:
      1. smh_api.i add:
            ```c
            %include sampledmh.i
            ```
      2. smh.py add prunning:
            1. add prune (Boolean) atribute in class SMHDiscoverer
            2. add argument for prune in class init
            3. modify fit:
                  ```python
                  mined = self.mine(listdb, weights = weights, expand = expand)
                  if self.prune:
                        sa.sampledmh_prune(listdb.ldb,mined.ldb,3,3,0.7,0.8)
                  ```
3. Re-build and install
4. Follow instructions to extract DELF descriptors https://github.com/tensorflow/models/tree/master/research/delf

Instructions:
1. run delf/minibatchkmeans.py to generate visual vocabulary
2. run delf/idToFile.py to generate mappings from fileId to fileName
3. run delf/toBagOfWords.py to generate binary bag words without stop words
4. run delf/toInvertIndex.py to generate inverted index
5. run delf/createModel.py to create object model
6. run delf/rankingImages.py to rank images for evaluation
7. run delf/evaluate.py to get AP for each landmark

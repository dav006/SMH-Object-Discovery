#!/bin/bash
#
# Script to perform Sampled Min-Hashing on a given dataset
#
DATAPATH=`pwd`/data/oxford

smhcmd ifindex $DATAPATH/corpus.txt $DATAPATH/ifindex
smhcmd mine $DATAPATH/ifindex.txt $DATAPATH/mined.txt
smhcmd prune $DATAPATH/ifindex.txt $DATAPATH/mined.txt $DATAPATH/pruned.txt
smhcmd cluster $DATAPATH/pruned.txt $DATAPATH/objects.txt

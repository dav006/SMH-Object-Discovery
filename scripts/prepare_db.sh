#!/bin/bash
#
# Script to download and preprocess the oxford buildings dataset
#
REL_CMDPATH=`dirname $0`
ABS_CMDPATH=`pwd`
ABS_CMDPATH=$ABS_CMDPATH/$REL_CMDPATH

DATAPATH=`dirname $ABS_CMDPATH`
DATAPATH=$DATAPATH/data/oxford

IMAGES=`find $DATAPATH -type f -name "*.jpg"`
readarray -t IMAGES < <(printf '%s\n' $IMAGES | sort)
printf "%s\n" "${IMAGES[@]}" > $DATAPATH/images.txt

FEATURES=`find $DATAPATH/features -type f -name "*.sift1"`
readarray -t FEATURES < <(printf '%s\n' $FEATURES | sort)
printf "%s\n" "${IMAGES[@]}" > $DATAPATH/features.txt

WORDS=`find $DATAPATH/word_oxc1_hesaff_sift_16M_1M -type f -name "*.txt"`
readarray -t WORDS < <(printf '%s\n' $WORDS | sort)
printf "%s\n" "${IMAGES[@]}" > $DATAPATH/words.txt

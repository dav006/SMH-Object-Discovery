#!/bin/bash
#
# Script to download and preprocess the oxford buildings dataset
#
REL_CMDPATH=`dirname $0`
ABS_CMDPATH=`pwd`

if [[ $REL_CMDPATH == "." ]]
then
    REL_CMDPATH=""
fi

ABS_CMDPATH=$ABS_CMDPATH/$REL_CMDPATH

DATAPATH=`dirname $ABS_CMDPATH`
DATAPATH=$DATAPATH/data/oxford

echo "Generating index"

echo "Writing list of image files at $DATAPATH/images.txt"
IMAGES=`find $DATAPATH -type f -name "*.jpg"`
readarray -t IMAGES < <(printf '%s\n' $IMAGES | sort)
printf "%s\n" "${IMAGES[@]}" > $DATAPATH/images.txt

echo "Writing list of feature files at $DATAPATH/features.txt"
FEATURES=`find $DATAPATH/features -type f -name "*.sift1"`
readarray -t FEATURES < <(printf '%s\n' $FEATURES | sort)
printf "%s\n" "${FEATURES[@]}" > $DATAPATH/features.txt

echo "Writing list of word files at $DATAPATH/words.txt"
WORDS=`find $DATAPATH/word_oxc1_hesaff_sift_16M_1M -type f -name "*.txt"`
readarray -t WORDS < <(printf '%s\n' $WORDS | sort)
printf "%s\n" "${WORDS[@]}" > $DATAPATH/words.txt

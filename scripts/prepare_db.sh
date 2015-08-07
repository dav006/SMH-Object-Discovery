#!/bin/bash
#
# Script to download and preprocess the oxford buildings dataset
#
DATAPATH=`pwd`/data/oxford

if [ ! -a $DATAPATH/images ]
then
    mkdir -p $DATAPATH/images
fi
echo "Downloading images of the Oxford Buildings Dataset"
curl -L http://www.robots.ox.ac.uk/~vgg/data/oxbuildings/oxbuild_images.tgz | tar -xvz -C $DATAPATH/images

if [ ! -a $DATAPATH/features ]
then
    mkdir -p $DATAPATH/features
fi
echo "Downloading features of the Oxford Buildings Dataset"
curl -L http://www.robots.ox.ac.uk/~vgg/data/oxbuildings/feat_oxc1_hesaff_sift.bin.tgz | tar xvz

if [ ! -a $DATAPATH/words ]
then
    mkdir -p $DATAPATH/words
fi
echo "Downloading words of the Oxford Buildings Dataset"
curl -L http://www.robots.ox.ac.uk/~vgg/data/oxbuildings/word_oxc1_hesaff_sift_16M_1M.tgz | tar xvz -C $DATAPATH/words

if [ ! -a $DATAPATH/groundtruth ]
then
    mkdir -p $DATAPATH/groundtruth
fi
echo "Downloading groundtruth of the Oxford Buildings Dataset"
curl -L http://www.robots.ox.ac.uk/~vgg/data/oxbuildings/gt_files_170407.tgz | tar xvz -C $DATAPATH/groundtruth

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

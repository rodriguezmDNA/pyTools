#!/bin/bash

file=$@ 
mkdir -p 'out'

fname=$(basename $file)
basefile=${fname%'.txt'}
touch 'out/'$basefile'_processed.txt'
#tail -n +2 $file | awk 'BEGIN {FS="\t"; print "ID","sepArea","petArea"} {print $1,$2*$3,$4*$5}' > 'out/'$basefile'_processed.txt'
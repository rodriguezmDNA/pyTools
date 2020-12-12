#!/bin/bash

<<<<<<< HEAD
file=$@ 
mkdir -p 'out'

fname=$(basename $file)
basefile=${fname%'.txt'}
touch 'out/'$basefile'_processed.txt'
#tail -n +2 $file | awk 'BEGIN {FS="\t"; print "ID","sepArea","petArea"} {print $1,$2*$3,$4*$5}' > 'out/'$basefile'_processed.txt'
=======
#mkdir -p out
#tail -n +2 $file | xargs awk 'BEGIN {FS="\t"; print "ID","sepArea","petArea"} {print $1,$2*$3,$4*$5}'
awk 'BEGIN {FS="\t"; print "ID","sepArea","petArea"} {print $1,$2*$3,$4*$5\n}'
>>>>>>> e9f3117b4bb04f83b41abd1abe8be771c76db5d0

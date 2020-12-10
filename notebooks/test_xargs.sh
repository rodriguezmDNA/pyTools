#!/bin/bash

#mkdir -p out
#tail -n +2 $file | xargs awk 'BEGIN {FS="\t"; print "ID","sepArea","petArea"} {print $1,$2*$3,$4*$5}'
awk 'BEGIN {FS="\t"; print "ID","sepArea","petArea"} {print $1,$2*$3,$4*$5\n}'
#!/bin/bash
read -p "Sentence: " sentence

reverse=$(echo "$sentence" | awk '{for(i=NF;i>0;i--) printf "%s ", $i; print ""}')

echo "Reversed: $reverse"

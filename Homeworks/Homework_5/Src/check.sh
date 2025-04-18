#!/bin/bash
read -p "File to check: " filename

if [ -f "$filename" ]; then
   echo "'$filename' exists in the current directory"
else
   echo "'$filename' does not exists in the current directory"
fi

#!/bin/bash

filename="$1"

if [ -f "$filename" ]; then
    cat "$filename"
else
    echo "File '$filename' not found."
    exit 1
fi

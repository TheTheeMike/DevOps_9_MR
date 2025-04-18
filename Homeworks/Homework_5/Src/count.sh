#!/bin/bash

filename="$1"

if [ ! -f "$filename" ]; then
    echo "Error: File '$filename' not found."
    exit 1
fi

line_count=$(wc -l < "$filename")
echo "The file '$filename' has $line_count lines."


#!/bin/bash

WATCH_DIR="$HOME/watch"

inotifywait -m -e create --format "%f" "$WATCH_DIR" | while read new_file; do
    echo "New file detected!"
    cat "$WATCH_DIR/$new_file"
    
    mv "$WATCH_DIR/$new_file" "$WATCH_DIR/$new_file.back"
done

#!/bin/bash

# Start at the root directory (or adjust the starting path as needed)
start_dir="."

# Find and process all directories named 'csv' or 'result'
find "$start_dir" -type d \( -name "csv" -o -name "result" \) | while read dir; do
    # Empty the folder (remove all files and subdirectories)
    rm -rf "$dir"/*

    # Print the cleaned directory path
    echo "Cleaned: $dir"
done

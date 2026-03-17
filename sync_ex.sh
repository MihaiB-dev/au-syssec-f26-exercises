#!/bin/bash

# Ensure a folder name was provided
if [ -z "$1" ]; then
    echo "Usage: ./sync_ex.sh folder_name"
    exit 1
fi

FOLDER_NAME="$1"

# 1. Download the latest changes from upstream
git fetch upstream

# 2. Update only the specified folder
git checkout upstream/main -- "$FOLDER_NAME"

echo "Successfully updated $FOLDER_NAME from upstream/main"
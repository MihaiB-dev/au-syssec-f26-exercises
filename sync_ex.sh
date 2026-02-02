#!/bin/bash

COMMIT_MSG=${1:-".."}

# 1. Download the latest changes from class
git fetch upstream

# 2. Merge the changes into my local branch
# The --no-edit flag skips the manual commit message prompt for the merge
git merge upstream/main --no-edit

# 3. Stage all of my new exercise files
git add .

# 4. Commit with the literal message ".."
git commit -m "$COMMIT_MSG"

# 5. Push everything to my personal GitHub repository
git push origin main
#!/bin/sh
OUTPUT="merged.pdf"

# Find and sort files numerically, then concatenate
find . -maxdepth 1 -name 'sorted*' -print0 | \
  sort -z -t 't' -k 2n | \
  xargs -0 cat > "$OUTPUT"

echo "Merged files into $OUTPUT"

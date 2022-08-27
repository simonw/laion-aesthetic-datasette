#!/bin/bash

# Create table
sqlite3 laion-aesthetic.db '
CREATE TABLE IF NOT EXISTS images (
   [text] TEXT,
   [url] TEXT,
   [width] INTEGER,
   [height] INTEGER,
   [similarity] FLOAT,
   [hash] TEXT,
   [punsafe] FLOAT,
   [pwatermark] FLOAT,
   [aesthetic] FLOAT
);'

# Loop through and import ever *.parquet file in the current directory
for filename in *.parquet; do
    parquet-tools csv $filename | sqlite3 -csv laion-aesthetic.db ".import --skip 1 '|cat -' images"
done

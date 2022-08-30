#!/bin/bash

# Create table
sqlite3 laion-aesthetic-6pls.db '
CREATE TABLE IF NOT EXISTS images (
   [url] TEXT,
   [text] TEXT,
   [width] INTEGER,
   [height] INTEGER,
   [similarity] FLOAT,
   [punsafe] FLOAT,
   [pwatermark] FLOAT,
   [aesthetic] FLOAT,
   [hash] TEXT,
   [__index_level_0__] INTEGER
);'

# Loop through and import ever *.parquet file in the current directory
for filename in *.parquet; do
    parquet-tools csv $filename | sqlite3 -csv laion-aesthetic-6pls.db ".import --skip 1 '|cat -' images"
done

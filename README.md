# laion-aesthetic-datasette

Use Datasette to explore the [laion-aesthetic](https://huggingface.co/datasets/laion/laion2B-en-aesthetic/tree/main) training data

## Fetching the data

Run `./fetch-data.sh` to fetch 8GB of Parquet files.

You need `git-lfs` installed. On macOS, you can install like this:

    brew install git-lfs
    git lfs install

## Importing Parquet data into SQLite

You need `parquet-tools` and `sqlite-utils` installed:

    pipx istall parquet-tools sqlite-utils

Then run `./import-data.sh` to create and populate a ~14GB SQLite database.

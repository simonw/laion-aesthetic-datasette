# laion-aesthetic-datasette

Use Datasette to explore the [improved_aesthetics_6plus](https://huggingface.co/datasets/ChristophSchuhmann/improved_aesthetics_6plus) training data used by [Stable Diffusion](https://github.com/CompVis/stable-diffusion).

Browse the data (12m+ images) here: https://laion-aesthetic.datasette.io/laion-aesthetic-6pls/images

For background on this project, see [Exploring 12 Million of the Images Used to Train Stable Diffusion’s Image Generator](https://waxy.org/2022/08/exploring-12-million-of-the-images-used-to-train-stable-diffusions-image-generator/).

A collaboration between [Andy Baio](https://wax.org/) and [Simon Willison](https://simonwillison.net/).

## Some rough notes from the implementation

[Issue #7](https://github.com/simonw/laion-aesthetic-datasette/issues/7) includes step-by-step details on how we built this database.

### Fetching the data

Run `./fetch-data.sh` to fetch the Parquet files.

You need `git-lfs` installed. On macOS, you can install like this:

    brew install git-lfs
    git lfs install

## Importing Parquet data into SQLite

You need `parquet-tools` and `sqlite-utils` installed:

    pipx install parquet-tools sqlite-utils

Then run `./import-data.sh` to create and populate a ~14GB SQLite database.

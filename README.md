# waymo-utils
Tools for downloading/manipulating the Waymo Open Dataset

Inspired by: https://github.com/RalphMao/Waymo-Dataset-Tool

## Getting Started
Make sure you have the following prerequisites:
- Python 3
- Install `gsutil` [here](https://cloud.google.com/sdk/docs/quickstart)

1. Run `gcloud init` and sign in with the account that has access to Waymo Open Dataset
2. Run `python download.py <training|validation|testing> --out-dir <output-dir>`
#!/bin/bash
git clone https://huggingface.co/datasets/laion/laion2B-en-aesthetic
cd laion2B-en-aesthetic
git lfs fetch
git lfs checkout

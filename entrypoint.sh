#!/bin/bash

set -e

# ref: https://docs.github.com/cn/actions/creating-actions/dockerfile-support-for-github-actions#workdir
cd $GITHUB_WORKSPACE && ls && python /generate-chart.py
# echo "Img dir: $IMG_DIR"
echo "Img dir input: $INPUT_IMG_DIR"
cp individual.png daily_total.png $INPUT_IMG_DIR/

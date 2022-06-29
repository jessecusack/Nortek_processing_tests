#!/usr/bin/env bash
source $CONDA_PREFIX/etc/profile.d/conda.sh
conda activate nortek-test && jupyter kernelspec uninstall nortek-test && conda deactivate
conda remove --name nortek-test --all
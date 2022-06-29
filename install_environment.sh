#!/usr/bin/env bash
source $CONDA_PREFIX/etc/profile.d/conda.sh
conda env create -f environment.yml
conda activate nortek-test && python -m ipykernel install --user --name nortek-test
cd matlab_toolboxes 
./get_toolboxes.sh
cd ../scripts
jupytext --to=ipynb xarray_check_data.py dolfyn_check_data.py
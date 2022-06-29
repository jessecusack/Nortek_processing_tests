# Nortek Processing Tests

Tests of different data processing tools for Nortek ADCPs

## Requirements


* [Conda package manager](https://conda.io/en/latest/) (I recommend the lightweight version [miniconda](https://docs.conda.io/en/latest/miniconda.html))
* MATLAB, including one of the toolboxes below:

```
 'quaternion' requires one of the following:
  Automated Driving Toolbox
  Navigation Toolbox
  Radar Toolbox
  Robotics System Toolbox
  Sensor Fusion and Tracking Toolbox
  UAV Toolbox
```

## Test data

Eli shared a Box drive containing some test data. I think this is from an instrument on a glider. I copied the following files to `data/external`:

```
Box/LeConte/testdata/Data_0000.ad2cp  # 1 GB 
Box/LeConte/testdata/Data_0000.ad2cp.00001_1.nc  # 330 MB 
Box/LeConte/testdata/Data_0000.ad2cp.00001_2.nc  # 330 MB 
```

My understanding is that the netcdf files are generated from the ad2cp file. 

## Processing Tools

### ocean-tools (MATLAB)

Dylan's toolbox is available at https://github.com/dswinters/ocean-tools. It is downloaded automatically using the script `matlab_toolboxes/get_toolboxes.sh`.

I tested the toolbox by first parsing the raw Nortek data and converting to a .mat with:

```
scripts/ocean_tools_convert.m
```

Then I plotted some of the data:

```
scripts/ocean_tools_check_data.m
```

Then I tried rotating into earth coordinates:

```
scripts/ocean_tools_rotate.m
```

This requires a toolbox that provies the `quaternion` function.

_Notes_

* The parsed data does not contain pressure or temperature, but I find them in the netcdf? Not sure if these are in the ad2cp file or added somewhere else in the netcdf creation.
* Requires additional MATLAB toolboxes for `quaternion`.
* Rotation worked, I think... 

### xarray (python)

Installed with the conda environment. Tested in the notebook `scripts/xarray_check_data.py`. To convert this script to a notebook, you may need to use:

```
conda activate nortek-test
jupytext --to=ipynb scripts/xarray_check_data.py
``` 

This is done automatically by the install script. 


_Notes_

* Data is stored in the group `Data/Burst`.
* Obscene variable and coordinate layout, eurgh.
* Data appear to be in beam coordinates. 

### dolfyn (python)

Installed with the conda environment.

```
scripts/dolfyn_check_data.ipynb
```

_Notes_

* Loads the `ad2cp` data no problem.
* Can do beam rotations, but was confused by the Glider model of ADCP.
* Looks very promising for a python solution. 

## Installing and removing the environment

A conda environment is specified in `environment.yml` and may be install using the appropriate bash scripts. 

To install:

```bash
./install_environment.sh
```

To remove:

```bash
./remove_environment.sh
```

These also install/remove the jupyter kernel for the environment.

> If these don't execute, you might need to change the file permissions with `chmod u+x *.sh`.

## Project Structure
```
Nortek_processing_tests/
    ├── LICENSE
    ├── README.md          <- The top-level README for people using this project.
    ├── data/
    │   ├── external       <- Data pulled in from outside of this project.
    │   └── internal       <- Data generated within this project.
    │
    ├── scripts/           <- MATLAB scripts and jupyter notebooks
    │   └── README.md      <- Any information about the code, such as execution order. 
    │
    ├── figures/           <- Saved figures generated during analysis.
    │
    ├── environment.yml    <- Conda environment specification. Install using the bash scripts.
    │
    ├── matlab_toolboxes/  <- A place for 3rd party MATLAB toolboxes.
    │   ├── toolbox/
    │   └── get_toolbox.sh <- Script to download toolboxes.
 ```

---

* Free software: MIT license


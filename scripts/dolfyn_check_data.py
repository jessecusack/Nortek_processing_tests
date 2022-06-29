# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     notebook_metadata_filter: -jupytext.text_representation.jupytext_version
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#   kernelspec:
#     display_name: nortek-test
#     language: python
#     name: nortek-test
# ---

# %%
import dolfyn
import numpy as np

# %%
dat = dolfyn.read("../data/external/Data_0000.ad2cp")

# %%
dat

# %% [markdown]
# Try rotating into earth coordinates.

# %%
# we have to hack the model from Glider to Signature otherwise dolfyn will not do the rotation
dat["inst_model"] = "Signature"

rot = dolfyn.rotate2(dat)

# %%
rot

# %% [markdown]
# Plot some quantities

# %%
# Stupid UNIX time
dat.vel.sel(dir=1).sel(time=slice(np.datetime64("2021-06-27").astype('datetime64[s]').astype(float), None)).plot()

# %%
rot.vel.sel(dir="E").sel(time=slice(np.datetime64("2021-06-27").astype('datetime64[s]').astype(float), None)).plot()

# %%
rot.pressure.sel(time=slice(np.datetime64("2021-06-27").astype('datetime64[s]').astype(float), None)).plot()


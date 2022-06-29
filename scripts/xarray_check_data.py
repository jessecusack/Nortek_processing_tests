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
import xarray as xr
import matplotlib.pyplot as plt

# %%
config1 = xr.open_dataset("../data/external/Data_0000.ad2cp.00001_1.nc", group="Config")
burst1 = xr.open_dataset("../data/external/Data_0000.ad2cp.00001_1.nc", group="Data/Burst")
config2 = xr.open_dataset("../data/external/Data_0000.ad2cp.00001_2.nc", group="Config")
burst2 = xr.open_dataset("../data/external/Data_0000.ad2cp.00001_2.nc", group="Data/Burst")

# %% [markdown]
# Check out data structure...

# %% tags=[]
config1

# %%
burst1

# %% [markdown]
# Plot some things...

# %%
fig, axs = plt.subplots(2, 1, sharex=True, figsize=(16, 8))
burst1.Pressure.plot(ax=axs[0], label="1")
burst2.Pressure.plot(ax=axs[0], label="2")
burst1.WaterTemperature.plot(ax=axs[1])
burst2.WaterTemperature.plot(ax=axs[1])
axs[0].legend()
axs[0].invert_yaxis()

# %%
fig, ax = plt.subplots(figsize=(16, 4))
burst1.AmplitudeBeam1.plot(ax=ax, x="time")

# %%
fig, ax = plt.subplots(figsize=(16, 4))
burst1.CorrelationBeam1.plot(ax=ax, x="time")

# %%
fig, ax = plt.subplots(figsize=(16, 4))
burst1.VelocityBeam1.plot(ax=ax, x="time")

# %%
fig, ax = plt.subplots()
ax.plot(burst1.time, ".")

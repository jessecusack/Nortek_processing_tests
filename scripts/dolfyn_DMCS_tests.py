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

# %% [markdown]
# # 250 Test 1 burst 4 beams

# %%
t1 = dolfyn.read("../data/external/Rutgers_ADCP_tests_2022/103461_DMCS_test_1/DMCS_test_1.ad2cp")

# %%
t1

# %%
t1.time_bt.data - t1.time.data

# %% [markdown]
# # 250 Test 2 multiplexing

# %%
mux = dolfyn.read("../data/external/Rutgers_ADCP_tests_2022/103461_DMCS_test_mux/DMCS_test_mux.ad2cp")

# %% [markdown]
# # 250 Test 3 burst beams 2 3 4

# %%
b234 = dolfyn.read("../data/external/Rutgers_ADCP_tests_2022/103461_DMCS_test_b234/DMCS_test_b234.ad2cp")

# %% [markdown]
# # 500 Test echosounder

# %%
d5 = dolfyn.read("../data/external/Rutgers_ADCP_tests_2022/AD2CP_Profiler_ECHOTEST500/ECHOTEST500.ad2cp")

# %% [markdown]
# # 500 Test 

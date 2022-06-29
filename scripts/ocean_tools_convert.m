addpath("../matlab_toolboxes/ocean-tools/")

dat = parse_nortek_adcp("../data/external/Data_0000.ad2cp");

save("../data/internal/Data_0000.mat", '-struct', 'dat');



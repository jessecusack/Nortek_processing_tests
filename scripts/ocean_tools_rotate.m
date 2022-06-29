addpath("../matlab_toolboxes/ocean-tools/")

if ~exist('dat', 'var')
    dat = load("../data/internal/Data_0000.mat");
end

declination = 0;
angles = [-dat.roll(:), -dat.pitch(:), dat.heading(:) - declination];
beam2earth = quaternion(angles, 'eulerd', 'YXZ', 'frame');
rot = adcp_beam2earth(dat, beam2earth, 'down');

save("../data/internal/Data_0000_rotated.mat", '-struct', 'rot');
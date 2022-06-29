if ~exist('dat', 'var')
    dat = load("../data/internal/Data_0000.mat");
    rot = load("../data/internal/Data_0000_rotated.mat");
end

close all

% Plot config
step = 100;
use = dat.time > datenum('27-June-2021');  % weird data before this
time = dat.time(use);

% Beam 3 echo, these should be the same between coordinates systems
figure(11)
a1 = squeeze(dat.echo_intens(:, 3, use));
a1r = squeeze(rot.echo_intens(:, 3, use));

subplot(2,1,1);
pcolor(time(1:step:end), dat.cell_depth, a1(:, 1:step:end))
shading flat
datetick

subplot(2,1,2); 
pcolor(time(1:step:end), dat.cell_depth, a1r(:, 1:step:end))
shading flat
datetick

% Beam 1 velocity, these should be different!
figure(12)
v1 = squeeze(dat.vel(:, 1, use));
v1r = squeeze(rot.vel(:, 1, use));

subplot(2,1,1);
pcolor(time(1:step:end), dat.cell_depth, v1(:, 1:step:end))
shading flat
datetick

subplot(2,1,2); 
pcolor(time(1:step:end), dat.cell_depth, v1r(:, 1:step:end))
shading flat
datetick

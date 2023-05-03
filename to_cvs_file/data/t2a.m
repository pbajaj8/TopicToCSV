function t2a(cvsPath)
%UNTITLED Summary of this function goes here
%   Detailed explanation goes here
T = readtable(cvsPath, 'ReadVariableNames',true);

[n_row, ~] = size(T);
B = [];
for i = 1:n_row
   a = table2array(T(i:i, ["TipTransX", "TipTransY", "TipTransZ", "ZaberVel"])); 
   sprintf('%f,%f', a(1), a(2))
end

end
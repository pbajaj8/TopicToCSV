function [x_ekf_bro, AB] = ekf_with_broydenUpdateMM(T,Q)
%UNTITLED2 Summary of this function goes here
%   Detailed explanation goes here
    factor = 1e3; 
    T = readtable(filepath,'ReadVariableName',true);
    R = [0.49 0 0; 0 0.49 0; 0 0 0.49]; 
    H = [1 0 0; 0 1 0; 0 0 1];

    [n_row, ~] = size(T);
    
    % Initial A and AB. 
    A = [1 0 0; 0 1 0; 0 0 1]; 
    % Keeping AB time independent, and shifting time to velocity side by using
    % v * dt; This well help me to update AB with broyden update without
    % worring about dt component in AB matrix. 
    AB = [A, [1 0 0; 0 1 0; 0 0 1]]; 
    
    Rbh = quat2rotm(table2array(T(1:1, ["HandleRotW", "HandleRotX", "HandleRotY", "HandleRotZ"])));
    
    % Zaber Velocity is w.r.t to handle frame, it needs to be transfromed by
    % Rbh to get it w.r.t base frame. 
    old_time = (table2array(T(1:1, "Time")) + (1e-9 * table2array(T(1:1, "TimeNanosec"))));
    U = Rbh * [0; -table2array(T(1:1, "ZaberVel")); 0]; 
    Xt = transpose(factor * table2array(T(1:1, ["TipTransX", "TipTransY", "TipTransZ"]))); 
    Pt = [10 0 0; 0 10 0; 0 0 10]; 
    
    x_ekf_bro = [transpose(Xt)];
    measurementCounter = 0;

    
    
end
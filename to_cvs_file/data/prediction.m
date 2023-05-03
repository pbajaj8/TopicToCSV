function x_hat = prediction(FilePath,Q)
    
    T = readtable(FilePath, 'ReadVariableName',true);
    R = [4.9000e-07 0 0; 0 4.9000e-07 0; 0 0 4.9000e-07]; 
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
    U = Rbh * [0; -1e-3*table2array(T(1:1, "ZaberVel")); 0]; 
    Xt = transpose(table2array(T(1:1, ["TipTransX", "TipTransY", "TipTransZ"]))); 
    Pt = [10 0 0; 0 10 0; 0 0 10]; 
    
    x_hat = [transpose(Xt)];

    for i = 2:n_row
        new_time = (table2array(T(i:i, "Time")) + (1e-9 * table2array(T(i:i, "TimeNanosec"))));
        dt = new_time - old_time; 
    
        [Xt_hat, Pt_hat] = predictionEKF(Xt, Pt, U, AB, Q, dt); 
        
        x_hat = [x_hat; transpose(Xt_hat)];
    
        % Updates after one cycle; 
        Xt = Xt_hat; 
        Pt = Pt_hat;
        old_time = new_time; 
        Rbh = quat2rotm(table2array(T(i:i, ["HandleRotW", "HandleRotX", "HandleRotY", "HandleRotZ"])));
        U = Rbh * [0; (-1e-3)*table2array(T(i:i, "ZaberVel")); 0]; 
    end 


end
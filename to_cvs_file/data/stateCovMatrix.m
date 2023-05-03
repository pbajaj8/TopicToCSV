function [Q, z_observed] = stateCovMatrix(fileAddress)
    
    factor = 1e3; 

    T = readtable(fileAddress, 'ReadVariableName',true);
    [n_row, ~] = size(T); 

    A = [1 0 0; 0 1 0; 0 0 1];
    AB = [A, [1 0 0; 0 1 0; 0 0 1]]; 

    Rbh = quat2rotm(table2array(T(1:1, ["HandleRotW", "HandleRotX", "HandleRotY", "HandleRotZ"])));
    old_time = (table2array(T(1:1, "Time")) + (1e-9 * table2array(T(1:1, "TimeNanosec"))));

    U = Rbh * [0; -table2array(T(1:1, "ZaberVel")); 0];
    %U = [0; -0.002; 0];
    Xt = transpose(factor * table2array(T(1:1, ["TipTransX", "TipTransY", "TipTransZ"])));

    e = [];
    z_observed = [transpose(Xt)];

    for i = 2:n_row
        new_time = (table2array(T(i:i, "Time")) + (1e-9 * table2array(T(i:i, "TimeNanosec"))));
        dt = new_time - old_time; 

        Xt_hat = AB * [Xt; U * dt];

        Zt = transpose(factor * table2array(T(i:i, ["TipTransX", "TipTransY", "TipTransZ"])));
       
        z_observed = [z_observed; transpose(Zt)];

        
        e = [e; transpose(Zt - Xt_hat)]; 
    
        % Updates for next time. 
        old_time = new_time; 
        Xt = Zt;
        Rbh = quat2rotm(table2array(T(i:i, ["HandleRotW", "HandleRotX", "HandleRotY", "HandleRotZ"])));
        U = Rbh * [0; -table2array(T(i:i, "ZaberVel")); 0];
        
    end 

    Q = cov(abs(e)); 

end
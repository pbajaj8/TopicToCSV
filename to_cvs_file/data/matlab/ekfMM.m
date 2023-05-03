function [x_ekf, x_hat] = ekfMM(T,Q)

    factor = 1e3; 
    R = [0.49 0 0; 0 0.49 0; 0 0 0.49]; 
    H = [1 0 0; 0 1 0; 0 0 1];

    [n_row, ~] = size(T);

    A = [1 0 0; 0 1 0; 0 0 1];
    AB = [A, [1 0 0; 0 1 0; 0 0 1]];

    Rbh = quat2rotm(table2array(T(1:1, ["HandleRotW", "HandleRotX", "HandleRotY", "HandleRotZ"])));
    old_time = (table2array(T(1:1, "Time")) + (1e-9 * table2array(T(1:1, "TimeNanosec"))));
    U = Rbh * [0; -table2array(T(1:1, "ZaberVel")); 0]; 
    Xt = transpose(factor * table2array(T(1:1, ["TipTransX", "TipTransY", "TipTransZ"])));
    Pt = [10 0 0; 0 10 0; 0 0 10];

    
    x_ekf = [transpose(Xt)];
    x_hat = [transpose(Xt)];

    for i = 2:n_row
        new_time = (table2array(T(i:i, "Time")) + (1e-9 * table2array(T(i:i, "TimeNanosec"))));
        dt = new_time - old_time;

        [Xt_hat, Pt_hat] = predictionEKF(Xt, Pt, U, AB, Q, dt); 

        x_hat = [x_hat; transpose(Xt_hat)];

        if (rem(i,1) == 0)
            Zt = transpose(factor * table2array(T(i:i, ["TipTransX", "TipTransY", "TipTransZ"])));
            [Xtt, Ptt] = measurementEKF(Xt_hat, Pt_hat, Zt, H, R); 
            x_ekf = [x_ekf; transpose(Xtt)];
            Xt = Xtt; 
            Pt = Ptt;  
        else    
            x_ekf = [x_ekf; transpose(Xt_hat)];
            Xt = Xt_hat; 
            Pt = Pt_hat; 
        end 


        old_time = new_time; 
        Rbh = quat2rotm(table2array(T(i:i, ["HandleRotW", "HandleRotX", "HandleRotY", "HandleRotZ"])));
        U = Rbh * [0; -table2array(T(i:i, "ZaberVel")); 0]; 
    end 


end
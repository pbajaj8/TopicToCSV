clear; 
csvPath = '/home/pranav/needle_steering/src/test/to_cvs_file/data/one.csv';
%normal_factor = 2*1e2;

%csvPath = '/home/pranav/needle_steering/src/test/to_cvs_file/data/two.csv';
learning_rate = 1;

%csvPath = '/home/pranav/needle_steering/src/test/to_cvs_file/data/three.csv';
%normal_factor = 2*1e2;

%csvPath = '/home/pranav/needle_steering/src/test/to_cvs_file/data/forth.csv';
%normal_factor = 2*1e2;

[Q, z_observed] = stateCovMatrix(csvPath); 

[x_ekf, x_hat, Pt, error] = ekf(csvPath, Q); 

[x_ekf_bro, AB, Pt_bro, error_bro] = ekf_with_broydenUpdate(csvPath, Q);



%tiledlayout(2,1)

%nexttile
plot(-x_ekf(:,2), x_ekf(:,1), "g")
hold("on")
plot(round(-z_observed(:,2),4), z_observed(:,1),"k")
hold("on")
plot(-x_ekf_bro(:,2), x_ekf_bro(:,1),"r")
hold("off")
title('Plot: Y vs X position, Needle insertion 5cm')
xlabel('y-axis (Insertion Axis)')
ylabel('x-axis')
legend('ekf','ground truth', 'ekf with Broydan update')

%nexttile
%plot(-x_ekf(:,2), x_ekf(:,3), "g")
%hold("on")
%plot(-z_observed(:,2),z_observed(:,3), "k")
%hold("on")
%plot(-x_ekf_bro(:,2), x_ekf_bro(:,3),"r")
%hold("off")
%title('Plot: Y vs Z position, Needle insertion 5cm')
%xlabel('y-axis (Insertion Axis)')
%ylabel('z-axis')
%xlabel('y-axis (Insertion Axis)')
%ylabel('x-axis')
%legend('ekf','ground truth', 'ekf with Broydan update')


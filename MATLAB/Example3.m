close all

try
    python_version = pyversion;
    fprintf(2,'** Python Version : %s\n', python_version);
catch e
    fprintf(2,'** Error : %s\n', e.message);
end

% Import pycm lib
pycmlib = py.importlib.import_module('pycm');
% Input file
address = 'cm1.obj';
file = py.open(address,'r');
% ConfusionMatrix object
cm = pycmlib.ConfusionMatrix(pyargs('file', file));
% Matrix
disp(cm.matrix);
% Classes list
disp(cm.classes);
% Print matrix
cm.print_matrix()
% Print normalized matrix
cm.print_normalized_matrix();
% Print stat
cm.stat();

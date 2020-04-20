close all

try
    python_version = pyversion;
    fprintf(2,'** Python Version : %s\n',python_version);
catch e
    fprintf(2,'** Error : %s\n',e.message);
end

% Import pycm lib
pycmlib = py.importlib.import_module('pycm');
% Input matrix
matrix = py.dict(pyargs('Class1', py.dict(pyargs('Class1', py.int(1), 'Class2',py.int(2))), 'Class2', py.dict(pyargs('Class1', py.int(0), 'Class2', py.int(5)))));
% ConfusionMatrix object
cm = pycmlib.ConfusionMatrix(NaN, NaN,matrix);
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

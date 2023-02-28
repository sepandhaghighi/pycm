close all

try
    python_version = pyversion;
    fprintf(2, '** Python Version : %s\n', python_version);
catch e
    fprintf(2, '** Error : %s\n', e.message);
end

% Import pycm lib
pycmlib = py.importlib.import_module('pycm');
% Actual and predict vectors
y_actu = py.list(['2', '0', '2', '2', '0', '1', '1', '2', '2', '0', '1', '2']);
y_pred = py.list(['0', '0', '2', '1', '0', '2', '1', '0', '2', '0', '2', '2']);
% ConfusionMatrix object
cm = pycmlib.ConfusionMatrix(y_actu, y_pred);
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
% Save object
cm.save_obj('cm1');
% Save html
cm.save_html('cm1');
% Save csv
cm.save_csv('cm1');

close all

try
    python_version = pyversion;
    fprintf(2,'** Python Version : %s\n',python_version);
catch e
    fprintf(2,'** Error : %s\n',e.message);
end

% Import pycm lib
pycmlib = py.importlib.import_module('pycm');
% Actual and predict vectors
y_actu = py.list(['2', '0', '2', '2', '0', '1', '1', '2', '2', '0', '1', '2']);
y_pred1 = py.list(['0', '0', '2', '1', '0', '2', '1', '0', '2', '0', '2', '2']);
y_pred2 = py.list(['1', '2', '2', '2', '2', '2', '1', '2', '2', '0', '2', '2']);
% ConfusionMatrix object
cm1 = pycmlib.ConfusionMatrix(y_actu, y_pred1);
cm2 = pycmlib.ConfusionMatrix(y_actu, y_pred2);
% Compare object
cp = pycmlib.Compare(py.dict(pyargs('cm1',cm1,'cm2',cm2)));
% Best
best_cm = cp.best;
best_cm.print_matrix()
% Print report
cp.print_report()
% Save report
cp.save_report('report');


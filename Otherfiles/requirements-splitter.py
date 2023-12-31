# -*- coding: utf-8 -*-
"""Requirements splitter."""

PLOT_LIB_LIST = ["matplotlib", "seaborn"]
test_req = ""
plot_req = ""

with open('dev-requirements.txt', 'r') as f:
    for line in f:
        plot_lib_flag = False
        for lib in PLOT_LIB_LIST:
            if line.find(lib) != -1:
                plot_lib_flag = True
                plot_req += line
                break
        if '==' not in line and not plot_lib_flag:
            test_req += line

with open('test-requirements.txt', 'w') as f:
    f.write(test_req)

with open('plot-requirements.txt', 'w') as f:
    f.write(plot_req)

# -*- coding: utf-8 -*-
"""Notebook-run script."""
import os
import shutil
import pycm
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from art import tprint

NOTEBOOKS_LIST = [
    "Document",
    "Distance",
    "Example1",
    "Example2",
    "Example3",
    "Example4",
    "Example5",
    "Example6",
    "Example7",
    "Example8"]

COPY_DICT = {os.path.join("Document", "Document_files", "cm1.csv"): os.path.join("Otherfiles", "test.csv"),
             os.path.join("Document", "Document_files", "cm1.html"): os.path.join("Otherfiles", "test.html"),
             os.path.join("Document", "Document_files", "cm1.obj"): os.path.join("Otherfiles", "test.obj"),
             os.path.join("Document", "Document_files", "cm1.pycm"): os.path.join("Otherfiles", "test.pycm"),
             os.path.join("Document", "Document_files", "cp.comp"): os.path.join("Otherfiles", "test.comp"),
             }

EXTENSION = ".ipynb"

if __name__ == "__main__":
    tprint("PYCM", "bulbhead")
    tprint("v{0}".format(pycm.__version__), "bulbhead")
    tprint("Notebook Run", "amc3line")
    print("Processing ...")
    for index, notebook in enumerate(NOTEBOOKS_LIST):
        ep = ExecutePreprocessor(timeout=6000, kernel_name='python3')
        path = os.path.join("Document", notebook)
        with open(path + EXTENSION, "r", encoding="utf-8") as f:
            nb = nbformat.read(f, as_version=4)
            ep.preprocess(nb, {'metadata': {'path': 'Document/'}})
        with open(path + EXTENSION, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        print("{0}.{1} [OK]".format(str(index + 1), notebook))
    print("\nCopying ...")
    for index, item in enumerate(sorted(COPY_DICT)):
        shutil.copy(item, COPY_DICT[item])
        print("\t{0}.{1} --> {2} [OK]".format(index + 1, item, COPY_DICT[item]))

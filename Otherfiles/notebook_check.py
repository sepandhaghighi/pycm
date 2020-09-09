import os
import nbformat
from nbconvert.preprocessors import ExecutePreprocessor
from art import tprint

NOTEBOOKS_LIST = [
    "Document",
    "Example1",
    "Example2",
    "Example3",
    "Example4",
    "Example5",
    "Example6",
    "Example7",
    "Example8"]

EXTENSION = ".ipynb"

if __name__ == "__main__":
    tprint("PYCM","bulbhead")
    tprint("Document","bulbhead")
    ep = ExecutePreprocessor(timeout=6000, kernel_name='python3')
    print("Processing ...")
    for index, notebook in enumerate(NOTEBOOKS_LIST):
        path = os.path.join("Document", notebook)
        with open(path + EXTENSION) as f:
            nb = nbformat.read(f, as_version=4, encoding='utf-8')
            ep.preprocess(nb, {'metadata': {'path': 'Document/'}})
        with open(path + EXTENSION, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        print("{0}.{1} [OK]".format(str(index + 1), notebook))

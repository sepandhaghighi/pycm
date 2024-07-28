# -*- coding: utf-8 -*-
"""Notebook-to-HTML script."""
import os
import time
import shutil
import pycm
import nbformat
from traitlets.config import Config
from nbconvert.preprocessors import ExecutePreprocessor
from nbconvert import HTMLExporter
from art import tprint


EXAMPLES_LIST = ["Example1",
                 "Example2",
                 "Example3",
                 "Example4",
                 "Example5",
                 "Example6",
                 "Example7",
                 "Example8"]

MAIN_DOCS_LIST = ["Distance",
                "Document"]

NOTEBOOK_EXTENSION = ".ipynb"

HTML_EXTENSION = ".html"

OUTPUT_FOLDER_PATH = "doc"

DOCUMENTS_FOLDER_PATH = "Document"

if __name__ == "__main__":
    tprint("PYCM", "bulbhead")
    tprint("v{0}".format(pycm.__version__), "bulbhead")
    tprint("Notebook Convert", "amc3line")
    if OUTPUT_FOLDER_PATH in os.listdir():
        shutil.rmtree(OUTPUT_FOLDER_PATH)
    time.sleep(5)
    os.mkdir(OUTPUT_FOLDER_PATH)

    print("Documents:")
    print("Processing ...")
    c = Config()
    c.TagRemovePreprocessor.remove_cell_tags = ("html_hide",)
    c.TagRemovePreprocessor.enabled = True
    c.TemplateExporter.exclude_input_prompt = True
    c.HTMLExporter.preprocessors = ["nbconvert.preprocessors.TagRemovePreprocessor"]
    for index, notebook in enumerate(sorted(MAIN_DOCS_LIST)):
        notebook_path = os.path.join(
            DOCUMENTS_FOLDER_PATH, notebook + NOTEBOOK_EXTENSION)
        notebook_copy_path = os.path.join(
            OUTPUT_FOLDER_PATH, notebook + NOTEBOOK_EXTENSION)
        html_file_path = os.path.join(
            OUTPUT_FOLDER_PATH, notebook + HTML_EXTENSION)
        shutil.copy(notebook_path, notebook_copy_path)
        ep = ExecutePreprocessor(timeout=6000, kernel_name='python3')
        with open(notebook_copy_path, "r", encoding="utf-8") as f:
            nb = nbformat.read(f, as_version=4)
            ep.preprocess(
                nb, {
                        'metadata': {
                        'path': OUTPUT_FOLDER_PATH}})
        with open(notebook_copy_path, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        exporter = HTMLExporter(config=c)
        output_notebook = nbformat.read(notebook_copy_path, as_version=4)
        output, resources = exporter.from_notebook_node(
            output_notebook, {'metadata': {'name': notebook}})
        with open(html_file_path, "w", encoding="utf-8") as html_file:
            html_file.write(output)
        os.remove(notebook_copy_path)
        print("\t{0}.{1} [OK]".format(index + 1, notebook))

    print("\nExamples:")
    print("Processing ...")
    for index, notebook in enumerate(sorted(EXAMPLES_LIST)):
        notebook_path = os.path.join(
            DOCUMENTS_FOLDER_PATH, notebook + NOTEBOOK_EXTENSION)
        notebook_copy_path = os.path.join(
            OUTPUT_FOLDER_PATH, notebook + NOTEBOOK_EXTENSION)
        html_file_path = os.path.join(
            OUTPUT_FOLDER_PATH, notebook + HTML_EXTENSION)
        shutil.copy(notebook_path, notebook_copy_path)
        ep = ExecutePreprocessor(timeout=6000, kernel_name='python3')
        with open(notebook_copy_path, "r", encoding="utf-8") as f:
            nb = nbformat.read(f, as_version=4)
            ep.preprocess(
                nb, {
                        'metadata': {
                        'path': OUTPUT_FOLDER_PATH}})
        with open(notebook_copy_path, 'w', encoding='utf-8') as f:
            nbformat.write(nb, f)
        exporter = HTMLExporter(config=c)
        output_notebook = nbformat.read(notebook_copy_path, as_version=4)
        output, resources = exporter.from_notebook_node(
            output_notebook, {'metadata': {'name': notebook}})
        with open(html_file_path, "w", encoding="utf-8") as html_file:
            html_file.write(output)
        os.remove(notebook_copy_path)
        print("\t{0}.{1} [OK]".format(index + 1, notebook))

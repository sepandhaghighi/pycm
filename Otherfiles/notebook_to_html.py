# -*- coding: utf-8 -*-
"""Notebook-to-HTML script."""
import os
import shutil
import time
import nbformat
import pycm
from traitlets.config import Config
from nbconvert import HTMLExporter
from nbconvert.preprocessors import ExecutePreprocessor, TagRemovePreprocessor
from art import tprint


EXAMPLES_LIST = [
    "Example1", "Example2", "Example3", "Example4",
    "Example5", "Example6", "Example7", "Example8"
]

MAIN_DOCS_LIST = ["Distance", "Document"]

NOTEBOOK_EXTENSION = ".ipynb"
HTML_EXTENSION = ".html"

OUTPUT_FOLDER_PATH = "doc"
DOCUMENTS_FOLDER_PATH = "Document"


def export_notebook(notebook_name: str, use_lab_template: bool = True):
    notebook_path = os.path.join(
        DOCUMENTS_FOLDER_PATH, notebook_name + NOTEBOOK_EXTENSION
    )

    notebook_copy_path = os.path.join(
        OUTPUT_FOLDER_PATH, notebook_name + NOTEBOOK_EXTENSION
    )

    html_file_path = os.path.join(
        OUTPUT_FOLDER_PATH, notebook_name + HTML_EXTENSION
    )

    shutil.copy(notebook_path, notebook_copy_path)

    ep = ExecutePreprocessor(timeout=6000, kernel_name="python3")

    with open(notebook_copy_path, "r", encoding="utf-8") as f:
        nb = nbformat.read(f, as_version=4)

    ep.preprocess(nb, {"metadata": {"path": OUTPUT_FOLDER_PATH}})

    with open(notebook_copy_path, "w", encoding="utf-8") as f:
        nbformat.write(nb, f)

    c = Config()
    c.TagRemovePreprocessor.remove_cell_tags = ("html_hide",)
    c.TagRemovePreprocessor.enabled = True
    c.HTMLExporter.exclude_input_prompt = True
    c.HTMLExporter.preprocessors = [TagRemovePreprocessor]

    if use_lab_template:
        c.HTMLExporter.template_name = "lab"
    else:
        c.HTMLExporter.template_name = "classic"

    exporter = HTMLExporter(config=c)

    body, _ = exporter.from_notebook_node(nb)

    with open(html_file_path, "w", encoding="utf-8") as f:
        f.write(body)

    os.remove(notebook_copy_path)


if __name__ == "__main__":
    tprint("PYCM", "bulbhead")
    tprint(f"v{pycm.__version__}", "bulbhead")
    tprint("Notebook Convert", "amc3line")

    if os.path.exists(OUTPUT_FOLDER_PATH):
        shutil.rmtree(OUTPUT_FOLDER_PATH)
        time.sleep(2)

    os.mkdir(OUTPUT_FOLDER_PATH)

    print("Documents:")
    print("Processing ...")

    for index, notebook in enumerate(sorted(MAIN_DOCS_LIST)):
        export_notebook(notebook, use_lab_template=True)
        print(f"\t{index + 1}.{notebook} [OK]")

    print("\nExamples:")
    print("Processing ...")

    for index, notebook in enumerate(sorted(EXAMPLES_LIST)):
        export_notebook(notebook, use_lab_template=False)
        print(f"\t{index + 1}.{notebook} [OK]")

    print("\nDone.")

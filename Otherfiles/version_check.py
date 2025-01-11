# -*- coding: utf-8 -*-
"""Version-check script."""
import os
import sys
import codecs
Failed = 0
PYCM_VERSION = "4.2"


SETUP_ITEMS = [
    "version='{0}'",
    'https://github.com/sepandhaghighi/pycm/tarball/v{0}']
README_ITEMS = [
    "[Version {0}](https://github.com/sepandhaghighi/pycm/archive/v{0}.zip)",
    "pip install pycm=={0}"]
CHANGELOG_ITEMS = [
    "## [{0}]",
    "https://github.com/sepandhaghighi/pycm/compare/v{0}...dev",
    "[{0}]:"]
DOCUMENT_ITEMS = [
    "### Version : {0}",
    "[Version {0}](https://github.com/sepandhaghighi/pycm/archive/v{0}.zip)",
    "pip install pycm=={0}"]
HTML_ITEMS = ["Version {0}"]
PARAMS_ITEMS = ['PYCM_VERSION = "{0}"']
META_ITEMS = ['% set version = "{0}" %']
ISSUE_TEMPLATE_ITEMS = ["- PyCM {0}"]
SECURITY_ITEMS = ["| {0}           | :white_check_mark: |", "| < {0}         | :x:                |"]
FILES = {
    os.path.join("Otherfiles", "meta.yaml"): META_ITEMS,
    "setup.py": SETUP_ITEMS, "README.md": README_ITEMS,
    "CHANGELOG.md": CHANGELOG_ITEMS,
    "SECURITY.md": SECURITY_ITEMS,
    os.path.join("Document", "Document.ipynb"): DOCUMENT_ITEMS,
    os.path.join("Document", "Example1_files", "cm1.html"): HTML_ITEMS,
    os.path.join("Document", "Example1_files", "cm2.html"): HTML_ITEMS,
    os.path.join("Document", "Example1_files", "cm3.html"): HTML_ITEMS,
    os.path.join("Otherfiles", "test.html"): HTML_ITEMS,
    os.path.join("pycm", "params.py"): PARAMS_ITEMS,
    os.path.join(".github", "ISSUE_TEMPLATE", "bug_report.yml"): ISSUE_TEMPLATE_ITEMS,
}

TEST_NUMBER = len(FILES)


def print_result(failed=False):
    """
    Print final result.

    :param failed: failed flag
    :type failed: bool
    :return: None
    """
    message = "Version tag tests "
    if not failed:
        print("\n" + message + "passed!")
    else:
        print("\n" + message + "failed!")
    print("Passed : " + str(TEST_NUMBER - Failed) + "/" + str(TEST_NUMBER))


if __name__ == "__main__":
    for file_name in FILES:
        try:
            file_content = codecs.open(
                file_name, "r", "utf-8", 'ignore').read()
            for test_item in FILES[file_name]:
                if file_content.find(test_item.format(PYCM_VERSION)) == -1:
                    print("Incorrect version tag in " + file_name)
                    Failed += 1
                    break
        except Exception as e:
            Failed += 1
            print("Error in " + file_name + "\n" + "Message : " + str(e))

    if Failed == 0:
        print_result(False)
        sys.exit(0)
    else:
        print_result(True)
        sys.exit(1)

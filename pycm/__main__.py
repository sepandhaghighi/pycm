# -*- coding: utf-8 -*-
"""PyCM main."""

import doctest
import sys
from .cm import *
from .output import *
from art import tprint


if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1:
        if args[1].upper() == "TEST":
            error_flag = doctest.testfile(
                "basic_test.py",
                optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
                | doctest.IGNORE_EXCEPTION_DETAIL,
                verbose=False)[0]
            sys.exit(error_flag)
        else:
            tprint("pycm")
            tprint("V:" + PYCM_VERSION)
            pycm_help()
    else:
        tprint("pycm")
        tprint("V:" + PYCM_VERSION)
        pycm_help()

# -*- coding: utf-8 -*-

import doctest
import sys
from .pycm_obj import *
from .pycm_output import *
from art import tprint


if __name__ == "__main__":
    args = sys.argv
    if len(args) > 1:
        if args[1].upper() == "TEST":
            doctest.testfile(
                "test.py",
                optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS
                | doctest.IGNORE_EXCEPTION_DETAIL,
                verbose=False)
        else:
            tprint("pycm")
            tprint("V:" + VERSION)
            pycm_help()
    else:
        tprint("pycm")
        tprint("V:" + VERSION)
        pycm_help()

# -*- coding: utf-8 -*-

import doctest
import sys
from .pycm import *
from .functions import *


if __name__=="__main__":
    args=sys.argv
    if len(args)>1:
        if args[1].upper()=="TEST":
            doctest.testfile("test.py",optionflags=doctest.NORMALIZE_WHITESPACE | doctest.ELLIPSIS, verbose=True)
        else:
            pycm_help()
    else:
        pycm_help()




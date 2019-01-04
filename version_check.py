# -*- coding: utf-8 -*-
import os
import sys
Failed = 0
VERSION = "1.8"


SETUP_ITEMS = ["version='{0}'",'https://github.com/sepandhaghighi/pycm/tarball/v{0}']
README_ITEMS = ["[Version {0}](https://github.com/sepandhaghighi/pycm/archive/v{0}.zip)","pip install pycm=={0}","pip3 install pycm=={0}"]
CHANGELOG_ITEMS = ["## [{0}]" , "https://github.com/sepandhaghighi/pycm/compare/v{0}...HEAD"]
DOCUMENT_ITEMS = ["### Version : {0}","[Version {0}](https://github.com/sepandhaghighi/pycm/archive/v{0}.zip)","pip install pycm=={0}","pip3 install pycm=={0}"]
HTML_ITEMS = ["Version {0}"]
PARAMS_ITEMS = ['VERSION = "{0}"']
FILES = {"setup.py":SETUP_ITEMS,"README.md":README_ITEMS,"CHANGELOG.md":CHANGELOG_ITEMS,os.path.join("Document","Document.ipynb"):DOCUMENT_ITEMS,os.path.join("Document","cm1.html"):HTML_ITEMS,\
        os.path.join("Document","cm2.html"):HTML_ITEMS,os.path.join("Document","cm3.html"):HTML_ITEMS,os.path.join("Otherfiles","test.html"):HTML_ITEMS,os.path.join("pycm","pycm_param.py"):PARAMS_ITEMS}

TEST_NUMBER = len(FILES.keys())

def print_result(failed=False):
    message = "Version tag tests "
    if failed==False :
        print("\n"+message+"passed!")
    else:
        print("\n" + message + "failed!")
    print("Passed : " + str(TEST_NUMBER-Failed) + "/" + str(TEST_NUMBER))

if __name__=="__main__":
    for file_name in FILES.keys():
        try:
            file_content = open(file_name,"r",errors='ignore').read()
            for test_item in FILES[file_name]:
                if file_content.find(test_item.format(VERSION))==-1:
                    print("Incorrect version tag in "+file_name)
                    Failed +=1
                    break
        except Exception as e:
            print("Error in "+file_name+"\n"+"Message : "+str(e))

    if Failed==0 :
        print_result(False)
        sys.exit(0)
    else:
        print_result(True)
        sys.exit(1)





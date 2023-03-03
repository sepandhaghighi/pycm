@echo off
call python -m art text "Doc Run Script"
call python setup.py install
for %%f in (Document\*.ipynb) do (
echo %%f is running!
call python -m nbconvert %%f --execute --clear-output --log-level=ERROR
if ERRORLEVEL 1 (echo %%f Failed! & exit /b 0) else (echo %%f Done!)
echo --------------------------
)

copy Document\Document_files\cm1.csv Otherfiles\test.csv
copy Document\Document_files\cm1.html Otherfiles\test.html
copy Document\Document_files\cm1.obj Otherfiles\test.obj
copy Document\Document_files\cm1.pycm Otherfiles\test.pycm
copy Document\Document_files\cp.comp Otherfiles\test.comp

call python Otherfiles\version_check.py

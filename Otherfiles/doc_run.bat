@echo off
call python -m art text "Doc Run Script"
for %%f in (Document\*.ipynb) do (
echo %%f is running!
call python -m nbconvert %%f --execute --clear-output --log-level=ERROR
if ERRORLEVEL 1 (echo %%f Failed! & exit /b 0) else (echo Done!)
echo --------------------------
)

copy Document\Document_Files\cm1.csv Otherfiles\test.csv
copy Document\Document_Files\cm1.html Otherfiles\test.html
copy Document\Document_Files\cm1.obj Otherfiles\test.obj
copy Document\Document_Files\cm1.pycm Otherfiles\test.pycm
copy Document\Document_Files\cp.comp Otherfiles\test.comp

@echo off

call python -m art text "Doc 2 HTML"
call python setup.py install
if not exist "doc_html" mkdir doc_html
for %%f in (doc_html\*) do (del %%f)
copy Document\*.ipynb doc_html
cd doc_html
echo --------------------------
echo Document.ipynb is running!
call python -m nbconvert --to html_toc --execute Document.ipynb --no-prompt --TagRemovePreprocessor.enabled=True --TagRemovePreprocessor.remove_cell_tags={\"html_hide\"} --log-level=ERROR
move Document.html index.html
if ERRORLEVEL 1 (echo Document.ipynb Failed! & cd .. & exit /b 0) else (echo Document.ipynb Done!)
echo --------------------------
del Document.ipynb
for %%f in (*.ipynb) do (
echo %%f is running!
call python -m nbconvert --to html --execute %%f --no-prompt --log-level=ERROR
if ERRORLEVEL 1 (echo %%f Failed! & cd .. & exit /b 0) else (echo %%f Done!)
echo --------------------------
del %%f
)
cd ..
call python Otherfiles\version_check.py

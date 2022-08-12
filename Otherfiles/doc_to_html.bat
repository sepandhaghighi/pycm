@echo off

if not exist "doc_html" mkdir doc_html
for %%f in (doc_html\*) do (del %%f)
copy ..\Document\*.ipynb doc_html
cd doc_html
python -m nbconvert --to html_toc --execute Document.ipynb --no-prompt --TagRemovePreprocessor.enabled=True --TagRemovePreprocessor.remove_cell_tags={\"html_hide\"}
move Document.html index.html
del Document.ipynb
for %%f in (*.ipynb) do (python -m nbconvert --to html --execute %%f --no-prompt & del %%f)
cd ..

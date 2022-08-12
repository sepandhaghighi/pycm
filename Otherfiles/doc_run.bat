@echo off

for %%f in (*.ipynb) do (python -m nbconvert %%f --execute --clear-output)

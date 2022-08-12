@echo off
call python -m art text "Doc Run Script"
for %%f in (Document\*.ipynb) do (
echo %%f is running!
call python -m nbconvert %%f --execute --clear-output --log-level=ERROR
if ERRORLEVEL 1 (echo %%f Failed! & exit /b 0) else (echo Done!)
echo --------------------------
)

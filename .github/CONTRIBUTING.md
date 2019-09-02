# Contribution			

Changes and improvements are more than welcome! ❤️ Feel free to fork and open a pull request.		


Please consider the following :


1. Fork it!
2. Create your feature branch (under `dev` branch)
3. Add your new features or fix detected bugs
	- To add a new class statistic visit [here](#class-statistic)
	- To add a new overall statistic visit [here](#overall-statistic)
	- To add a new interpretation visit [here](#interpretation)
4. Add standard `docstring` to your functions/methods
5. Add tests for your functions/methods (`doctest`, `Test` folder)
6. Update `README.md` (if needed)
7. Pass all CI tests
8. Update `CHANGELOG.md`
	- Describe changes under `[Unreleased]` section
9. Update `AUTHORS.md`
	- Add your name under `# Other Contributors #` section
10. Submit a pull request into `dev` (please complete the pull request template)


## Class statistic 

1. Add new functions to `pycm_class_func.py`
2. Update `class_statistics` function in `pycm_class_func.py`
	- Define a new variable as a dictionary
	- Call statistic function and store result in this variable
	- Add this variable to `result` dictionary
3. Update `__class_stat_init__` function in `pycm_obj.py` by a new attribute
4. Update `PARAMS_DESCRIPTION` dictionary in `pycm_param.py` by a short description
5. Update `References` section in `Document.ipynb` and `README.md`
6. Add description to `Class Statistics` section in `Document.ipynb`
	- Cite reference
	- Update table of contents
	- Use `LaTeX` for formula
7. Update `PARAMS_LINK` dictionary in `pycm_param.py` by document tag (without `#`)
8. Add tests to `overall_test.py` and `function_test.py` in `TEST` folder
9. Run `autopep8.bat` (Optional, need to install latest version of `autopep8` package)



## Overall statistic 

1. Add new functions to `pycm_overall_func.py`
2. Update `overall_statistics` function in `pycm_class_func.py`
	- Call statistic function and store result in a variable
	- Add this variable to output
3. Update `__overall_stat_init__` function in `pycm_obj.py` by a new attribute
4. Update `References` section in `Document.ipynb` and `README.md`
5. Add description to `Overall Statistics` section in `Document.ipynb`
	- Cite reference
	- Update table of contents
	- Use `LaTeX` for formula
6. Update `PARAMS_LINK` dictionary in `pycm_param.py` by document tag (without `#`)
7. Add tests to `overall_test.py` and `function_test.py` in `TEST` folder
8. Run `autopep8.bat` (Optional, need to install latest version of `autopep8` package)


## Interpretation

1. Add new interpretation table as a function to `pycm_interpret.py`
2. Add a score dictionary to `pycm_param.py`
	- Example : ```PLRI_SCORE = {"Good": 4, "Fair": 3, "Poor": 2, "Negligible": 1, "None": "None"}```
3. Add a color dictionary to `BENCHMARK_COLOR` in `pycm_param.py`
	- Example : 
		```"PLRI": {
        "Negligible": "Red",
        "Poor": "Orange",
        "Fair": "Yellow",
        "Good": "Green",
        "None": "White"}		```
4. If interpretation table is for a class statistic:
	- Step 2-7 [class statistic](#class-statistic)
	- Update `CLASS_BENCHMARK_SCORE_DICT` in `pycm_param.py`
5. If interpretation table is for overall statistic:
	- Step 2-6 [overall statistic](#overall-statistic)
	- Update `OVERALL_BENCHMARK_SCORE_DICT` in `pycm_param.py`
6. Add tests to `compare_test.py` and `function_test.py` in `TEST` folder
7. Run `autopep8.bat` (Optional, need to install latest version of `autopep8` package)

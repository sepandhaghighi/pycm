
# PyCM Release Instructions

#### Last Update: 2023-11-25

1. Create the `release` branch under `dev`
2. Update all version tags
	1. `setup.py`
	2. `README.md`
	3. `Otherfiles/version_check.py`
	4. `Otherfiles/meta.yaml`
	5. `pycm/pycm_param.py`
	6. `Document/Document.ipynb`
3. Update `CHANGELOG.md`
	1. Add a new header under `Unreleased` section (Example: `## [0.1] - 2022-08-17`)
	2. Add a new compare link to the end of the file (Example: `[0.2]: https://github.com/sepandhaghighi/pycm/compare/v0.1...v0.2`)
	3. Update `dev` compare link (Example: `[Unreleased]: https://github.com/sepandhaghighi/pycm/compare/v0.2...dev`)
4. Update `.github/ISSUE_TEMPLATE/bug_report.yml`
   1. Add new version tag to `PyCM version` dropbox options
5. Update Document
	1. Run `Otherfiles/doc_run.bat`
6. Create a PR from `release` to `dev`
	1. Title: `Version x.x` (Example: `Version 0.1`)
	2. Tag all related issues
	3. Labels: `release`
	4. Set milestone
	5. Set project
	6. Wait for all CI pass
	7. Need review (**2** reviewers)
7. Merge `dev` branch into `master`
	1. `git checkout master`
	2. `git merge dev`
	3. `git push origin master`
	4. Wait for all CI pass
8. Create a new release
	1. Target branch: `master`
	2. Tag: `vx.x` (Example: `v0.1`)
	3. Title: `Version x.x` (Example: `Version 0.1`)
	4. Copy changelogs
	5. Tag all related issues
9. Bump!!
10. Close this version issues
11. Close milestone
12. Close project
13. Generate HTML files
	1. Run `Otherfiles/doc_to_html.bat`
	2. Copy `doc` folder for the next steps
14. Update website
	1. `git checkout gh-pages`
	2. Update `download.html` page
		1. Add a new section
		2. Add changelogs
	3. Update all version tags
		1. `index.html`
	4. Update size of files
		1. `index.html`
	5. Update `doc` folder (Step **12.2**)
	6. Copy `doc/Document_files/cm1.html` to `test.html`
**Please note: this repository is no longer being maintained.**

# Introduction
This package contains the chemistry functions for REINVENT.

# Installation
To install in REINVENT's environment either install from repo or use `pip install reinvent-chemistry` for the latest
official release.

# Developing
## Setup environment
You can use Conda to create an environment with all the necessary packages installed.

```
$ conda env create -f reinvent_chemistry
[...]
$ conda activate reinvent_chemistry
```

## Run tests
The tests use the `unittest` package testing framework; you can run the tests, located in the 
`unittest_reinvent` directory, by running

```
$ python main_test.py
```

# Building
- Building: `python setup.py sdist bdist_wheel`
- Upload build to test: `python -m twine upload --repository testpypi dist/*`
- Upload build: `python -m twine upload dist/*`

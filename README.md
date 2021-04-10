This package contains the chemistry functions for REINVENT.
To install in REINVENT's environment either install from repo or use `pip install reinvent-chemistry` for the latest
official release.

For development use the enclosed environment.yml


Building: python setup.py sdist bdist_wheel

Upload build to test: python -m twine upload --repository testpypi dist/*

Upload build: python -m twine upload dist/*
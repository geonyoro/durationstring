Build
-----
python -m build

Publish to TestPypi
-------------------
python -m twine upload --repository testpypi dist/*

Publish to Pypy
---------------
python -m twine upload dist/*

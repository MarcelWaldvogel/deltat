python-package:
	${RM} -f dist/*
	./setup.py sdist bdist_wheel

pypi:	python-package
	twine upload dist/*

.PHONY: python-package pypi

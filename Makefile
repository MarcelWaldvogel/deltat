python-package:
	${RM} -f dist/*
	./setup.py sdist bdist_wheel

pypi:	python-package
	twine upload dist/*

test:	tests
tests:
	nosetests3

.PHONY: python-package pypi tests test

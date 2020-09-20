.PHONY: all test

test:
	cd hlib && python -m unittest discover -v
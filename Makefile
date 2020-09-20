.PHONY: all test

# publish:

test:
	cd hlib && python -m unittest discover -v
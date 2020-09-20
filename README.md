# hlib
Simple graph library.

* [Documentation](#documentation)
* [Build](#build)
* [Publish](#publish)
* [Source Control](#source_control)

## Documentation
TBD...

## Build
```
docker build -t hlib .
```

## Publish

```
python setup.py sdist bdist_wheel
python -m twine upload dist/*
```

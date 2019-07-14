# hlib

* [Documentation](#documentation)
* [Setup](#setup)
* [Build](#build)
* [Test](#test)
* [Publish](#publish)
* [Source Control](#source_control)

## <a name="documentation"> Documentation

Supplemental algorithms and data structures.

## <a name="setup"> Setup

#### Tools

* [Git](http://git-scm.com/)

* [Python3.5](https://www.python.org/)

#### Clone Source

```
git clone git@github.com:hlatourette/hlib.git
```

#### Create Virtual Environment

```
python -m venv env
source ./env/bin/activate
pip install -r requirements.txt
```

## <a name="build"> Build

None

## <a name="test"> Test

```
cd hlib && python3 -m unittest discover -v
```

## <a name="publish"> Publish

```
python setup.py sdist bdist_wheel
python -m twine upload dist/*
```

## <a name="source_control"></a> Source Control

Each commit message consists of a **header**, a **body** and a **footer**.  The header has a special format that includes a **type**, a **scope** and a **subject**:

```
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

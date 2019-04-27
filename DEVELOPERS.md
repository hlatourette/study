# Developers

* [Setup](#setup)
* [Test](#test)
* [Deploy](#deploy)
* [Style](#style)
* [Source Control](#source_control)

## <a name="setup"> Setup

### Developer Tools

* [Git](http://git-scm.com/)

* [Python3.5](https://www.python.org/)

### Clone Source

```
git clone git@github.com:hlatourette/hlib.git
```

### Install Dependencies

```
cd <repo>
python3 -m venv env
source ./env/bin/activate
pip3 install -r requirements.txt
```

## <a name="test"> Test

### <a name="unit-tests"></a> Running the Unit Test Suite

```
cd hlib && python3 -m unittest discover -v
```


## Deploy

```
python setup.py sdist bdist_wheel
python3 -m twine upload dist/*
```

## <a name="style"></a> Style

PEP 8 Style Guide for Python (https://www.python.org/dev/peps/pep-0008/)

## <a name="source_control"></a> Source Control

Each commit message consists of a **header**, a **body** and a **footer**.  The header has a special format that includes a **type**, a **scope** and a **subject**:

```
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

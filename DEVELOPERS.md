# Developing

* [Development Setup](#setup)
* [Tests](#tests)
* [Coding Rules](#rules)
* [Commit Message Guidelines](#commits)

## <a name="setup"> Development Setup

How to set up your development environment.

### Installing Dependencies

Before you can develop for study, you must install and configure the following dependencies on your machine:

* [Git](http://git-scm.com/): The [Github Guide to Installing Git][git-setup] is a good source of information.

* [Python3.5](https://www.python.org/)

### Creating Environment

Any development must be done under a virtual environment (venv) to keep dependency consistency.

In the root of your local repository:

```
python3 -m venv env
source ./env/bin/activate
```

``` 
pip3 install -r requirements.txt
```

## <a name="tests"> Tests

### <a name="unit-tests"></a> Running the Unit Test Suite

```
python3 -m unittest discover -v
```

## <a name="rules"></a> Coding Rules

PEP 8 Style Guide for Python (https://www.python.org/dev/peps/pep-0008/)

## <a name="commits"></a> Git Commit Guidelines

### Commit Message Format

Each commit message consists of a **header**, a **body** and a **footer**.  The header has a special format that includes a **type**, a **scope** and a **subject**:

```
<type>(<scope>): <subject>
<BLANK LINE>
<body>
<BLANK LINE>
<footer>
```

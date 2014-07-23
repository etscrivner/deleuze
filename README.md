# Deleuze

A simple system for generating new python projects according to a resonable
default skeleton.

Install:

`$ pip install deleuze`

Example:

`$ deleuze new supertool`

This will generate the following project directory structure:

```
supertool
|-- bin
|    +-- supertool.py
|-- reqs
|    +-- common.txt
|    +-- dev.txt
|    +-- production.txt
|    +-- test.txt
|-- supertool
|    +-- __init__.py
|-- tests
|    +-- __init__.py
|    +-- base.py
|    +-- factories.py
|    +-- test_supertool.py
+-- README.md
+-- requirements.txt
+-- setup.py
```

This provides, what is solely in my opinion, a decent initial project structure.
The requirements files are preconfigured, reasonable testing defaults are added,
and a failing unit-test is included in supertool/tests/test_supertool.py to
remind you to start by writing some passing tests.

Next I usually spin up a new virtualenv environment for this project, install
the requirements, and get to work on something more interesting.

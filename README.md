# Python code kata template

## Prerequisites

If you're using a MacBook, your system is going to come bundled with Python3.  

## PyCharm setup

I recommend setting up the project with `PyCharm`. I also recommend always using a _virtualenv_ in case you want to install a project specific package that you don't want to have system wide.

This is not strictly necessary as everything that you need for a basic code kata, you already have. But in case you'd like to install new packages, it's good hygiene to have them isolated in a project specific virtualenv. 

See below if you don't want to create a separate virtualenv.  

1. Open the project in PyCharm.

_If you want to create a virtualenv:_ 
2a. Create a new virtualenv. For this under `Preferences > Project: Python > Python Interpreter` in the `Python Interpreter` dropdown, select to show all. Click on `Add`, then add new virtualenv using your latest Python3 system version as base interpreter.

_If you don't want to create a virtualenv:_
2b. Under `Preferences > Project: Python > Python Interpreter` choose the latest Python3 interpreter that your system has.

### Running the tests

Move your cursor to the test scope you want to run and hit `ctrl + shift + R`.

## Commandline setup

```bash
> pip3 install virtualenv
> virtualenv venv
> . ./venv/bin/activate
```

### Running the tests

Python3 should come bundled with unittest, so you should be all set. You can either run the tests from inside `PyCharm` or run them from the terminal with the following command:  

``` bash
> . ./venv/bin/activate
> python -m unittest kata_test.py
```

Exiting virtualenv with:
```bash
> deactivate
```

# Toy Package

Just an example project for setting up your python environment.

This goes along with the blog post at https://www.loganasherjones.com/2018/03/setting-up-your-python-environment/


## The Basics

Clone this repository

```bash
git clone https://github.com/loganasherjones/toy_package.git
cd toy_package
```

Make sure you have your python environment set using pyenv and pyenv-virtualenv

```bash
pyenv virtualenv 3.6.4 toy_package
pyenv local toy_package 3.6.4 2.7.14
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Run the tests on your python version:

```bash
pytest
```

Run the tests on all the python verisons:

```bash
tox
```

Uh oh! It looks like one of the tests are broken! I wonder what could be wrong...

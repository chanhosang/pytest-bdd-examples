# Python BDD

## Initial Setup

Let's setup a pipenv for this project by the following commands:
```
pipenv install

pipenv install pytest

pipenv install pytest-bdd
```

## Feature Files

The *test_durians_steps.py* is an automatically generated module, and it provides stubs for each of those steps: *Given*, *When*, and *Then* in feature file (*features/durian.feature*).

To run individual step definition modules, by giving the full path, run the following command:.
```
pipenv run python -m pytest tests/step_defs/test_durians_steps.py 
```
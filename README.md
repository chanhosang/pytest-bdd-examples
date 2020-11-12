# Python BDD

## Initial Setup

Let's setup a pipenv for this project by the following commands:
```
pipenv install

pipenv install pytest

pipenv install pytest-bdd

pipenv install selenium

pipenv install pytest-html
```

## Basic Tests

The *test_durians_steps.py* is an automatically generated module, and it provides stubs for each of those steps: *Given*, *When*, and *Then* in feature file (*features/durian.feature*).

To run all durian tests, run the following command:
```
pipenv run python -m pytest -k durian --html=reports/report.html 
```

To run individual step definition modules, by giving the full path, run the following command:.
```
pipenv run python -m pytest tests/step_defs/test_durians_steps.py 
```

## Web UI Tests

In this example, we'll use the DuckDuckGo search engine as product under test where it works like any other search engine. Just type in a phrase and get search results with links.

To run all web ui tests, run the following command:
```
pipenv run python -m pytest -k web --html=reports/report.html 
```

To run individual step definition modules, by giving the full path, run the following command:
```
pipenv run python -m pytest tests/step_defs/test_web_steps.py 
```
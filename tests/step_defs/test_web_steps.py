"""
This module contains step definitions for web.feature.
It uses Selenium WebDriver for browser interactions:
https://www.seleniumhq.org/projects/webdriver/
Setup and cleanup are handled using hooks.
For a real test automation project,
use Page Object Model or Screenplay Pattern to model web interactions.

Prerequisites:
 - Firefox must be installed.
 - geckodriver must be installed and accessible on the system path.
"""

import pytest

from pytest_bdd import scenarios, given, when, then, parsers
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from pages.result import DuckDuckGoResultPage
from pages.search import DuckDuckGoSearchPage


# Scenarios

scenarios('../features/web.feature')


# Given Steps
@given('the DuckDuckGo home page is displayed')
def ddg_home(browser):
    # browser.get(DUCKDUCKGO_HOME)
    search_page = DuckDuckGoSearchPage(browser)
    search_page.load()


# When Steps

@when(parsers.parse('the user searches for "{text}"'))
@when(parsers.parse('the user searches for the phrase:"""{text}"""'))
def search_phrase(browser, text):
    search_page = DuckDuckGoSearchPage(browser)
    
    # search_input = browser.find_element_by_name('q')
    # search_input.send_keys(text + Keys.RETURN)
    
    search_page.search(text + Keys.RETURN)


# Then Steps

@then(parsers.parse('one of the results contains "{phrase}"'))
def results_have_one(browser, phrase):
    result_page = DuckDuckGoResultPage(browser)

    # xpath = "//div[@id='links']//*[contains(text(), '%s')]" % phrase
    # results = browser.find_elements_by_xpath(xpath)
    # assert len(results) > 0
    
    results = result_page.result_link_contents(phrase)
    assert len(results) > 0
    
@then(parsers.parse('results are shown for "{phrase}"'))
def search_results(browser, phrase):    
    result_page = DuckDuckGoResultPage(browser)

    # Check search result list
    # (A more comprehensive test would check results for matching phrases)
    # (Check the list before the search phrase for correct implicit waiting)

    # links_div = browser.find_element_by_id('links')
    # assert len(links_div.find_elements_by_xpath('//div')) > 0

    titles = result_page.result_link_titles()
    matches = [t for t in titles if phrase.lower() in t.lower()]
    assert len(matches) > 0

    # Check search phrase
    # And the search result query is "phrase"

    # search_input = browser.find_element_by_name('q')
    # assert search_input.get_attribute('value') == phrase    
    assert phrase == result_page.search_input_value()
    

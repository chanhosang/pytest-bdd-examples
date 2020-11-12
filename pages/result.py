"""
This module contains DuckDuckGoResultPage,
the page object for the DuckDuckGo search result page.
"""

from selenium.webdriver.common.by import By


class DuckDuckGoResultPage:
  
  # Locators

  RESULT_LINKS = (By.CSS_SELECTOR, 'a.result__a')
  SEARCH_INPUT = (By.ID, 'search_form_input')

  # Initializer

  def __init__(self, browser):
    self.browser = browser

  # Interaction Methods
  def result_link_contents(self, phrase):
    xpath = "//div[@id='links']//*[contains(text(), '%s')]" % phrase
    results = self.browser.find_elements_by_xpath(xpath)
    return results
    
  def result_link_titles(self):
    links = self.browser.find_elements(*self.RESULT_LINKS)
    titles = [link.text for link in links]
    return titles
  
  def search_input_value(self):
    search_input = self.browser.find_element(*self.SEARCH_INPUT)
    value = search_input.get_attribute('value')
    return value

  def title(self):
    return self.browser.title

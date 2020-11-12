Feature: Durian Basket
  As a farmer,
  I want to carry durians into a bamboo basket,
  So that I don't drop them all.


  Scenario: Add durians to a bamboo basket
    Given the bamboo basket has "2" durians
    When "4" durians are added to the bamboo basket
    Then the bamboo basket contains "6" durians

  Scenario: Remove durians from a bamboo basket
    Given the bamboo basket has "8" durians
    When "3" durians are removed from the bamboo basket
    Then the bamboo basket contains "5" durians

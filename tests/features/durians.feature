@basic @durian
Feature: Durian Basket
  As a farmer,
  I want to carry durians into a bamboo basket,
  So that I don't drop them all.

  @add
  Scenario: Add durians to a bamboo basket
    Given the bamboo basket has "<initial>" durians
    When "<some>" durians are added to the bamboo basket
    Then the bamboo basket contains "<total>" durians

    Examples:
      | initial | some | total |
      | 0       | 3    | 3     |
      | 2       | 4    | 6     |
      | 5       | 5    | 10    |

  @remove
  Scenario: Remove durians from a bamboo basket
    Given the bamboo basket has "8" durians
    When "3" durians are removed from the bamboo basket
    Then the bamboo basket contains "5" durians

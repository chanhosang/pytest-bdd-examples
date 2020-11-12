from pytest_bdd import scenario, given, when, then

from durians import DurianBasket


@scenario('../features/durians.feature', 'Add durians to a bamboo basket')
def test_add():
    pass


@given("the bamboo basket has 2 durians", target_fixture="basket")
def basket():
    return DurianBasket(initial_count=2)


@when("4 durians are added to the bamboo basket")
def add_durians(basket):
    basket.add(4)


@then("the bamboo basket contains 6 durians")
def basket_has_total(basket):
    assert basket.count == 6

from pytest_bdd import scenarios, parsers, given, when, then

from durians import DurianBasket

EXTRA_TYPES = {
    'Number': int,
}

CONVERTERS = {
    'initial': int,
    'some': int,
    'total': int,
}

# scenarios('../features/durians.feature')
scenarios('../features/durians.feature', example_converters=CONVERTERS)


@given(parsers.cfparse('the bamboo basket has "{initial:Number}" durians', extra_types=EXTRA_TYPES), target_fixture="basket")
@given('the bamboo basket has "<initial>" durians')
def basket(initial):
    return DurianBasket(initial_count=initial)


@when(parsers.cfparse('"{some:Number}" durians are added to the bamboo basket', extra_types=EXTRA_TYPES))
@when('"<some>" durians are added to the bamboo basket')
def add_durians(basket, some):
    basket.add(some)


@when(parsers.cfparse('"{some:Number}" durians are removed from the bamboo basket', extra_types=EXTRA_TYPES))
@when('"<some>" durians are removed from the bamboo basket')
def remove_durians(basket, some):
    basket.remove(some)


@then(parsers.cfparse('the bamboo basket contains "{total:Number}" durians', extra_types=EXTRA_TYPES))
@then('the bamboo basket contains "<total>" durians')
def basket_has_total(basket, total):
    assert basket.count == total

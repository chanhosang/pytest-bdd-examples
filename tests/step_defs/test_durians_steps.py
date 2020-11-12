from pytest_bdd import scenarios, parsers, given, when, then

from durians import DurianBasket


scenarios('../features/durians.feature')


EXTRA_TYPES = {
    'Number': int,
}


@given(parsers.cfparse('the bamboo basket has "{initial:Number}" durians', extra_types=EXTRA_TYPES), target_fixture="basket")
def basket(initial):
    return DurianBasket(initial_count=initial)


@when(parsers.cfparse('"{some:Number}" durians are added to the bamboo basket', extra_types=EXTRA_TYPES))
def add_durians(basket, some):
    basket.add(some)


@when(parsers.cfparse('"{some:Number}" durians are removed from the bamboo basket', extra_types=EXTRA_TYPES))
def remove_durians(basket, some):
    basket.remove(some)


@then(parsers.cfparse('the bamboo basket contains "{total:Number}" durians', extra_types=EXTRA_TYPES))
def basket_has_total(basket, total):
    assert basket.count == total

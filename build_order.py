"""
I play victoria 3. The early part of the game appears to be about achieving the fastest exponential growth possible.
Mostly this means building construction centres and supporting buildings to avoid going bankrupt.
I would like a program which takes in the current state of the nation and outputs an ideal build order given some
assumptions.

I choose to maximize (rate of construction)/(rate of expenditure)

Factors not currently included in calculation in importance order:
- Iron usage and production rates are wrong
- Construction uses resources other than iron
- Iron mines use resources too
- Iron is used by things other than construction
- Which provence a building is built in

"""

import pytest

# This should live in a json file
BUILDINGS = {
    "iron mine": {"cost": 150, "iron production": 20},
    "construction site": {"cost": 50, "iron production": 100},
}

initial_buildings = {"iron mine": 10, "construction site": 10}
IRON_BASE_PRICE = 40


def score():
    """
    I currently define the score of the situation to be the (rate of construction)/(rate of government expenditure)
    :return:
    """


def price_of_iron(supply, demand):
    assert supply >= 0
    assert demand >= 0

    if supply == 0 and demand == 0:
        price_modifier = 1
    elif supply == 0:
        price_modifier = 1.75
    elif demand == 0:
        price_modifier = 0.25
    else:
        price_modifier = 1 - 0.75 * (supply - demand) / min(supply, demand)
        price_modifier = min(1.75, price_modifier)
        price_modifier = max(0.25, price_modifier)
    return IRON_BASE_PRICE * price_modifier


def test_price_of_iron():
    assert price_of_iron(0, 0) == IRON_BASE_PRICE
    assert price_of_iron(1, 0) == 0.25 * IRON_BASE_PRICE
    assert price_of_iron(0, 1) == 1.75 * IRON_BASE_PRICE
    assert price_of_iron(1, 1) == IRON_BASE_PRICE

    assert price_of_iron(10, 0) == 0.25 * IRON_BASE_PRICE
    assert price_of_iron(10, 5) == 0.25 * IRON_BASE_PRICE
    # assert price_of_iron(10, 9) == IRON_BASE_PRICE
    assert price_of_iron(10, 10) == IRON_BASE_PRICE
    # assert price_of_iron(10, 11) == IRON_BASE_PRICE
    assert price_of_iron(10, 20) == 1.75 * IRON_BASE_PRICE
    assert price_of_iron(10, 999) == 1.75 * IRON_BASE_PRICE

import pytest

from shoppingbasket import ShoppingBasket
from item import Item

@pytest.fixture
def shopping_basket():
    return ShoppingBasket()

@pytest.fixture
def apple_item():
    return Item("Apple", "100g", 2.20, stock=9)

@pytest.fixture
def multiple_items(apple_item):
    return [
        apple_item,
        Item("Banana", "80g", 1.20),
        Item("Cherry", "30g", 0.90),
    ]

#
def test_add_item(shopping_basket, apple_item):
    shopping_basket.addItem(apple_item)
    assert apple_item in shopping_basket.items

def test_add_item_affect_stock(shopping_basket, apple_item):
    shopping_basket.addItem(apple_item)
    assert apple_item in shopping_basket.items
    assert apple_item.stock == 8

def test_add_over_stock_item(shopping_basket, apple_item):
    with pytest.raises(ValueError):
        shopping_basket.addItem(apple_item, quantity=100)

#
def test_add_multiple_items(shopping_basket, multiple_items):
    for i in multiple_items:
        shopping_basket.addItem(i)

    assert all(i in shopping_basket.items for i in multiple_items)

#
def test_remove_item(shopping_basket, apple_item, multiple_items):
    for i in multiple_items:
        shopping_basket.addItem(i)

    initially_in = apple_item in shopping_basket.items

    shopping_basket.remove_item(apple_item)

    now_gone = apple_item not in shopping_basket.items

    assert initially_in and now_gone

def test_remove_item_affects_stock(shopping_basket, apple_item, multiple_items):
    for i in multiple_items:
        shopping_basket.addItem(i)

    initially_in = apple_item in shopping_basket.items
    assert apple_item.stock == 8

    shopping_basket.remove_item(apple_item)

    now_gone = apple_item not in shopping_basket.items

    assert initially_in and now_gone
    assert apple_item.stock == 9

#
def test_update_item(shopping_basket, apple_item):
    shopping_basket.addItem(apple_item)

    shopping_basket.updateItem(apple_item, quantity=17)

    assert shopping_basket.items[apple_item] == 17

#
def test_view(shopping_basket, multiple_items):
    # I guess that if this runs then all is well

    for i in multiple_items:
        shopping_basket.addItem(i)

    shopping_basket.view()

    assert True

#
def test_get_total_cost(shopping_basket, multiple_items):
    for i in multiple_items:
        shopping_basket.addItem(i)

    assert shopping_basket.get_total_cost() == 4.30

#
def test_is_empty(shopping_basket):
    assert shopping_basket.is_empty()

#
def test_reset(shopping_basket, multiple_items):
    for i in multiple_items:
        shopping_basket.addItem(i)

    shopping_basket.reset()
    assert shopping_basket.is_empty()


from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    dish = Dish("Test Dish", 10.99)
    dish2 = Dish("Test Dish", 10.99)
    dish3 = Dish("Test Chinese Dish", 10.99)

    assert dish == dish2
    assert dish != dish3

    assert dish.name == "Test Dish"
    assert dish.price == 10.99
    assert dish.recipe == {}

    with pytest.raises(ValueError):
        Dish("Test Dish", -5)
    with pytest.raises(TypeError):
        Dish("Test Dish", "10.99")

    assert dish.__hash__() == dish2.__hash__()
    assert dish.__hash__() != dish3.__hash__()

    assert dish.__repr__() == "Dish('Test Dish', R$10.99)"

    ingredient1 = Ingredient("Ingredient 1")
    ingredient2 = Ingredient("Ingredient 2")
    dish.add_ingredient_dependency(ingredient1, 2)
    dish.add_ingredient_dependency(ingredient2, 1)
    assert ingredient1 in dish.recipe
    assert ingredient2 in dish.recipe
    assert dish.recipe[ingredient1] == 2
    assert dish.recipe[ingredient2] == 1

    ingredient1.restrictions = ["A", "B"]
    ingredient3 = Ingredient("Ingredient 3")
    ingredient3.restrictions = ["B", "C"]
    dish.add_ingredient_dependency(ingredient3, 3)
    restrictions = dish.get_restrictions()
    assert restrictions == {"A", "B", "C"}

    ingredients = dish.get_ingredients()
    assert ingredients == {ingredient1, ingredient2, ingredient3}

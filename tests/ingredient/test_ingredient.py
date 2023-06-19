from src.models.ingredient import Ingredient, Restriction
# from tests.ingredients import INGREDIENTS


# Req 1
def test_ingredient():
    ingredient = Ingredient("queijo provolone")
    ingredient2 = Ingredient("queijo provolone")
    ingredient3 = Ingredient("massa de raviole")

    assert ingredient.__hash__() == ingredient.__hash__()
    assert ingredient.__hash__() != ingredient3.__hash__()
    assert ingredient == ingredient2
    assert ingredient != ingredient3
    assert ingredient.__repr__() == "Ingredient('queijo provolone')"
    assert ingredient.name == "queijo provolone"
    assert ingredient.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }

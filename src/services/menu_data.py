import csv
from models.dish import Dish
from models.ingredient import Ingredient


class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.source_path = source_path

        with open(self.source_path, "r") as file:
            reader = csv.DictReader(file)
            csv_content = list(reader)

            for dish in csv_content:
                current_dish = Dish(dish["dish"], float(dish["price"]))

                if current_dish in self.dishes:
                    current_dish = next(
                        d for d in self.dishes if d == current_dish
                    )

                else:
                    self.dishes.add(current_dish)

                current_dish.add_ingredient_dependency(
                    Ingredient(dish["ingredient"]), int(dish["recipe_amount"])
                )

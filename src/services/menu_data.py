import csv
from models.dish import Dish
from models.ingredient import Ingredient

class MenuData:
    def __init__(self, source_path: str) -> None:
        self.dishes = set()
        self.source_path = source_path

    # def get_dishes(self):
        with open(self.source_path, 'r') as file:
            reader = csv.DictReader(file)
            csv_content = list(reader)
            # print(csv_content, 'AAAAAAAAAAAAA')
            for dish in csv_content:
                # print(dish, 'CURRENT DISH')
                current_dish = Dish(dish['dish'], float(dish['price']))
                self.dishes.add(current_dish)
                
                ingredient = Ingredient(dish['ingredient'])
                current_dish.add_ingredient_dependency(ingredient, int(dish['recipe_amount']))
            
            return self.dishes

meu_menu = MenuData('data/menu_base_data.csv')
meu_menu.get_dishes()
print(meu_menu.dishes)
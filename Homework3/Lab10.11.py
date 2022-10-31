#JenniferChu
#1873159

class FoodItem:
    def __init__(self, name="None", fat=0.0, carbs=0.0, protein=0.0, num_servings: object = 0.0):
        self.name = name
        self.protein = protein
        self.carbs = carbs
        self.fat = fat
        self.num_servings = num_servings

    def get_calories(self, num_servings) -> object:
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * num_servings
        return calories

    def print_info(self) -> object:
        print('Nutritional information per serving of {}:'.format(self.name))
        print(f'   Fat: {self.fat:.2f} g')
        print(f'   Carbohydrates: {self.carbs:.2f} g')
        print(f'   Protein: {self.protein:.2f} g')


if __name__ == "__main__":
    name = input()
    fat = float(input())
    carbs = float(input())
    protein = float(input())
    num_servings = float(input())

    food1: FoodItem = FoodItem()
    food1.print_info()
    print(f'Number of calories for {num_servings:.2f} serving(s): {food1.get_calories(num_servings):.2f}\n')

    food2: FoodItem = FoodItem(name, fat, carbs, protein, num_servings)
    food2.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(num_servings, food2.get_calories(num_servings)))


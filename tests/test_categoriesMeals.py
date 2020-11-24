import unittest

from src.sample.categoriesMeals import MealCategoris


class MealNameTest(unittest.TestCase):

    def setUp(self):
        self.temp = MealCategoris()

    def test_meal_categories(self):
        categories = ['Beef', 'Chicken', 'Dessert', 'Lamb', 'Miscellaneous', 'Pasta', 'Pork', 'Seafood', 'Side', 'Starter', 'Vegan', 'Vegetarian', 'Breakfast', 'Goat']
        self.assertEqual(self.temp.get_meal_categories(),categories)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()

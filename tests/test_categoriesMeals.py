import unittest

from src.sample.categoriesMeals import MealCategoris


class MealCategoriesTest(unittest.TestCase):

    def setUp(self):
        self.temp = MealCategoris()

    def test_meal_categories(self):
        categories = ['Beef', 'Chicken', 'Dessert', 'Lamb', 'Miscellaneous', 'Pasta', 'Pork', 'Seafood', 'Side',
                      'Starter', 'Vegan', 'Vegetarian', 'Breakfast', 'Goat']
        self.assertEqual(self.temp.get_meal_categories(), categories)

    def test_meals_in_category(self):
        meals = ['Baked salmon with fennel & tomatoes', 'Cajun spiced fish tacos', 'Escovitch Fish', 'Fish pie',
                 'Fish Stew with Rouille', 'Garides Saganaki', 'Honey Teriyaki Salmon', 'Kedgeree', 'Kung Po Prawns',
                 'Laksa King Prawn Noodles', 'Mediterranean Pasta Salad', 'Recheado Masala Fish',
                 'Salmon Avocado Salad', 'Salmon Prawn Risotto', 'Saltfish and Ackee', 'Seafood fideuà',
                 'Shrimp Chow Fun', 'Sledz w Oleju (Polish Herrings)', 'Three Fish Pie', 'Tuna and Egg Briks',
                 'Tuna Nicoise']
        self.assertEqual(self.temp.get_meals_in_category("Seafood"), meals)

    def test_meals_in_category_not_found(self):
        self.assertEqual(self.temp.get_meals_in_category("none"), None)

    def test_meals_in_categorya_type_error(self):
        self.assertRaisesRegex(TypeError, "You_use_str_type", self.temp.get_meals_in_category, False)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()

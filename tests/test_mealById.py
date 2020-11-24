import unittest

from src.sample.mealById import MealById


class MealNameByIdTest(unittest.TestCase):

    def setUp(self):
        self.temp = MealById()

    def test_meal_name_By_id(self):
        mealById = self.temp.get_meal_name_by_id("52772")
        self.assertEqual(mealById[0]['strMeal'],"Teriyaki Chicken Casserole")

    def test_meal_name_by_id_errorType(self):
        self.assertRaisesRegex(TypeError, 'not str number', self.temp.get_meal_name_by_id, 1)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()

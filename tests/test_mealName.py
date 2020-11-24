import unittest

from src.sample.mealName import MealName


class MealNameTest(unittest.TestCase):

    def setUp(self):
        self.temp = MealName()

    def test_meal_instruction(self):
        instruction = self.temp.get_meal_instruction("Polish Pancakes")
        self.assertEqual(instruction[0]['strInstructions'],
                         "Add flour, eggs, milk, water, and salt in a large bowl then mix with a hand mixer until you have a smooth, lump-free batter.\r\nAt this point, mix in the butter or the vegetable oil. Alternatively, you can use them to grease the pan before frying each pancake.\r\nHeat a non-stick pan over medium heat, then pour in the batter, swirling the pan to help it spread.\r\nWhen the pancake starts pulling away a bit from the sides, and the top is no longer wet, flip it and cook shortly on the other side as well.\r\nTransfer to a plate. Cook the remaining batter until all used up.\r\nServe warm, with the filling of your choice.")

    def test_meal_typeError(self):
        self.assertRaises(TypeError, self.temp.get_meal_instruction, True)

    def test_meal_yt_link(self):
        instruction = self.temp.get_yt_link("Fish")
        self.assertEqual(instruction, "https://www.youtube.com/watch?v=2sX4fCgg-UI")

    def test_meal_yt_link_typeError(self):
        self.assertRaisesRegex(TypeError, 'not type string', self.temp.get_yt_link, 1)

    def test_ingredients_to_meal(self):
        ingredients = self.temp.get_ingredients_to_meal("Pancakes")
        self.assertEqual(ingredients, ['Flour', 'Eggs', 'Milk', 'Sunflower Oil', 'Sugar', 'Raspberries', 'Blueberries'])

    def test_ingredients_to_meal_not_found_meal(self):
        ingredients = self.temp.get_ingredients_to_meal("abcdefg")
        self.assertEqual(ingredients, None)

    def test_measure_to_prepare_meal(self):
        measures = self.temp.get_measure_to_prepare_meal("Arrabiata")
        self.assertEqual(measures,
                         ['1 pound', '1/4 cup', '3 cloves', '1 tin ', '1/2 teaspoon', '1/2 teaspoon', '6 leaves',
                          'spinkling'])

    def test_measure_to_prepare_meal_not_found_meal(self):
        measures = self.temp.get_measure_to_prepare_meal("abcdefgh")
        self.assertEqual(measures, None)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()

import unittest

from src.sample.mealName import MealName


class MealNameTest(unittest.TestCase):

    def setUp(self):
        self.temp = MealName()

    def test_meal_instruction(self):
        instruction = self.temp.get_meal_instruction("Polish Pancakes")
        self.assertEqual(instruction[0]['strInstructions'], "Add flour, eggs, milk, water, and salt in a large bowl then mix with a hand mixer until you have a smooth, lump-free batter.\r\nAt this point, mix in the butter or the vegetable oil. Alternatively, you can use them to grease the pan before frying each pancake.\r\nHeat a non-stick pan over medium heat, then pour in the batter, swirling the pan to help it spread.\r\nWhen the pancake starts pulling away a bit from the sides, and the top is no longer wet, flip it and cook shortly on the other side as well.\r\nTransfer to a plate. Cook the remaining batter until all used up.\r\nServe warm, with the filling of your choice.")

    def tearDown(self):
        self.temp = None

if __name__ == '__main__':
    unittest.main()
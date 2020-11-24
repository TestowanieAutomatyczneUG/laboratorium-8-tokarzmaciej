import unittest

from src.sample.mealsStartFromFirstLetter import MealsFromFirstLetter


class AreaMealsTest(unittest.TestCase):

    def setUp(self):
        self.temp = MealsFromFirstLetter()

    def test_meals_from_first_letter(self):
        meals = ['Apple Frangipan Tart', 'Apple & Blackberry Crumble']
        self.assertEqual(self.temp.get_meals_from_first_letter("a"), meals)

    def test_meals_from_first_letter_exception(self):
        self.assertRaisesRegex(Exception, 'You_have_to_choose_single_letter', self.temp.get_meals_from_first_letter, "abc")

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()

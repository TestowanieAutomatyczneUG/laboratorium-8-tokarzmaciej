import unittest

from src.sample.areaMeals import AreaMeals


class AreaMealsTest(unittest.TestCase):

    def setUp(self):
        self.temp = AreaMeals()

    def test_areas(self):
        areas = ['American', 'British', 'Canadian', 'Chinese', 'Dutch', 'Egyptian', 'French', 'Greek', 'Indian',
                 'Irish', 'Italian', 'Jamaican', 'Japanese', 'Kenyan', 'Malaysian', 'Mexican', 'Moroccan', 'Polish',
                 'Russian', 'Spanish', 'Thai', 'Tunisian', 'Turkish', 'Unknown', 'Vietnamese']
        self.assertEqual(self.temp.get_area(), areas)

    def test_meals_in_area(self):
        meals = ['BeaverTails', 'Breakfast Potatoes', 'Canadian Butter Tarts', 'Montreal Smoked Meat', 'Nanaimo Bars',
                 'Pate Chinois', 'Pouding chomeur', 'Poutine', 'Rappie Pie', 'Split Pea Soup', 'Sugar Pie', 'Timbits',
                 'Tourtiere']
        self.assertEqual(self.temp.get_meals_in_area("Canadian"), meals)

    def test_meals_in_area_not_found(self):
        self.assertEqual(self.temp.get_meals_in_area("abcdef"), None)

    def test_meals_in_area_type_error(self):
        self.assertRaisesRegex(TypeError, "not str", self.temp.get_meals_in_area, 1)

    def tearDown(self):
        self.temp = None


if __name__ == '__main__':
    unittest.main()

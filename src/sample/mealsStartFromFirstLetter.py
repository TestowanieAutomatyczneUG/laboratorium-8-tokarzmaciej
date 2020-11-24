import requests


class MealsFromFirstLetter:
    def get_meals_from_first_letter(self, firstLetter):
        if type(firstLetter) == str and len(firstLetter) == 1:
            categories = requests.get('https://www.themealdb.com/api/json/v1/1/search.php?f=' + firstLetter)
            result = []
            for category in categories.json()['meals']:
                result.append(category['strMeal'])
            return result
        else:
            raise Exception('You_have_to_choose_single_letter')


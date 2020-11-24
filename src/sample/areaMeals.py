import requests


class AreaMeals:
    def get_meals_in_area(self, areaName):
        if type(areaName) == str:
            result = requests.get('https://www.themealdb.com/api/json/v1/1/filter.php?a=' + areaName)
            meals = []
            if result.json()['meals'] != None:
                for category in result.json()['meals']:
                    meals.append(category['strMeal'])
                return meals
            else:
                return None
        else:
            raise TypeError("not str")

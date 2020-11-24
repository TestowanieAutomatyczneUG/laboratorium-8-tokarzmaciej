import requests


class MealById:
    def get_meal_name_by_id(self, id):
        meals = requests.get('https://www.themealdb.com/api/json/v1/1/lookup.php?i=' + id)
        return meals.json()['meals']

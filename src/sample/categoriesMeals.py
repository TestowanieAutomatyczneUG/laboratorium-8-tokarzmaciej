import requests

class MealCategoris:
    def get_meal_categories(self):
        categories = requests.get('https://www.themealdb.com/api/json/v1/1/categories.php')
        result = []
        for category in categories.json()['categories']:
            result.append(category['strCategory'])
        return result


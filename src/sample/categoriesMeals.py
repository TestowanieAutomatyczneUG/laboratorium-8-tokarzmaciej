import requests


class MealCategoris:
    def get_meal_categories(self):
        categories = requests.get('https://www.themealdb.com/api/json/v1/1/categories.php')
        result = []
        for category in categories.json()['categories']:
            result.append(category['strCategory'])
        return result

    def get_meals_in_category(self, categoryName):
        if type(categoryName) == str:
            result = requests.get('https://www.themealdb.com/api/json/v1/1/filter.php?c=' + categoryName)
            meals = []
            if result.json()['meals'] != None:
                for category in result.json()['meals']:
                    meals.append(category['strMeal'])
                return meals
            else:
                return None
        else:
            raise TypeError("You_use_str_type")

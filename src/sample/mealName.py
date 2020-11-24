import requests


class MealName:
    def get_meal_instruction(self, name):
        if type(name) == str:
            meal = requests.get('https://www.themealdb.com/api/json/v1/1/search.php?s=' + name)
            return meal.json()['meals']
        else:
            raise TypeError('not type string')

    def get_yt_link(self, name):
        if type(name) == str:
            link = requests.get('https://www.themealdb.com/api/json/v1/1/search.php?s=' + name)
            return link.json()['meals'][0]['strYoutube']
        else:
            raise TypeError('not type string')

    def get_ingredients_to_meal(self, name):
        meals = requests.get('https://www.themealdb.com/api/json/v1/1/search.php?s=' + name)
        if meals.json()['meals'] is not None:
            ingredients = []
            for i in range(1, 20, 1):
                ingredient = "strIngredient" + str(i)
                if meals.json()['meals'][0][ingredient] != 'null' and meals.json()['meals'][0][ingredient] != "":
                    ingredients.append(meals.json()['meals'][0][ingredient])
            return ingredients
        else:
            return None

    def get_measure_to_prepare_meal(self, name):
        meals = requests.get('https://www.themealdb.com/api/json/v1/1/search.php?s=' + name)
        measures = []
        for i in range(1, 20, 1):
            measure = "strMeasure" + str(i)
            if meals.json()['meals'][0][measure] != 'null' and meals.json()['meals'][0][measure] != "" and meals.json()['meals'][0][measure] != None:
                measures.append(meals.json()['meals'][0][measure])
        return measures


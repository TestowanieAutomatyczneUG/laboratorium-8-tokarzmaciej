import requests


class MealName:
    def get_meal_instruction(self, name):
        if type(name) == str:
            meal = requests.get('https://www.themealdb.com/api/json/v1/1/search.php?s=' + name)
            return meal.json()['meals']
        else:
            raise TypeError('not type string')

    def get_yt_link(self, name):
        link = requests.get('https://www.themealdb.com/api/json/v1/1/search.php?s=' + name)
        return link.json()['meals'][0]['strYoutube']

class Dessert:
    def __init__(self, name='', calories=0):
        self.name = name
        self.calories = calories

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name

    @property
    def calories(self):
        return self.__calories

    @calories.setter
    def calories(self, calories):
        self.__calories = calories

    def is_healthy(self):
        try:
            return float(self.calories) < 200
        except (TypeError, ValueError):
            return False

    def is_delicious(self):
        return True


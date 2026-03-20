class Dessert:
    
    def __init__(self, name = '', calories = 0):
        self.name = name
        self.calories = calories

    @staticmethod
    def type_name(name):
        return isinstance(name, str)
    
    @staticmethod
    def validete_calories(calories):
        if not isinstance(calories, (int, float)):
            print('Калории должны быть числом')
            return False
        if calories < 0:
            print('Калории не могут быть отрицательным числом')
            return False
        return True
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not Dessert.type_name(name):
            print('Название десерта должно быть строкой')
            return False
        self._name = name

    @property
    def calories(self):
        return self._calories
    
    @calories.setter
    def calories(self, calories):
        self.validete_calories(calories)
        self._calories = calories

    def is_healthy(self):
        try:
            return float(self.calories) < 200
        except (TypeError, ValueError):
            return False

    def is_delicious(self):
        return True

class JellyBean(Dessert):
    def __init__(self, name='', calories=0, flavor=''):
        super().__init__(name, calories)
        self.flavor = flavor

    @property
    def flavor(self):
        return self.__flavor

    @flavor.setter
    def flavor(self, flavor):
        self.__flavor = flavor

    def is_delicious(self):
        if self.flavor == 'black licorice':
            return False
        return super().is_delicious()



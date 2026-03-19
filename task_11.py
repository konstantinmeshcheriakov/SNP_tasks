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
            raise TypeError('Калории должны быть числом')
        if calories < 0:
            raise ValueError('Калории не могут быть отрицательным числом')
        return True
    
    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not Dessert.type_name(name):
            raise ValueError('Название десерта должно быть строкой')
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

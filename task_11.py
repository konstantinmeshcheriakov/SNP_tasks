# Реализуйте класс Dessert c геттерами и сеттерами name и calories, конструктором,
# принимающим на вход name и calories (не обязательные параметры), а также двумя
# методами is_healthy (возвращает true при условии калорийности десерта менее
# 200) и is_delicious (возвращает true для всех десертов).
class Dessert:
    
    def __init__(self, name = '', calories = 0):
        self.name = name
        self.calories = calories
        self.is_healthy(self.calories)
        self.is_delicious()

    @classmethod
    def type_name(cls, name):
        if type(name) != str:
            print('Название десерта должно быть строкой')
        
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.type_name(name)
        self.__name = name

    @property
    def calories(self):
        return self.__calories
    
    @calories.setter
    def calories(self, calories):
        self.__calories = calories

    def is_healthy(self, __calories):
        if self.__calories < 200:
            return True

    def is_delicious(self):
        return True
    
d = Dessert(1, 150)
d1 = Dessert('cake', 200)
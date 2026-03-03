class Dessert:
    
    def __init__(self, name = '', calories = 0):
        self.name = name
        self.calories = calories

    @classmethod
    def type_name(cls, name):
        if type(name) == str:
            print(True)
        else:
            print('Название десерта должно быть строкой')
        
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name):
        self.__name = name
        self.is_delicious(self.__name)

    @property
    def calories(self):
        return self.__calories
    
    @calories.setter
    def calories(self, calories):
        self.__calories = calories
        self.is_healthy(self.__calories)

    def is_healthy(self, __calories):
        return self.__calories < 200

    def is_delicious(self, __name):
        self.type_name(__name)

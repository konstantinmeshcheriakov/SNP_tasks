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
        return self._name

    @name.setter
    def name(self, name):
        self._name = name
        self.is_delicious(self._name)

    @property
    def calories(self):
        return self._calories
    
    @calories.setter
    def calories(self, calories):
        self._calories = calories
        self.is_healthy(self._calories)

    def is_healthy(self, _calories):
        return self._calories < 200

    def is_delicious(self, _name):
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

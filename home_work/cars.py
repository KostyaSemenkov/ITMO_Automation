class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def started(self):
        return 'Автомобиль заведен'

    def stoped(self):
        return 'Автомобиль заглушен'

    def year1(self):
        return self.year

    def type1(self):
        return self.type

    def color1(self):
        return self.color


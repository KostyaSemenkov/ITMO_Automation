class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def started(self):
        return 'Автомобиль заведен'

    def stoped(self):
        return 'Автомобиль заглушен'

    def year1(self, year2):
        self.year = year2

    def type1(self, type2):
        self.type = type2

    def color1(self, color2):
        self.color = color2

print('lemur')
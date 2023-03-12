class Rentangle:

    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def square(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2


ren1 = Rentangle(2, 9)
ren2 = Rentangle(7, 5)
ren3 = Rentangle(6, 5)
print(ren1.square())
print(ren2.square())
print(ren3.square())
print(ren1.perimeter())
print(ren2.perimeter())
print(ren2.perimeter())


class Math:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self):
        return self.a + self.b

    def multiplication(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b

    def subtraction(self):
        return self.a - self.b


calc = Math(6, 3)
print(calc.addition())
print(calc.multiplication())
print(calc.division())
print(calc.subtraction())


class Demoqa:

    def __init__(self, text_box, type='Кнопка', locator=''):
        self.text_box = text_box
        self.type = type
        self.locator = locator

    def click(self):
        return f'Клик по кнопке {self.text_box}'


check_box = Demoqa('Check box')
print(check_box.click())
radio_button = Demoqa('Radio Button')
print(radio_button.click())
web_tables = Demoqa('Web Tables')
print(web_tables.click())
buttons = Demoqa('Buttons')
print(buttons.click())
links = Demoqa('Links')
print(links.click())
broken_links_images = Demoqa('Broken Links - Images')
print(broken_links_images.click())
upload_and_download = Demoqa('Upload and Download')
print(upload_and_download.click())
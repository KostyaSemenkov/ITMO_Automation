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
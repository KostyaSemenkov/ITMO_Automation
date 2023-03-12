from task_9_checks import Check
class Input(Check):
    def __init__(self, Loc, text):
        super().__init__(Loc)
        self.Loc = Loc
        self.text = text
search = Input('loca', 'text')
print(search.Loc, search.text)
class Button(Check):
    def __init__(self, Loc, text):
        super().__init__(Loc)
        self.Loc = Loc
        self.text = text

class Title(Check):
    def __init__(self, Loc, text):
        super().__init__(Loc)
        self.Loc = Loc
        self.text = text
class Link(Check):
    def __init__(self, Loc, text):
        super().__init__(Loc)
        self.Loc = Loc
        self.text = text
buttons = Button('loca1', 'text1')
print(buttons.Loc, buttons.text)
titles = Title('loca2', 'text2')
print(titles.Loc, titles.text)
links = Link('loca3', 'text3')
print(links.Loc, links.text)
print(buttons.check_text())
print(titles.check_text())
print(links.check_text())
print(search.check_text())





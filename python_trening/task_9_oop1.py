class Input:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text
class Button:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text
class Title:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text
class Link:
    def __init__(self, loc, text):
        self.loc = loc
        self.text = text
search = Input('Spain', 'Hola')
print (search.loc, search.text)
search1 = Button('Spain1', 'Hola1')
print (search1.loc, search1.text)
search2 = Title('Spain2', 'Hola2')
print (search2.loc, search2.text)
search3 = Link('Spain3', 'Hola3')
print (search3.loc, search3.text)
class Soda:
    def __init__(self, add):
        self.add = add

    def show_my_drink(self):
        if len(self.add) > 0:
            print('Газировка и', self.add)
        else:
            print('Обычная газировка')


gaz1 = Soda('Кокос')
gaz2 = Soda('')
gaz1.show_my_drink()
gaz2.show_my_drink()

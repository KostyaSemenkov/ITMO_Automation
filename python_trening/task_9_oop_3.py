class Soda:
    def __init__(self, dob):
        self.dob = dob
    def show_my_drink(self):
        if self.dob == '':
            print('Обычная газировка')
        else:
            print(f'Газировка и {self.dob}')



dobavka = Soda('мясо')
nedobavka = Soda('')
dobavka.show_my_drink()
nedobavka.show_my_drink()

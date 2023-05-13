class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'Название ресторана: {self.restaurant_name} \nТип кухни: {self.cuisine_type}')

    def open_restaurant(self):
        print('Ресторан открыт!')


rest1 = Restaurant('Amo Resto-', 'Европейская')
rest2 = Restaurant('Glitch Door', 'Азатская')
rest3 = Restaurant('Sea Room', 'Морская')

rest1.describe_restaurant()
print('')
rest2.describe_restaurant()
print('')
rest3.describe_restaurant()

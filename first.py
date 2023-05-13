class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f'Название ресторана: {self.restaurant_name}. \nТип кухни: {self.cuisine_type}')

    def open_restaurant(self):
        print('Ресторан открыт!')


newRestaurant = Restaurant('Свобода', 'Русская')
print(newRestaurant.restaurant_name)
print(newRestaurant.cuisine_type)
print('')
newRestaurant.describe_restaurant()
print('')
newRestaurant.open_restaurant()

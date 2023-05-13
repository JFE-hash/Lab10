class Restaurant:
    def __init__(self, restaurant_name, cuisine_type, rating):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.old_rating = rating

    def describe_restaurant(self):
        print(f'Название ресторана: {self.restaurant_name} \nТип кухни: {self.cuisine_type}')

    def open_restaurant(self):
        print('Ресторан открыт!')

    def rating_update(self, new_rating):
        self.old_rating = new_rating
        print(f'Рейтинг {self.restaurant_name} изменился на {self.old_rating}')
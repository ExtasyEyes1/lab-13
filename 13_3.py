class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = 5
    def describe_restaurant(self):
        print(f"Название: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
        print(f"Рейтинг: {self.rating}")
    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} открыт!")
    def update_rating(self, new_rating):
        self.rating = new_rating
        print(f"Рейтинг ресторана '{self.restaurant_name}' обновлён до {self.rating}")
newRestaurant = Restaurant("Уют", "Европейская")
newRestaurant.describe_restaurant()
print()
newRestaurant.update_rating(9)
newRestaurant.describe_restaurant()
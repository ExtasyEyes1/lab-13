class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
    def describe_restaurant(self):
        print(f"Название: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} открыт!")
r1 = Restaurant("Токио", "Японская")
r2 = Restaurant("Пицца Рим", "Итальянская")
r3 = Restaurant("Самса", "Узбекская")
for r in [r1, r2, r3]:
    r.describe_restaurant()
    r.open_restaurant()
    print()
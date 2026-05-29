class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.rating = 5 #13.3 рейтинг
    def describe_restaurant(self):
        print(f"Название: {self.restaurant_name}")
        print(f"Тип кухни: {self.cuisine_type}")
    def open_restaurant(self):
        print(f"Ресторан {self.restaurant_name} открыт!")
    #13.3 Функция Обновления рейтинга
    def update_rating(self, new_rating):
        self.rating = new_rating
        print(f"Рейтинг ресторана '{self.restaurant_name}' обновлён до {self.rating}")
newRestaurant = Restaurant("Уют", "Европейская")
print(newRestaurant.restaurant_name)
print(newRestaurant.cuisine_type)
print()
newRestaurant.describe_restaurant()
newRestaurant.open_restaurant()
print()
#13.2 три ресторана
r1 = Restaurant("Токио", "Японская")
r2 = Restaurant("Пицца Рим", "Итальянская")
r3 = Restaurant("Самса", "Узбекская")
for r in [r1, r2, r3]:
    r.describe_restaurant()
    r.open_restaurant()
    print()
newRestaurant.update_rating(9) #13.3 обновление рейтинга
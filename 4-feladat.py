persons = ["John", "Marissa", "Pete", "Dayton"]
restaurants = ["Japanese", "American", "Mexican", "French"]

person = []
restaurant = []

for p in (persons):
  person.append(p)

for q in (restaurants):
  restaurant.append(q)

for i in range(len(persons)):
  for f in range(len(restaurants)):
    print(f'{person[i]} eats {restaurant[f]}')
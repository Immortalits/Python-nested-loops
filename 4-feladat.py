persons = ["John", "Marissa", "Pete", "Dayton"]
restaurants = ["Japanese", "American", "Mexican", "French"]

for i in range(len(persons)):
    for f in range(len(restaurants)):
        print(f'{persons[i]} eats {restaurants[f]}')
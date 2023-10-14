"""
Python 
"""
cities = ["new york", "san francisco","london","tokyo","barcelona","bangkok","lisbon","los angeles","toronto"]

# Exercise 1 - print out all of the cities in the array WITH proper capitalization. **HINT: use string.title()
print("----- Exercise 1 -----")

for city in cities:
    print(city.title())

# Exercise 2 - print out all the cities that are not in the visited cities array
print("----- Exercise 2 -----")
visited_cities = ["new york","london","bangkok"]

for city in cities:
    if city not in visited_cities:
        print(city)

# Exercise 3 - dictionaries. Print out what I think about london. Use bracket notation to select a specific entry in a dictionary. Ex: dictionary['entry']
print("----- Exercise 3 -----")
city_reviews = {"new york":"my favorite","london":"cool but rainy","tokyo":"i really want to go"}

print(city_reviews['london'])

# Exercise 4 - math. Print out the city I have not been to. You must determine this programatically. 
print("----- Exercise 4 -----")
city_visits = {"new york":55,"london":2,"tokyo":0,"lisbon":1}

for city in city_visits:
    if city_visits[city] == 0:
        print(city)

# Exercise 5. Print out the city from `city_visits` I have visited the most. You must determine this programatically. 
print("----- Exercise 5 -----")
most_visits = 0
for city in city_visits:
    if city_visits[city] > most_visits:
        most_visited_city = {city:city_visits[city]}
        most_visits = city_visits[city]
print(most_visited_city)

# Exercise 6. Pretty printing with f strings. Use f string notation to print out: "I live in Willy B, New York". You must use the provided variables.
print("----- Exercise 6 -----")
city = "New York"
where_i_live = "Willy B"

print(f"I live in {where_i_live}, {city}")
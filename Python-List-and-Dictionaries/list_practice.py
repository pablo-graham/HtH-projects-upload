cities = ["Oakland", "Atlanta", "New York City", "Seattle", "Memphis", "Miami", "Boston", "Los Angeles", "Denver", "New Orleans"]

# print(cities)

# print(cities[0] + ", " + cities[2] + ", " + cities[7])

fourCities = cities[0:4]
# print(fourCities)

cities[0] = "San Francisco"
cities[2] = "Brooklyn"
cities[7] = "Hollywood"
cities[5] = "Tampa"
# print(cities)

cities.append("Oakland")
cities.extend(["New York City", "Los Angeles"])
cities.insert(0, "Miami")
# print(cities)

del cities[5]
cities.pop(5)
cities.remove("Denver")
# print(cities)


letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# print(letters) 
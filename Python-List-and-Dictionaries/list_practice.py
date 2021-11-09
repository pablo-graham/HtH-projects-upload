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

def printCities():
    for i in range(len(cities)):
        if(i == 0):
            print(cities[i])
        elif len(cities[i]) > len(cities[i-1]):
            print(cities[i])

    while i <= (len(cities)):
        if(i == 0):
            print(cities[i])
        elif len(cities[i]) > len(cities[i-1]):
            print(cities[i])
        i +=1

# printCities()

def sortCities():
    for i in range(len(cities)):
        if i == len(cities) - 1:
            return cities
        elif len(cities[i]) <= len(cities[i+1]):
            continue
        else:
            short = cities[i + 1]
            cities.pop(i + 1)
            cities.append(short)

    return cities

print(sortCities())
# need help in the last STRETCH of step x
# need help commbine functions

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j"]
# print(letters) 
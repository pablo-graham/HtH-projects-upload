foodPrices = {
    "Chicken": 1.59,
    "Beef": 1.99,
    "Cheese": 1.00,
    "Milk": 2.50
}

chickenPrices = foodPrices["Chicken"]
beefPrices = foodPrices["Beef"]
cheesePrices = foodPrices["Cheese"]
milkPrices = foodPrices["Milk"]

foodPrices["Apples"] = .20
foodPrices["Soda"] = 2.00
foodPrices["Cereal"] = 4.00

print(chickenPrices)
print(beefPrices)
print(cheesePrices)
print(milkPrices)
print(foodPrices["Apples"])
print(foodPrices["Soda"])
print(foodPrices["Cereal"])

foodPrices.pop("Chicken")
foodPrices.pop("Beef")

# print(foodPrices)



favorites = {
    "Color": "green",
    "Number": 7,
    "Show": "H.I.M.Y.M",
    "Anime": "Bunny Girl Senpai and Naruto"
}

favColor = favorites["Color"]
favNumber = favorites["Number"]
favShow = favorites["Show"]
favAnime = favorites["Anime"]

favorites["Car"] = "Acura NSX"
favorites["soccerTeam"] = "Real Madrid"
favorites["songATM"] = "Ode To The Mets"

# print(favColor)
# print(favNumber)
# print(favShow)
# print(favAnime)
# print(favorites["Car"])
# print(favorites["soccerTeam"])
# print(favorites["songATM"])

favorites.pop("Color")
favorites.pop("Number")

# print(favorites)


shoeInventory = {
    "Jordan 13" : 1,
    "Yeezy" : 8,
    "Foamposite" : 10,
    "Airmax" : 5,
    "SB Dunk" : 20
}

shoeInventory["SB Dunk"] -= 2
shoeInventory["Yeezy"] += 1


shoeInventory["Jordan 13"] += 7
shoeInventory["Yeezy"] =+ 7
shoeInventory["Foamposite"] += 7
shoeInventory["Airmax"] += 7
shoeInventory["SB Dunk"] += 7

shoeInventory["Jordan 13"] -= 3
shoeInventory["Yeezy"] -= 3
shoeInventory["Foamposite"] -= 3
shoeInventory["Airmax"] -= 3
shoeInventory["SB Dunk"] -= 3

shoeInventory["Travis Scott AF1"] = 1
shoeInventory["Vans"] = 3
shoeInventory["Cleats"] = 2

# print(shoeInventory)

shoeInventory.pop("Yeezy")
shoeInventory.pop("Airmax")

# print(shoeInventory)
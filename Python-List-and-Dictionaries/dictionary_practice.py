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

# print(chickenPrices)
# print(beefPrices)
# print(cheesePrices)
# print(milkPrices)
# print(foodPrices["Apples"])
# print(foodPrices["Soda"])
# print(foodPrices["Cereal"])

foodPrices.pop("Chicken")
foodPrices.pop("Milk")

# print(foodPrices)

# ------------------------- still need to do the last stretch -------------------------
def total_price(item1, item2) :
    if item1 in foodPrices and item2 in foodPrices:
        total = foodPrices[item1] + foodPrices[item2]
        print("The total price of beef and cheese is {}".format(total))
    else:
        print("that food is not available")

# total_price("Beef", "Cheese")

def price_difference(item1, item2):
    if item1 in foodPrices and item2 in foodPrices:
        dif = foodPrices[item1] - foodPrices[item2]
        if dif < 0:
            dif *= -1
        print("The difference in price of beef and cheese is {}".format(dif))
    else:
        print("that food is not available")

# price_difference("Cheese", "Beef")


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
# print(shoeInventory)
shoeInventory["SB Dunk"] -= 2
shoeInventory["Yeezy"] += 1
# print(shoeInventory)
shoeInventory["Jordan 13"] += 7
shoeInventory["Yeezy"] = shoeInventory["Yeezy"] + 7
shoeInventory["Foamposite"] += 7
shoeInventory["Airmax"] += 7
shoeInventory["SB Dunk"] += 7
# print(shoeInventory)

shoeInventory["Jordan 13"] -= 3
shoeInventory["Yeezy"] -= 3
shoeInventory["Foamposite"] -= 3
shoeInventory["Airmax"] -= 3
shoeInventory["SB Dunk"] -= 3
# print(shoeInventory)

shoeInventory["Travis Scott AF1"] = 1
shoeInventory["Vans"] = 3
shoeInventory["Cleats"] = 2

shoeInventory.pop("Foamposite")
shoeInventory.pop("Airmax")

def restock(item1, multi) :
    if item1 == "All":
            shoeInventory["Vans"] *= multi
            shoeInventory["Jordan 13"] *= multi
            shoeInventory["Travis Scott AF1"] *= multi
            shoeInventory["Cleats"] *= multi
            shoeInventory["SB Dunk"] *= multi
            shoeInventory["Yeezy"] *= multi
            print("The new inventory is {}".format(shoeInventory))
    elif item1 in shoeInventory:
        shoeInventory[item1] *= multi
        print("The new inventory is {}".format(shoeInventory))
    else:
        print("that shoe isn't available")

# restock("All", 3)


def clearance_sale(item1, sale):
    if item1 == "All":
            shoeInventory["Vans"] /= sale
            shoeInventory["Jordan 13"] /= sale
            shoeInventory["Travis Scott AF1"] /= sale
            shoeInventory["Cleats"] /= sale
            shoeInventory["SB Dunk"] /= sale
            shoeInventory["Yeezy"] /= sale
            print("The new inventory is {}".format(shoeInventory))
    elif item1 in shoeInventory:
        shoeInventory[item1] = shoeInventory[item1] / sale
        print("The new inventory {}".format(shoeInventory))
    else:
        print("that shoe is not available")

# clearance_sale("a", 2)


playersInSports = {
    "Soccer" : 11,
    "Basketball" : 5,
    "Baseball" : 9,
    "Football" : 11
}

def injuredPlayers(sport, numOfInjPlayers):
    if numOfInjPlayers == playersInSports[sport]:
         print("All your players are injured")
    elif numOfInjPlayers > playersInSports[sport]:
        print("how did you injured more players than you have?")
    else:
        print("{} number of not injured players left in your sport").format(playersInSports[sport] - numOfInjPlayers)
injuredPlayers("Soccer", 6)
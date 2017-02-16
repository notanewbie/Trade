import math
import random
class Player(object):
    name = ""
    Gold = 0
    Silver = 0
    Bronze = 0
    Platinum = 0
    Uranium = 0
    Iron = 0
    Tin = 0
    Titanium = 0
    Vibranium = 0
    Ultanium = 0
    Bread = 0
    Sugar = 0
    Salt = 0
    Corn = 0
    Chocolate = 0
    Pistachios = 0
    Bacon = 0
    Oysters = 0
    Eggs = 0
    Beef = 0
    Cherries = 0
    Rubies = 0
    Diamonds = 0
    Sapphires = 0
    Admantium = 0
    Blackberries = 0
    Kiwi = 0
    Strawberries = 0
    Wood = 0
    Cows = 0
    Chicken = 0
    Turkey = 0
    Fish = 0
    Pigs = 0
    Sheep = 0
    Horses = 0
    Interest1 = ""
    Interest2 = ""
    Interest3 = ""
    Disinterest1 = ""
    Disinterest2 = ""
    Disinterest3 = ""
class Material(object):
    Total = 0
    Left = 0
    Taken = 0
    Name = ""
Silver = Material()
Silver.Total = 35
Silver.Left = 35
Silver.Name = "Silver"

Gold = Material()
Gold.Total = 20
Gold.Left = 20
Gold.Name = "Gold"

Bronze = Material()
Bronze.Total = 50
Bronze.Left = 50
Bronze.Name = "Bronze"

Platinum = Material()
Platinum.Total = 30
Platinum.Left = 30
Platinum.Name = "Platinum"

Uranium = Material()
Uranium.Total = 10
Uranium.Left = 10
Uranium.Name = "Uranium"

Iron = Material()
Iron.Total = 75
Iron.Left = 75
Iron.Name = "Iron"

Tin = Material()
Tin.Total = 99
Tin.Left = 99
Tin.Name = "Tin"

Titanium = Material()
Titanium.Total = 5
Titanium.Left = 5
Titanium.Name = "Titanium"

Vibranium = Material()
Vibranium.Total = 20
Vibranium.Left = 20
Vibranium.Name = "Vibranium"

Ultanium = Material()
Ultanium.Total = 1
Ultanium.Left = 1
Ultanium.Name = "Ultanium"

Bread = Material()
Bread.Total = 80
Bread.Left = 80
Bread.Name = "Bread"

Sugar = Material()
Sugar.Total = 60
Sugar.Left = 60

Salt = Material()
Salt.Total = 40
Salt.Left = 40
Salt.Name = "Salt"

Corn = Material()
Corn.Total = 80
Corn.Left = 80
Corn.Name = "Corn"

Chocolate = Material()
Chocolate.Total = 55
Chocolate.Left = 55
Chocolate.Name = "Chocolate"

Pistachios = Material()
Pistachios.Total = 45
Pistachios.Left = 45
Pistachios.Name = "Pistachios"

Bacon = Material()
Bacon.Total = 85
Bacon.Left = 85
Bacon.Name = "Bacon"

Oysters = Material()
Oysters.Total = 25
Oysters.Left = 25
Oysters.Name = "Oysters"

Eggs = Material()
Eggs.Total = 99
Eggs.Left = 99
Eggs.Name = "Eggs"

Beef = Material()
Beef.Total = 80
Beef.Left = 80
Beef.Name = "Beef"

Cherries = Material()
Cherries.Total = 70
Cherries.Left = 70
Cherries.Name = "Cherries"

Rubies = Material()
Rubies.Total = 15
Rubies.Left = 15
Rubies.Name = "Rubies"

Diamonds = Material()
Diamonds.Total = 30
Diamonds.Left = 30
Diamonds.Name = "Diamonds"

Sapphires = Material()
Sapphires.Total = 5
Sapphires.Left = 5
Sapphires.Name = "Sapphires"

Admantium = Material()
Admantium.Total = 3
Admantium.Left = 3
Admantium.Name = "Admantium"

Blackberries = Material()
Blackberries.Total = 30
Blackberries.Left = 30
Blackberries.Name = "Blackberries"

Kiwi = Material()
Kiwi.Total = 15
Kiwi.Left = 15
Kiwi.Name = "Kiwi"

Strawberries = Material()
Strawberries.Total = 50
Strawberries.Left = 50
Strawberries.Name = "Strawberries"

Wood = Material()
Wood.Total = 50
Wood.Left = 50
Wood.Name = "Wood"

Cows = Material()
Cows.Total = 85
Cows.Left = 85
Cows.Name = "Cows"

Chicken = Material()
Chicken.Total = 99
Chicken.Left = 99
Chicken.Name = "Chicken"

Turkey = Material()
Turkey.Total = 99
Turkey.Left = 99
Turkey.Name = "Turkey"

Fish = Material()
Fish.Total = 99
Fish.Left = 99
Fish.Name = "Fish"

Pigs = Material()
Pigs.Total = 70
Pigs.Left = 70
Pigs.Name = "Pigs"

Sheep = Material()
Sheep.Total = 99
Sheep.Left = 99
Sheep.Name = "Sheep"

Horses = Material()
Horses.Total = 70
Horses.Left = 70
Horses.Name = "Horses"

ListOfMaterials = [Gold, Silver, Bronze, Platinum, Uranium, Iron, Tin, Titanium, Vibranium, Ultanium, Bread, Sugar, Salt, Corn, Chocolate, Pistachios, Bacon, Oysters, Eggs, Beef, Cherries, Rubies, Diamonds, Sapphires, Admantium, Blackberries, Kiwi, Strawberries, Wood, Cows, Chicken, Turkey, Fish, Pigs, Sheep, Horses]
You = Player()
def IsWorth(Subject):
    return 1/float(Subject)
#print IsWorth(Sheep.Left)
#print IsWorth(Uranium.Total)
response = int(raw_input("How many players do you want to play against?"))
players = 0
ListOfPlayers = []
Play = []
for item in range(response):
    players = players + 1
    response = response - 1
    ListOfPlayers.append("Player " + str(players))
    print ListOfPlayers
    Play.append(Player())
print "Distributing Gold..."
#Name Players
i = 0
Mats = 0
for item in ListOfMaterials:
        Mats = Mats + 1
Mats = Mats - 1
for object in ListOfPlayers:
    Play[i].name = "Player " + str(i + 1)
    Play[i].Interest1 = ListOfMaterials[random.randint(0, Mats)].Name
    Play[i].Interest2 = ListOfMaterials[random.randint(0, Mats)].Name
    Play[i].Interest3 = ListOfMaterials[random.randint(0, Mats)].Name
    print Play[i].name + " wants " + Play[i].Interest1 + ", " + Play[i].Interest2 + " and " + Play[i].Interest3 + "."
    Play[i].Disinterest1 = ListOfMaterials[random.randint(0, Mats)].Name
    Play[i].Disinterest2 = ListOfMaterials[random.randint(0, Mats)].Name
    Play[i].Disinterest3 = ListOfMaterials[random.randint(0, Mats)].Name
    print Play[i].name + " doesn't want " + Play[i].Disinterest1 + ", " + Play[i].Disinterest2 + " and " + Play[i].Disinterest3 + "."
    print ""
    i = i + 1
i = 0
#Dole Out (Function)
def Dole(Thing, i):
    print "_-=-_"
    print "Dole() Running."
    #print "Doling out " + Thing.Name
    Max = int(Thing.Left * .5)
    if i < 3:
        print "For player " + str(i) + " I'm lowering the maximum ammount he can get from " + str(Thing.Left) + " to " + str(Max)
        Thing.Taken = random.randint(0, Max);
        print "See, I only took " + str(Thing.Taken)
        #Play[i].Gold = Thing.Taken
        Thing.Left = Thing.Left - Thing.Taken
    if i > 2:
        Thing.Taken = Thing.Left - random.randint(0, Thing.Left);
        #Play[i].Gold = Thing.Taken
        Thing.Left = Thing.Left - Thing.Taken
    #print "Took " + str(Taken) + " away. Now there's " + str(GoldLeft) + " left."
    #print Play[i].name + " has " + str(Play[i].Gold) + " " + Thing.Name
    #print "There is " + str(Thing.Left) + " " + Thing.Name + " left."
    print "Dole() finished running."
    print "_-=-_"
    return Thing

#Dole Out Gold
You.Name = str(raw_input("What's your name?"))
i = 0
Gold = Dole(Gold, i)
You.Gold = Gold.Taken
print You.Name + " has " + str(You.Gold) + " Gold."
print "There is " + str(Gold.Left) + " Gold left."
for item in ListOfPlayers:
    Gold = Dole(Gold, i)
    Play[i].Gold = Gold.Taken
    print Play[i].name + " has " + str(Play[i].Gold) + " Gold."
    print "There is " + str(Gold.Left) + " Gold left."
    i = i + 1
i = 0
Silver = Dole(Silver, i)
You.Silver = Silver.Taken
print You.Name + " has " + str(You.Silver) + " Silver."
print "There is " + str(Silver.Left) + " Silver left."
for item in ListOfPlayers:
    Silver = Dole(Silver, i)
    Play[i].Silver = Silver.Taken
    print Play[i].name + " has " + str(Play[i].Silver) + " Silver."
    print "There is " + str(Silver.Left) + " Silver left."
    i = i + 1
i = 0
Bronze = Dole(Bronze, i)
You.Bronze = Bronze.Taken
print You.Name + " has " + str(You.Bronze) + " Bronze."
print "There is " + str(Bronze.Left) + " Bronze left."
for item in ListOfPlayers:
    Bronze = Dole(Bronze, i)
    Play[i].Bronze = Bronze.Taken
    print Play[i].name + " has " + str(Play[i].Bronze) + " Bronze."
    print "There is " + str(Bronze.Left) + " Bronze left."
    i = i + 1
i = 0
Platinum = Dole(Platinum, i)
You.Platinum = Platinum.Taken
print You.Name + " has " + str(You.Platinum) + " Platinum."
print "There is " + str(Platinum.Left) + " Platinum left."
for item in ListOfPlayers:
    Platinum = Dole(Platinum, i)
    Play[i].Platinum = Platinum.Taken
    print Play[i].name + " has " + str(Play[i].Platinum) + " Platinum."
    print "There is " + str(Platinum.Left) + " Platinum left."
    i = i + 1
i = 0
Uranium = Dole(Uranium, i)
You.Uranium = Uranium.Taken
print You.Name + " has " + str(You.Uranium) + " Uranium."
print "There is " + str(Uranium.Left) + " Uranium left."
for item in ListOfPlayers:
    Uranium = Dole(Uranium, i)
    Play[i].Uranium = Uranium.Taken
    print Play[i].name + " has " + str(Play[i].Uranium) + " Uranium."
    print "There is " + str(Uranium.Left) + " Uranium left."
    i = i + 1
i = 0
Iron = Dole(Iron, i)
You.Iron = Iron.Taken
print You.Name + " has " + str(You.Iron) + " Iron."
print "There is " + str(Iron.Left) + " Iron left."
for item in ListOfPlayers:
    Iron = Dole(Iron, i)
    Play[i].Iron = Iron.Taken
    print Play[i].name + " has " + str(Play[i].Iron) + " Iron."
    print "There is " + str(Iron.Left) + " Iron left."
    i = i + 1
i = 0
Tin = Dole(Tin, i)
You.Tin = Tin.Taken
print You.Name + " has " + str(You.Tin) + " Tin."
print "There is " + str(Tin.Left) + " Tin left."
for item in ListOfPlayers:
    Tin = Dole(Tin, i)
    Play[i].Tin = Tin.Taken
    print Play[i].name + " has " + str(Play[i].Tin) + " Tin."
    print "There is " + str(Tin.Left) + " Tin left."
    i = i + 1
i = 0
Titanium = Dole(Titanium, i)
You.Titanium = Titanium.Taken
print You.Name + " has " + str(You.Titanium) + " Titanium."
print "There is " + str(Titanium.Left) + " Titanium left."
for item in ListOfPlayers:
    Titanium = Dole(Titanium, i)
    Play[i].Titanium = Titanium.Taken
    print Play[i].name + " has " + str(Play[i].Titanium) + " Titanium."
    print "There is " + str(Titanium.Left) + " Titanium left."
    i = i + 1
i = 0
Vibranium = Dole(Vibranium, i)
You.Vibranium = Vibranium.Taken
print You.Name + " has " + str(You.Vibranium) + " Vibranium."
print "There is " + str(Vibranium.Left) + " Vibranium left."
for item in ListOfPlayers:
    Vibranium = Dole(Vibranium, i)
    Play[i].Vibranium = Vibranium.Taken
    print Play[i].name + " has " + str(Play[i].Vibranium) + " Vibranium."
    print "There is " + str(Vibranium.Left) + " Vibranium left."
    i = i + 1
i = 0
Ultanium = Dole(Ultanium, i)
You.Ultanium = Ultanium.Taken
print You.Name + " has " + str(You.Ultanium) + " Ultanium."
print "There is " + str(Ultanium.Left) + " Ultanium left."
for item in ListOfPlayers:
    Ultanium = Dole(Ultanium, i)
    Play[i].Ultanium = Ultanium.Taken
    print Play[i].name + " has " + str(Play[i].Ultanium) + " Ultanium."
    print "There is " + str(Ultanium.Left) + " Ultanium left."
    i = i + 1
i = 0
Bread = Dole(Bread, i)
You.Bread = Bread.Taken
print You.Name + " has " + str(You.Bread) + " Bread."
print "There is " + str(Bread.Left) + " Bread left."
for item in ListOfPlayers:
    Bread = Dole(Bread, i)
    Play[i].Bread = Bread.Taken
    print Play[i].name + " has " + str(Play[i].Bread) + " Bread."
    print "There is " + str(Bread.Left) + " Bread left."
    i = i + 1
i = 0
Sugar = Dole(Sugar, i)
You.Sugar = Sugar.Taken
print You.Name + " has " + str(You.Sugar) + " Sugar."
print "There is " + str(Sugar.Left) + " Sugar left."
for item in ListOfPlayers:
    Sugar = Dole(Sugar, i)
    Play[i].Sugar = Sugar.Taken
    print Play[i].name + " has " + str(Play[i].Sugar) + " Sugar."
    print "There is " + str(Sugar.Left) + " Sugar left."
    i = i + 1
i = 0
Salt = Dole(Salt, i)
You.Salt = Salt.Taken
print You.Name + " has " + str(You.Salt) + " Salt."
print "There is " + str(Salt.Left) + " Salt left."
for item in ListOfPlayers:
    Salt = Dole(Salt, i)
    Play[i].Salt = Salt.Taken
    print Play[i].name + " has " + str(Play[i].Salt) + " Salt."
    print "There is " + str(Salt.Left) + " Salt left."
    i = i + 1
i = 0
Corn = Dole(Corn, i)
You.Corn = Corn.Taken
print You.Name + " has " + str(You.Corn) + " Corn."
print "There is " + str(Corn.Left) + " Corn left."
for item in ListOfPlayers:
    Corn = Dole(Corn, i)
    Play[i].Corn = Corn.Taken
    print Play[i].name + " has " + str(Play[i].Corn) + " Corn."
    print "There is " + str(Corn.Left) + " Corn left."
    i = i + 1
i = 0
Chocolate = Dole(Chocolate, i)
You.Chocolate = Chocolate.Taken
print You.Name + " has " + str(You.Chocolate) + " Chocolate."
print "There is " + str(Chocolate.Left) + " Chocolate left."
for item in ListOfPlayers:
    Chocolate = Dole(Chocolate, i)
    Play[i].Chocolate = Chocolate.Taken
    print Play[i].name + " has " + str(Play[i].Chocolate) + " Chocolate."
    print "There is " + str(Chocolate.Left) + " Chocolate left."
    i = i + 1
i = 0
Pistachios = Dole(Pistachios, i)
You.Pistachios = Pistachios.Taken
print You.Name + " has " + str(You.Pistachios) + " Pistachios."
print "There is " + str(Pistachios.Left) + " Pistachios left."
for item in ListOfPlayers:
    Pistachios = Dole(Pistachios, i)
    Play[i].Pistachios = Pistachios.Taken
    print Play[i].name + " has " + str(Play[i].Pistachios) + " Pistachios."
    print "There is " + str(Pistachios.Left) + " Pistachios left."
    i = i + 1
i = 0
Bacon = Dole(Bacon, i)
You.Bacon = Bacon.Taken
print You.Name + " has " + str(You.Bacon) + " Bacon."
print "There is " + str(Bacon.Left) + " Bacon left."
for item in ListOfPlayers:
    Bacon = Dole(Bacon, i)
    Play[i].Bacon = Bacon.Taken
    print Play[i].name + " has " + str(Play[i].Bacon) + " Bacon."
    print "There is " + str(Bacon.Left) + " Bacon left."
    i = i + 1
i = 0
Oysters = Dole(Oysters, i)
You.Oysters = Oysters.Taken
print You.Name + " has " + str(You.Oysters) + " Oysters."
print "There is " + str(Oysters.Left) + " Oysters left."
for item in ListOfPlayers:
    Oysters = Dole(Oysters, i)
    Play[i].Oysters = Oysters.Taken
    print Play[i].name + " has " + str(Play[i].Oysters) + " Oysters."
    print "There is " + str(Oysters.Left) + " Oysters left."
    i = i + 1
i = 0
Eggs = Dole(Eggs, i)
You.Eggs = Eggs.Taken
print You.Name + " has " + str(You.Eggs) + " Eggs."
print "There is " + str(Eggs.Left) + " Eggs left."
for item in ListOfPlayers:
    Eggs = Dole(Eggs, i)
    Play[i].Eggs = Eggs.Taken
    print Play[i].name + " has " + str(Play[i].Eggs) + " Eggs."
    print "There is " + str(Eggs.Left) + " Eggs left."
    i = i + 1
i = 0
Beef = Dole(Beef, i)
You.Beef = Beef.Taken
print You.Name + " has " + str(You.Beef) + " Beef."
print "There is " + str(Beef.Left) + " Beef left."
for item in ListOfPlayers:
    Beef = Dole(Beef, i)
    Play[i].Beef = Beef.Taken
    print Play[i].name + " has " + str(Play[i].Beef) + " Beef."
    print "There is " + str(Beef.Left) + " Beef left."
    i = i + 1
i = 0
Cherries = Dole(Cherries, i)
You.Cherries = Cherries.Taken
print You.Name + " has " + str(You.Cherries) + " Cherries."
print "There is " + str(Cherries.Left) + " Cherries left."
for item in ListOfPlayers:
    Cherries = Dole(Cherries, i)
    Play[i].Cherries = Cherries.Taken
    print Play[i].name + " has " + str(Play[i].Cherries) + " Cherries."
    print "There is " + str(Cherries.Left) + " Cherries left."
    i = i + 1
i = 0
Rubies = Dole(Rubies, i)
You.Rubies = Rubies.Taken
print You.Name + " has " + str(You.Rubies) + " Rubies."
print "There is " + str(Rubies.Left) + " Rubies left."
for item in ListOfPlayers:
    Rubies = Dole(Rubies, i)
    Play[i].Rubies = Rubies.Taken
    print Play[i].name + " has " + str(Play[i].Rubies) + " Rubies."
    print "There is " + str(Rubies.Left) + " Rubies left."
    i = i + 1
i = 0
Diamonds = Dole(Diamonds, i)
You.Diamonds = Diamonds.Taken
print You.Name + " has " + str(You.Diamonds) + " Diamonds."
print "There is " + str(Diamonds.Left) + " Diamonds left."
for item in ListOfPlayers:
    Diamonds = Dole(Diamonds, i)
    Play[i].Diamonds = Diamonds.Taken
    print Play[i].name + " has " + str(Play[i].Diamonds) + " Diamonds."
    print "There is " + str(Diamonds.Left) + " Diamonds left."
    i = i + 1
i = 0
Sapphires = Dole(Sapphires, i)
You.Sapphires = Sapphires.Taken
print You.Name + " has " + str(You.Sapphires) + " Sapphires."
print "There is " + str(Sapphires.Left) + " Sapphires left."
for item in ListOfPlayers:
    Sapphires = Dole(Sapphires, i)
    Play[i].Sapphires = Sapphires.Taken
    print Play[i].name + " has " + str(Play[i].Sapphires) + " Sapphires."
    print "There is " + str(Sapphires.Left) + " Sapphires left."
    i = i + 1
i = 0
Admantium = Dole(Admantium, i)
You.Admantium = Admantium.Taken
print You.Name + " has " + str(You.Admantium) + " Admantium."
print "There is " + str(Admantium.Left) + " Admantium left."
for item in ListOfPlayers:
    Admantium = Dole(Admantium, i)
    Play[i].Admantium = Admantium.Taken
    print Play[i].name + " has " + str(Play[i].Admantium) + " Admantium."
    print "There is " + str(Admantium.Left) + " Admantium left."
    i = i + 1
i = 0
Blackberries = Dole(Blackberries, i)
You.Blackberries = Blackberries.Taken
print You.Name + " has " + str(You.Blackberries) + " Blackberries."
print "There is " + str(Blackberries.Left) + " Blackberries left."
for item in ListOfPlayers:
    Blackberries = Dole(Blackberries, i)
    Play[i].Blackberries = Blackberries.Taken
    print Play[i].name + " has " + str(Play[i].Blackberries) + " Blackberries."
    print "There is " + str(Blackberries.Left) + " Blackberries left."
    i = i + 1
i = 0
Kiwi = Dole(Kiwi, i)
You.Kiwi = Kiwi.Taken
print You.Name + " has " + str(You.Kiwi) + " Kiwi."
print "There is " + str(Kiwi.Left) + " Kiwi left."
for item in ListOfPlayers:
    Kiwi = Dole(Kiwi, i)
    Play[i].Kiwi = Kiwi.Taken
    print Play[i].name + " has " + str(Play[i].Kiwi) + " Kiwi."
    print "There is " + str(Kiwi.Left) + " Kiwi left."
    i = i + 1
i = 0
Strawberries = Dole(Strawberries, i)
You.Strawberries = Strawberries.Taken
print You.Name + " has " + str(You.Strawberries) + " Strawberries."
print "There is " + str(Strawberries.Left) + " Strawberries left."
for item in ListOfPlayers:
    Strawberries = Dole(Strawberries, i)
    Play[i].Strawberries = Strawberries.Taken
    print Play[i].name + " has " + str(Play[i].Strawberries) + " Strawberries."
    print "There is " + str(Strawberries.Left) + " Strawberries left."
    i = i + 1
i = 0
Wood = Dole(Wood, i)
You.Wood = Wood.Taken
print You.Name + " has " + str(You.Wood) + " Wood."
print "There is " + str(Wood.Left) + " Wood left."
for item in ListOfPlayers:
    Wood = Dole(Wood, i)
    Play[i].Wood = Wood.Taken
    print Play[i].name + " has " + str(Play[i].Wood) + " Wood."
    print "There is " + str(Wood.Left) + " Wood left."
    i = i + 1
i = 0
Cows = Dole(Cows, i)
You.Cows = Cows.Taken
print You.Name + " has " + str(You.Cows) + " Cows."
print "There is " + str(Cows.Left) + " Cows left."
for item in ListOfPlayers:
    Cows = Dole(Cows, i)
    Play[i].Cows = Cows.Taken
    print Play[i].name + " has " + str(Play[i].Cows) + " Cows."
    print "There is " + str(Cows.Left) + " Cows left."
    i = i + 1
i = 0
Chicken = Dole(Chicken, i)
You.Chicken = Chicken.Taken
print You.Name + " has " + str(You.Chicken) + " Chicken."
print "There is " + str(Chicken.Left) + " Chicken left."
for item in ListOfPlayers:
    Chicken = Dole(Chicken, i)
    Play[i].Chicken = Chicken.Taken
    print Play[i].name + " has " + str(Play[i].Chicken) + " Chicken."
    print "There is " + str(Chicken.Left) + " Chicken left."
    i = i + 1
i = 0
Turkey = Dole(Turkey, i)
You.Turkey = Turkey.Taken
print You.Name + " has " + str(You.Turkey) + " Turkey."
print "There is " + str(Turkey.Left) + " Turkey left."
for item in ListOfPlayers:
    Turkey = Dole(Turkey, i)
    Play[i].Turkey = Turkey.Taken
    print Play[i].name + " has " + str(Play[i].Turkey) + " Turkey."
    print "There is " + str(Turkey.Left) + " Turkey left."
    i = i + 1
i = 0
Fish = Dole(Fish, i)
You.Fish = Fish.Taken
print You.Name + " has " + str(You.Fish) + " Fish."
print "There is " + str(Fish.Left) + " Fish left."
for item in ListOfPlayers:
    Fish = Dole(Fish, i)
    Play[i].Fish = Fish.Taken
    print Play[i].name + " has " + str(Play[i].Fish) + " Fish."
    print "There is " + str(Fish.Left) + " Fish left."
    i = i + 1
i = 0
Pigs = Dole(Pigs, i)
You.Pigs = Pigs.Taken
print You.Name + " has " + str(You.Pigs) + " Pigs."
print "There is " + str(Pigs.Left) + " Pigs left."
for item in ListOfPlayers:
    Pigs = Dole(Pigs, i)
    Play[i].Pigs = Pigs.Taken
    print Play[i].name + " has " + str(Play[i].Pigs) + " Pigs."
    print "There is " + str(Pigs.Left) + " Pigs left."
    i = i + 1
i = 0
Sheep = Dole(Sheep, i)
You.Sheep = Sheep.Taken
print You.Name + " has " + str(You.Sheep) + " Sheep."
print "There is " + str(Sheep.Left) + " Sheep left."
for item in ListOfPlayers:
    Sheep = Dole(Sheep, i)
    Play[i].Sheep = Sheep.Taken
    print Play[i].name + " has " + str(Play[i].Sheep) + " Sheep."
    print "There is " + str(Sheep.Left) + " Sheep left."
    i = i + 1
i = 0
Horses = Dole(Horses, i)
You.Horses = Horses.Taken
print You.Name + " has " + str(You.Horses) + " Horses."
print "There is " + str(Horses.Left) + " Horses left."
for item in ListOfPlayers:
    Horses = Dole(Horses, i)
    Play[i].Horses = Horses.Taken
    print Play[i].name + " has " + str(Play[i].Horses) + " Horses."
    print "There is " + str(Horses.Left) + " Horses left."
    i = i + 1
print You.Name + ":"
print "Gold: " + str(You.Gold) + "; Silver: " + str(You.Silver) + "; Bronze: " + str(You.Bronze) + "; Platinum: " + str(You.Platinum) + "; Uranium: " + str(You.Uranium) + "; Iron: " + str(You.Iron) + "; Tin: " + str(You.Tin) + "; Titanium: " + str(You.Titanium) + "; Vibranium: " + str(You.Vibranium) + "; Ultanium: " + str(You.Ultanium) + "; Bread: " + str(You.Bread) + "; Sugar: " + str(You.Sugar) + "; Salt: " + str(You.Salt) + "; Corn: " + str(You.Corn) + "; Chocolate: " + str(You.Chocolate) + "; Pistachios: " + str(You.Pistachios) + "; Bacon: " + str(You.Bacon) + "; Oysters: " + str(You.Oysters) + "; Eggs: " + str(You.Eggs) + "; Beef: " + str(You.Beef) + "; Cherries: " + str(You.Cherries) + "; Rubies: " + str(You.Rubies) + "; Diamonds: " + str(You.Diamonds) + "; Sapphires: " + str(You.Sapphires) + "; Admantium: " + str(You.Admantium) + "; Blackberries: " + str(You.Blackberries) + "; Kiwi: " + str(You.Kiwi) + "; Strawberries: " + str(You.Strawberries) + "; Wood: " + str(You.Wood) + "; Cows: " + str(You.Cows) + "; Chicken: " + str(You.Chicken) + "; Turkey: " + str(You.Turkey) + "; Fish: " + str(You.Fish) + "; Pigs: " + str(You.Pigs) + "; Sheep: " + str(You.Sheep) + "; Horses: " + str(You.Horses)
i = 0
for item in ListOfPlayers:
    print Play[i].name + ":"
    print "Gold: " + str(Play[i].Gold) + "; Silver: " + str(Play[i].Silver) + "; Bronze: " + str(Play[i].Bronze) + "; Platinum: " + str(Play[i].Platinum) + "; Uranium: " + str(Play[i].Uranium) + "; Iron: " + str(Play[i].Iron) + "; Tin: " + str(Play[i].Tin) + "; Titanium: " + str(Play[i].Titanium) + "; Vibranium: " + str(Play[i].Vibranium) + "; Ultanium: " + str(Play[i].Ultanium) + "; Bread: " + str(Play[i].Bread) + "; Sugar: " + str(Play[i].Sugar) + "; Salt: " + str(Play[i].Salt) + "; Corn: " + str(Play[i].Corn) + "; Chocolate: " + str(Play[i].Chocolate) + "; Pistachios: " + str(Play[i].Pistachios) + "; Bacon: " + str(Play[i].Bacon) + "; Oysters: " + str(Play[i].Oysters) + "; Eggs: " + str(Play[i].Eggs) + "; Beef: " + str(Play[i].Beef) + "; Cherries: " + str(Play[i].Cherries) + "; Rubies: " + str(Play[i].Rubies) + "; Diamonds: " + str(Play[i].Diamonds) + "; Sapphires: " + str(Play[i].Sapphires) + "; Admantium: " + str(Play[i].Admantium) + "; Blackberries: " + str(Play[i].Blackberries) + "; Kiwi: " + str(Play[i].Kiwi) + "; Strawberries: " + str(Play[i].Strawberries) + "; Wood: " + str(Play[i].Wood) + "; Cows: " + str(Play[i].Cows) + "; Chicken: " + str(Play[i].Chicken) + "; Turkey: " + str(Play[i].Turkey) + "; Fish: " + str(Play[i].Fish) + "; Pigs: " + str(Play[i].Pigs) + "; Sheep: " + str(Play[i].Sheep) + "; Horses: " + str(Play[i].Horses)
    i = i + 1
def Trade(ThisPlayer, ThatPlayer, Giveamount, Giving, Getamount, Getting):
    print ThisPlayer.name + " is giving " + ThatPlayer.name + " " + str(Giveamount) + " " + Giving + "."
    if Giving is "Silver":
        ThisPlayer.Silver = ThisPlayer.Silver + Giveamount
        ThatPlayer.Silver = ThatPlayer.Silver - Giveamount
    if Getting is "Silver":
        ThisPlayer.Silver = ThisPlayer.Silver - Giveamount
        ThatPlayer.Silver = ThatPlayer.Silver + Giveamount
    if Giving is "Bronze":
        ThisPlayer.Bronze = ThisPlayer.Bronze + Giveamount
        ThatPlayer.Bronze = ThatPlayer.Bronze - Giveamount
    if Getting is "Bronze":
        ThisPlayer.Bronze = ThisPlayer.Bronze - Giveamount
        ThatPlayer.Bronze = ThatPlayer.Bronze + Giveamount
    if Giving is "Platinum":
        ThisPlayer.Platinum = ThisPlayer.Platinum + Giveamount
        ThatPlayer.Platinum = ThatPlayer.Platinum - Giveamount
    if Getting is "Platinum":
        ThisPlayer.Platinum = ThisPlayer.Platinum - Giveamount
        ThatPlayer.Platinum = ThatPlayer.Platinum + Giveamount
    if Giving is "Uranium":
        ThisPlayer.Uranium = ThisPlayer.Uranium + Giveamount
        ThatPlayer.Uranium = ThatPlayer.Uranium - Giveamount
    if Getting is "Uranium":
        ThisPlayer.Uranium = ThisPlayer.Uranium - Giveamount
        ThatPlayer.Uranium = ThatPlayer.Uranium + Giveamount
    if Giving is "Iron":
        ThisPlayer.Iron = ThisPlayer.Iron + Giveamount
        ThatPlayer.Iron = ThatPlayer.Iron - Giveamount
    if Getting is "Iron":
        ThisPlayer.Iron = ThisPlayer.Iron - Giveamount
        ThatPlayer.Iron = ThatPlayer.Iron + Giveamount
    if Giving is "Tin":
        ThisPlayer.Tin = ThisPlayer.Tin + Giveamount
        ThatPlayer.Tin = ThatPlayer.Tin - Giveamount
    if Getting is "Tin":
        ThisPlayer.Tin = ThisPlayer.Tin - Giveamount
        ThatPlayer.Tin = ThatPlayer.Tin + Giveamount
    if Giving is "Titanium":
        ThisPlayer.Titanium = ThisPlayer.Titanium + Giveamount
        ThatPlayer.Titanium = ThatPlayer.Titanium - Giveamount
    if Getting is "Titanium":
        ThisPlayer.Titanium = ThisPlayer.Titanium - Giveamount
        ThatPlayer.Titanium = ThatPlayer.Titanium + Giveamount
    if Giving is "Vibranium":
        ThisPlayer.Vibranium = ThisPlayer.Vibranium + Giveamount
        ThatPlayer.Vibranium = ThatPlayer.Vibranium - Giveamount
    if Getting is "Vibranium":
        ThisPlayer.Vibranium = ThisPlayer.Vibranium - Giveamount
        ThatPlayer.Vibranium = ThatPlayer.Vibranium + Giveamount
    if Giving is "Ultanium":
        ThisPlayer.Ultanium = ThisPlayer.Ultanium + Giveamount
        ThatPlayer.Ultanium = ThatPlayer.Ultanium - Giveamount
    if Getting is "Ultanium":
        ThisPlayer.Ultanium = ThisPlayer.Ultanium - Giveamount
        ThatPlayer.Ultanium = ThatPlayer.Ultanium + Giveamount
    if Giving is "Bread":
        ThisPlayer.Bread = ThisPlayer.Bread + Giveamount
        ThatPlayer.Bread = ThatPlayer.Bread - Giveamount
    if Getting is "Bread":
        ThisPlayer.Bread = ThisPlayer.Bread - Giveamount
        ThatPlayer.Bread = ThatPlayer.Bread + Giveamount
    if Giving is "Sugar":
        ThisPlayer.Sugar = ThisPlayer.Sugar + Giveamount
        ThatPlayer.Sugar = ThatPlayer.Sugar - Giveamount
    if Getting is "Sugar":
        ThisPlayer.Sugar = ThisPlayer.Sugar - Giveamount
        ThatPlayer.Sugar = ThatPlayer.Sugar + Giveamount
    if Giving is "Salt":
        ThisPlayer.Salt = ThisPlayer.Salt + Giveamount
        ThatPlayer.Salt = ThatPlayer.Salt - Giveamount
    if Getting is "Salt":
        ThisPlayer.Salt = ThisPlayer.Salt - Giveamount
        ThatPlayer.Salt = ThatPlayer.Salt + Giveamount
    if Giving is "Corn":
        ThisPlayer.Corn = ThisPlayer.Corn + Giveamount
        ThatPlayer.Corn = ThatPlayer.Corn - Giveamount
    if Getting is "Corn":
        ThisPlayer.Corn = ThisPlayer.Corn - Giveamount
        ThatPlayer.Corn = ThatPlayer.Corn + Giveamount
    if Giving is "Cocolate":
        ThisPlayer.Cocolate = ThisPlayer.Cocolate + Giveamount
        ThatPlayer.Cocolate = ThatPlayer.Cocolate - Giveamount
    if Getting is "Cocolate":
        ThisPlayer.Cocolate = ThisPlayer.Cocolate - Giveamount
        ThatPlayer.Cocolate = ThatPlayer.Cocolate + Giveamount
    if Giving is "Pistachios":
        ThisPlayer.Pistachios = ThisPlayer.Pistachios + Giveamount
        ThatPlayer.Pistachios = ThatPlayer.Pistachios - Giveamount
    if Getting is "Pistachios":
        ThisPlayer.Pistachios = ThisPlayer.Pistachios - Giveamount
        ThatPlayer.Pistachios = ThatPlayer.Pistachios + Giveamount
    if Giving is "Bacon":
        ThisPlayer.Bacon = ThisPlayer.Bacon + Giveamount
        ThatPlayer.Bacon = ThatPlayer.Bacon - Giveamount
    if Getting is "Bacon":
        ThisPlayer.Bacon = ThisPlayer.Bacon - Giveamount
        ThatPlayer.Bacon = ThatPlayer.Bacon + Giveamount
    if Giving is "Oysters":
        ThisPlayer.Oysters = ThisPlayer.Oysters + Giveamount
        ThatPlayer.Oysters = ThatPlayer.Oysters - Giveamount
    if Getting is "Oysters":
        ThisPlayer.Oysters = ThisPlayer.Oysters - Giveamount
        ThatPlayer.Oysters = ThatPlayer.Oysters + Giveamount
    if Giving is "Eggs":
        ThisPlayer.Eggs = ThisPlayer.Eggs + Giveamount
        ThatPlayer.Eggs = ThatPlayer.Eggs - Giveamount
    if Getting is "Eggs":
        ThisPlayer.Eggs = ThisPlayer.Eggs - Giveamount
        ThatPlayer.Eggs = ThatPlayer.Eggs + Giveamount
    if Giving is "Beef":
        ThisPlayer.Beef = ThisPlayer.Beef + Giveamount
        ThatPlayer.Beef = ThatPlayer.Beef - Giveamount
    if Getting is "Beef":
        ThisPlayer.Beef = ThisPlayer.Beef - Giveamount
        ThatPlayer.Beef = ThatPlayer.Beef + Giveamount
    if Giving is "Cherries":
        ThisPlayer.Cherries = ThisPlayer.Cherries + Giveamount
        ThatPlayer.Cherries = ThatPlayer.Cherries - Giveamount
    if Getting is "Cherries":
        ThisPlayer.Cherries = ThisPlayer.Cherries - Giveamount
        ThatPlayer.Cherries = ThatPlayer.Cherries + Giveamount
    if Giving is "Rubies":
        ThisPlayer.Rubies = ThisPlayer.Rubies + Giveamount
        ThatPlayer.Rubies = ThatPlayer.Rubies - Giveamount
    if Getting is "Rubies":
        ThisPlayer.Rubies = ThisPlayer.Rubies - Giveamount
        ThatPlayer.Rubies = ThatPlayer.Rubies + Giveamount
    if Giving is "Diamonds":
        ThisPlayer.Diamonds = ThisPlayer.Diamonds + Giveamount
        ThatPlayer.Diamonds = ThatPlayer.Diamonds - Giveamount
    if Getting is "Diamonds":
        ThisPlayer.Diamonds = ThisPlayer.Diamonds - Giveamount
        ThatPlayer.Diamonds = ThatPlayer.Diamonds + Giveamount
    if Giving is "Sapphires":
        ThisPlayer.Sapphires = ThisPlayer.Sapphires + Giveamount
        ThatPlayer.Sapphires = ThatPlayer.Sapphires - Giveamount
    if Getting is "Sapphires":
        ThisPlayer.Sapphires = ThisPlayer.Sapphires - Giveamount
        ThatPlayer.Sapphires = ThatPlayer.Sapphires + Giveamount
    if Giving is "Admantium":
        ThisPlayer.Admantium = ThisPlayer.Admantium + Giveamount
        ThatPlayer.Admantium = ThatPlayer.Admantium - Giveamount
    if Getting is "Admantium":
        ThisPlayer.Admantium = ThisPlayer.Admantium - Giveamount
        ThatPlayer.Admantium = ThatPlayer.Admantium + Giveamount
    if Giving is "Blackberries":
        ThisPlayer.Blackberries = ThisPlayer.Blackberries + Giveamount
        ThatPlayer.Blackberries = ThatPlayer.Blackberries - Giveamount
    if Getting is "Blackberries":
        ThisPlayer.Blackberries = ThisPlayer.Blackberries - Giveamount
        ThatPlayer.Blackberries = ThatPlayer.Blackberries + Giveamount
    if Giving is "Kiwi":
        ThisPlayer.Kiwi = ThisPlayer.Kiwi + Giveamount
        ThatPlayer.Kiwi = ThatPlayer.Kiwi - Giveamount
    if Getting is "Kiwi":
        ThisPlayer.Kiwi = ThisPlayer.Kiwi - Giveamount
        ThatPlayer.Kiwi = ThatPlayer.Kiwi + Giveamount
    if Giving is "Strawberries":
        ThisPlayer.Strawberries = ThisPlayer.Strawberries + Giveamount
        ThatPlayer.Strawberries = ThatPlayer.Strawberries - Giveamount
    if Getting is "Strawberries":
        ThisPlayer.Strawberries = ThisPlayer.Strawberries - Giveamount
        ThatPlayer.Strawberries = ThatPlayer.Strawberries + Giveamount
    if Giving is "Wood":
        ThisPlayer.Wood = ThisPlayer.Wood + Giveamount
        ThatPlayer.Wood = ThatPlayer.Wood - Giveamount
    if Getting is "Wood":
        ThisPlayer.Wood = ThisPlayer.Wood - Giveamount
        ThatPlayer.Wood = ThatPlayer.Wood + Giveamount
    if Giving is "Cows":
        ThisPlayer.Cows = ThisPlayer.Cows + Giveamount
        ThatPlayer.Cows = ThatPlayer.Cows - Giveamount
    if Getting is "Cows":
        ThisPlayer.Cows = ThisPlayer.Cows - Giveamount
        ThatPlayer.Wood = ThatPlayer.Cows + Giveamount
    if Giving is "Chicken":
        ThisPlayer.Chicken = ThisPlayer.Chicken + Giveamount
        ThatPlayer.Chicken = ThatPlayer.Chicken - Giveamount
    if Getting is "Chicken":
        ThisPlayer.Chicken = ThisPlayer.Chicken - Giveamount
        ThatPlayer.Chicken = ThatPlayer.Chicken + Giveamount
    if Giving is "Turkey":
        ThisPlayer.Turkey = ThisPlayer.Turkey + Giveamount
        ThatPlayer.Turkey = ThatPlayer.Turkey - Giveamount
    if Getting is "Turkey":
        ThisPlayer.Turkey = ThisPlayer.Turkey - Giveamount
        ThatPlayer.Turkey = ThatPlayer.Turkey + Giveamount
    if Giving is "Fish":
        ThisPlayer.Fish = ThisPlayer.Fish + Giveamount
        ThatPlayer.Fish = ThatPlayer.Fish - Giveamount
    if Getting is "Fish":
        ThisPlayer.Fish = ThisPlayer.Fish - Giveamount
        ThatPlayer.Fish = ThatPlayer.Fish + Giveamount
    if Giving is "Pigs":
        ThisPlayer.Pigs = ThisPlayer.Pigs + Giveamount
        ThatPlayer.Pigs = ThatPlayer.Pigs - Giveamount
    if Getting is "Pigs":
        ThisPlayer.Pigs = ThisPlayer.Pigs - Giveamount
        ThatPlayer.Pigs = ThatPlayer.Pigs + Giveamount
    if Giving is "Sheep":
        ThisPlayer.Sheep = ThisPlayer.Sheep + Giveamount
        ThatPlayer.Sheep = ThatPlayer.Sheep - Giveamount
    if Getting is "Sheep":
        ThisPlayer.Sheep = ThisPlayer.Sheep - Giveamount
        ThatPlayer.Sheep = ThatPlayer.Sheep + Giveamount
    if Giving is "Horses":
        ThisPlayer.Horses = ThisPlayer.Horses + Giveamount
        ThatPlayer.Horses = ThatPlayer.Horses - Giveamount
    if Getting is "Horses":
        ThisPlayer.Horses = ThisPlayer.Horses - Giveamount
        ThatPlayer.Horses = ThatPlayer.Horses + Giveamount
def getItem(Person, Object):
    if Object is "Gold":
        return Person.Gold
    if Object is "Silver":
        return Person.Silver
    if Object is "Bronze":
        return Person.Bronze
    if Object is "Platinum":
        return Person.Platinum
    if Object is "Uranium":
        return Person.Uranium
    if Object is "Iron":
        return Person.Iron
    if Object is "Tin":
        return Person.Tin
    if Object is "Titanium":
        return Person.Titanium
    if Object is "Vibranium":
        return Person.Vibranium
    if Object is "Ultanium":
        return Person.Ultanium
    if Object is "Bread":
        return Person.Bread
    if Object is "Sugar":
        return Person.Sugar
    if Object is "Salt":
        return Person.Salt
    if Object is "Corn":
        return Person.Corn
    if Object is "Chocolate":
        return Person.Chocolate
    if Object is "Pistachios":
        return Person.Pistachios
    if Object is "Bacon":
        return Person.Bacon
    if Object is "Oysters":
        return Person.Oysters
    if Object is "Eggs":
        return Person.Eggs
    if Object is "Beef":
        return Person.Beef
    if Object is "Cherries":
        return Person.Cherries
    if Object is "Rubies":
        return Person.Rubies
    if Object is "Diamonds":
        return Person.Diamonds
    if Object is "Sapphires":
        return Person.Sapphires
    if Object is "Admantium":
        return Person.Admantium
    if Object is "Blackberries":
        return Person.Blackberries
    if Object is "Kiwi":
        return Person.Kiwi
    if Object is "Strawberries":
        return Person.Strawberries
    if Object is "Wood":
        return Person.Wood
    if Object is "Cows":
        return Person.Cows
    if Object is "Chicken":
        return Person.Chicken
    if Object is "Turkey":
        return Person.Turkey
    if Object is "Fish":
        return Person.Fish
    if Object is "Pigs":
        return Person.Pigs
    if Object is "Sheep":
        return Person.Sheep
    if Object is "Horses":
        return Person.Horses
def Loop():
    if 1 is 1:
        First_Trader = random.randint(0, players)
        Second_Trader = random.randint(0, players)
        #if First_Trader.Interest1 in Second_Trader.Disinterest1:
            #Trade(Play[Second_Trader], Play[First_Trader], getItem(First_Trader.Interest1), random.randint(0, getItem(First_Trader.Interest1).left), 0)
        Trade(Play[Second_Trader], Play[First_Trader], getItem(First_Trader.Interest1), random.randint(0, getItem(First_Trader.Interest1).left), 0)
        Loop()
#Trade(Play[0], Play[1], 1, "Gold", 1, "Silver")
Loop()

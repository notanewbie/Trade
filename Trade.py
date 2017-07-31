import math
import random
import time
class Player(object):
    name = ""
    wants = ""
    hates = ""
    worth = float(0)
    oldworth = float(0)
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
class Material(object):
    Total = 0
    Left = 0
    Taken = 0
    Name = ""
    Worth = 0
Gold = Material()
Gold.Total = 20
Gold.Left = 20
Gold.Worth = round(100.0 / 20.0, 2)
Gold.Name = "Gold"

Silver = Material()
Silver.Total = 35
Silver.Left = 35
Silver.Worth = round(100.0 / 35.0, 2)
Silver.Name = "Silver"

Bronze = Material()
Bronze.Total = 50
Bronze.Left = 50
Bronze.Worth = round(100.0 / 50.0, 2)
Bronze.Name = "Bronze"

Platinum = Material()
Platinum.Total = 30
Platinum.Left = 30
Platinum.Worth = round(100.0 / 30.0, 2)
Platinum.Name = "Platinum"

Uranium = Material()
Uranium.Total = 10
Uranium.Left = 10
Uranium.Worth = round(100.0 / 10.0, 2)
Uranium.Name = "Uranium"

Iron = Material()
Iron.Total = 75
Iron.Left = 75
Iron.Worth = round(100.0 / 75.0, 2)
Iron.Name = "Iron"

Tin = Material()
Tin.Total = 99
Tin.Left = 99
Tin.Worth = round(100.0 / 99.0, 2)
Tin.Name = "Tin"

Titanium = Material()
Titanium.Total = 5
Titanium.Left = 5
Titanium.Worth = round(100.0 / 5.0, 2)
Titanium.Name = "Titanium"

Vibranium = Material()
Vibranium.Total = 20
Vibranium.Left = 20
Vibranium.Worth = round(100.0 / 20.0, 2)
Vibranium.Name = "Vibranium"

Ultanium = Material()
Ultanium.Total = 1
Ultanium.Left = 1
Ultanium.Worth = 100.0
Ultanium.Name = "Ultanium"

Bread = Material()
Bread.Total = 80
Bread.Left = 80
Bread.Worth = round(100.0 / 80.0, 2)
Bread.Name = "Bread"

Sugar = Material()
Sugar.Total = 60
Sugar.Left = 60
Bread.Worth = round(100.0 / 60.0, 2)
Sugar.Name = "Sugar"

Salt = Material()
Salt.Total = 40
Salt.Left = 40
Salt.Worth = round(100.0 / 60.0, 2)
Salt.Name = "Salt"

Materials = [Gold, Silver, Bronze, Platinum, Uranium, Iron, Tin, Titanium, Vibranium, Bread, Sugar, Salt]

Player1 = Player()
Player1.Name = "Player1"

Player2 = Player()
Player2.Name = "Player2"

Player3 = Player()
Player3.Name = "Player3"

Player4 = Player()
Player4.Name = "Player4"

You = Player()
print "** Please enter your name."
You.Name = raw_input("")
Players = [Player1, Player2, Player3, Player4]
Names = ["John", "Luke", "Jackson", "Steele", "Carson", "Ken", "Jack", "Lenny", "Lukas", "Patrick", "Henry", "David", "Don", "Abe", "Andrew", "Ian", "Greg", "Daniel", "Xavier", "Jonas", "Nick", "Logan", "Alex", "Zachary", "Charles", "Casey", "Lee", "Jamie", "Erik", "Tony", "Blake", "Alexei", "Francisco", "Peter", "Matt", "Wade", "Grant", "Garrett", "Fitz", "Simmons", "Archer", "Cade", "Chris", "Ryan", "Paul", "Lincoln", "Cole", "Jon", "Antoine", "Mack", "Wesley", "Lester", "Clay", "Hans", "Henri", "Isaac", "Aaron", "Sebastian", "Dominic", "Carlos", "Cameron", "Austin", "Jake", "Carter", "Nathaniel", "Nathan", "Dwight"]
given = "false"
def Advisor():
    print "@adviser: You have " + str(You.Gold) + " Gold, " + str(You.Silver) + " Silver, " + str(You.Bronze) + " Bronze, " + str(You.Platinum) + " Platinum, " + str(You.Uranium) + " Uranium, " + str(You.Iron) + " Iron, " + str(You.Tin) + " Tin, " + str(You.Titanium) + " Titanium, " + str(You.Vibranium) + " Vibranium, " + str(You.Ultanium) + " Ultanium, " + str(You.Bread) + " Bread, " + str(You.Sugar) + " Sugar and " + str(You.Salt) + " Salt."
def getCiel():
    GoldTote = float(Gold.Worth) * Gold.Total
    SilverTote = float(Silver.Worth) * Silver.Total
    BronzeTote = float(Bronze.Worth) * Bronze.Total
    PlatinumTote = float(Platinum.Worth) * Platinum.Total
    UraniumTote = float(Uranium.Worth) * Uranium.Total
    IronTote = float(Iron.Worth) * Iron.Total
    TinTote = float(Tin.Worth) * Tin.Total
    TitaniumTote = float(Titanium.Worth) * Titanium.Total
    VibraniumTote = float(Vibranium.Worth) * Vibranium.Total
    UltaniumTote = float(Ultanium.Worth) * Ultanium.Total
    BreadTote = float(Bread.Worth) * Bread.Total
    SugarTote = float(Sugar.Worth) * Sugar.Total
    SaltTote = float(Salt.Worth) * Salt.Total
    Totals = GoldTote + SilverTote + BronzeTote + PlatinumTote + UraniumTote + IronTote + TinTote + TitaniumTote + VibraniumTote + UltaniumTote + BreadTote + SaltTote
    return Totals
def getWorth(Thing):
    if Thing in "Gold" or "Gold" in Thing:
        return Gold.Worth
    if Thing in "Silver" or "Silver" in Thing:
        return Silver.Worth
    if Thing in "Platinum" or "Platinum" in Thing:
        return Platinum.Worth
    if Thing in "Bronze" or "Bronze" in Thing:
        return Bronze.Worth
    if Thing in "Uranium" or "Uranium" in Thing:
        return Uranium.Worth
    if Thing in "Iron" or "Iron" in Thing:
        return Iron.Worth
    if Thing in "Tin" or "Tin" in Thing:
        return Tin.Worth
    if Thing in "Titanium" or "Titanium" in Thing:
        return Titanium.Worth
    if Thing in "Vibranium" or "Vibranium" in Thing:
        return Vibranium.Worth
    if Thing in "Ultanium" or "Ultanium" in Thing:
        return Ultanium.Worth
    if Thing in "Bread" or "Bread" in Thing:
        return Bread.Worth
    if Thing in "Sugar" or "Sugar" in Thing:
        return Sugar.Worth
    if Thing in "Salt" or "Salt" in Thing:
        return Salt.Worth
        i = i + 1
def getTotal(Thing):
    if Thing in "Gold" or "Gold" in Thing:
        return Gold.Total
    if Thing in "Silver" or "Silver" in Thing:
        return Silver.Total
    if Thing in "Platinum" or "Platinum" in Thing:
        return Platinum.Total
    if Thing in "Bronze" or "Bronze" in Thing:
        return Bronze.Total
    if Thing in "Uranium" or "Uranium" in Thing:
        return Uranium.Total
    if Thing in "Iron" or "Iron" in Thing:
        return Iron.Total
    if Thing in "Tin" or "Tin" in Thing:
        return Tin.Total
    if Thing in "Titanium" or "Titanium" in Thing:
        return Titanium.Total
    if Thing in "Vibranium" or "Vibranium" in Thing:
        return Titanium.Total
    if Thing in "Ultanium" or "Ultanium" in Thing:
        return Ultanium.Total
    if Thing in "Bread" or "Bread" in Thing:
        return Bread.Total
    if Thing in "Sugar" or "Sugar" in Thing:
        return Sugar.Total
    if Thing in "Salt" or "Salt" in Thing:
        return Salt.Total
        i = i + 1
def getFair(Thing1, Thing2):
    i = 0
    try:
        Worth1 = getTotal(Thing1)
        Worth2 = getTotal(Thing2)
        Worth1 = Worth1 * 100
        Worth2 = Worth2 * 100
        #print Worth2
        #print Worth1
        result = float(Worth2) / Worth1
        #print result
        return result
    except TypeError:
        print "!! Error finding fair market values for " + Thing1 + " and " + Thing2 + "."
        return 0
def getMaterial(Thing):
    newLine()
    i = 0
    for item in Materials:
        if Thing in Materials[i].Name:
            return Materials[i]
        i = i + 1
def takeMaterial(Thing, Ammount):
    newLine()
    i = 0
    for item in Materials:
        if Thing in Materials[i].Name:
            Materials[i].Left = Materials[i].Left - Ammount
            print "** Took " + str(Ammount) + " " + Thing + " from the bank."
            print "** There is now " + str(Materials[i].Left) + " " + Thing + " left."
        i = i + 1
def giveMaterial(Thing, Ammount):
    newLine()
    i = 0
    for item in Materials:
        if Thing in Materials[i].Name:
            Materials[i].Left = Materials[i].Left + Ammount
            print "** Put " + str(Ammount) + " " + Thing + " in the bank."
            print "** There is now " + str(Materials[i].Left) + " " + Thing + " left."
        i = i + 1
def givePlayer(Player, Thing, Ammount):
    newLine()
    i = 0
    given = "false"
    for item in Players:
        if Player in Players[i].Name and "false" in given:
            if "Gold" in Thing or Thing in "Gold":
                Players[i].Gold = Players[i].Gold + Ammount
                print "** Gave " + Player + " " + str(Ammount) + " " + Thing + "."
                while Ammount > 0:
                    Players[i].worth = Players[i].worth + float(getWorth(Thing))
                    Ammount = Ammount - 1
                while Ammount < 0:
                    Players[i].worth = Players[i].worth - getWorth(Thing)
                    Ammount = Ammount + 1
                print "** " + Player + " now has " + str(Players[i].Gold) + " " + Thing + "."
                given = "true"
            if "Platinum" in Thing or Thing in "Platinum":
                Players[i].Platinum = Players[i].Platinum + Ammount
                print "** Gave " + Player + " " + str(Ammount) + " " + Thing + "."
                while Ammount > 0:
                    Players[i].worth = Players[i].worth + getWorth(Thing)
                    Ammount = Ammount - 1
                while Ammount < 0:
                    Players[i].worth = Players[i].worth - getWorth(Thing)
                    Ammount = Ammount + 1
                print "** " + Player + " now has " + str(Players[i].Platinum) + " " + Thing + "."
                given = "true"
            if "Silver" in Thing or Thing in "Silver":
                Players[i].Silver = Players[i].Silver + Ammount
                print "** Gave " + Player + " " + str(Ammount) + " " + Thing + "."
                while Ammount > 0:
                    Players[i].worth = Players[i].worth + getWorth(Thing)
                    Ammount = Ammount - 1
                while Ammount < 0:
                    Players[i].worth = Players[i].worth - getWorth(Thing)
                    Ammount = Ammount + 1
                print "** " + Player + " now has " + str(Players[i].Silver) + " " + Thing + "."
                given = "true"
            if "Bronze" in Thing or Thing in "Bronze":
                Players[i].Bronze = Players[i].Bronze + Ammount
                print "** Gave " + Player + " " + str(Ammount) + " " + Thing + "."
                while Ammount > 0:
                    Players[i].worth = Players[i].worth + getWorth(Thing)
                    Ammount = Ammount - 1
                while Ammount < 0:
                    Players[i].worth = Players[i].worth - getWorth(Thing)
                    Ammount = Ammount + 1
                print "** " + Player + " now has " + str(Players[i].Bronze) + " " + Thing + "."
                given = "true"
            if "Uranium" in Thing or Thing in "Uranium":
                Players[i].Uranium = Players[i].Uranium + Ammount
                print "** Gave " + Player + " " + str(Ammount) + " " + Thing + "."
                while Ammount > 0:
                    Players[i].worth = Players[i].worth + getWorth(Thing)
                    Ammount = Ammount - 1
                while Ammount < 0:
                    Players[i].worth = Players[i].worth - getWorth(Thing)
                    Ammount = Ammount + 1
                print "** " + Player + " now has " + str(Players[i].Uranium) + " " + Thing + "."
                given = "true"
            if "Iron" in Thing or Thing in "Iron":
                Players[i].Iron = Players[i].Iron + Ammount
                print "** Gave " + Player + " " + str(Ammount) + " " + Thing + "."
                while Ammount > 0:
                    Players[i].worth = Players[i].worth + getWorth(Thing)
                    Ammount = Ammount - 1
                while Ammount < 0:
                    Players[i].worth = Players[i].worth - getWorth(Thing)
                    Ammount = Ammount + 1
                print "** " + Player + " now has " + str(Players[i].Iron) + " " + Thing + "."
                given = "true"
            if "Tin" in Thing or Thing in "Tin":
                Players[i].Tin = Players[i].Tin + Ammount
                print "** Gave " + Player + " " + str(Ammount) + " " + Thing + "."
                while Ammount > 0:
                    Players[i].worth = Players[i].worth + getWorth(Thing)
                    Ammount = Ammount - 1
                while Ammount < 0:
                    Players[i].worth = Players[i].worth - getWorth(Thing)
                    Ammount = Ammount + 1
                print "** " + Player + " now has " + str(Players[i].Tin) + " " + Thing + "."
                given = "true"
            if "Titanium" in Thing or Thing in "Titanium":
                Players[i].Titanium = Players[i].Titanium + Ammount
                print "** Gave " + Player + " " + str(Ammount) + " " + Thing + "."
                while Ammount > 0:
                    Players[i].worth = Players[i].worth + getWorth(Thing)
                    Ammount = Ammount - 1
                while Ammount < 0:
                    Players[i].worth = Players[i].worth - getWorth(Thing)
                    Ammount = Ammount + 1
                print "** " + Player + " now has " + str(Players[i].Titanium) + " " + Thing + "."
                given = "true"
            if "Vibranium" in Thing or Thing in "Vibranium":
                Players[i].Vibranium = Players[i].Vibranium + Ammount
                print "** Gave " + Player + " " + str(Ammount) + " " + Thing + "."
                while Ammount > 0:
                    Players[i].worth = Players[i].worth + getWorth(Thing)
                    Ammount = Ammount - 1
                while Ammount < 0:
                    Players[i].worth = Players[i].worth - getWorth(Thing)
                    Ammount = Ammount + 1
                print "** " + Player + " now has " + str(Players[i].Vibranium) + " " + Thing + "."
                given = "true"
            if "Ultanium" in Thing or Thing in "Ultanium":
                Players[i].Ultanium = Players[i].Ultanium + Ammount
                print "** Gave " + Player + " " + str(Ammount) + " " + Thing + "."
                while Ammount > 0:
                    Players[i].worth = Players[i].worth + getWorth(Thing)
                    Ammount = Ammount - 1
                while Ammount < 0:
                    Players[i].worth = Players[i].worth - getWorth(Thing)
                    Ammount = Ammount + 1
                print "** " + Player + " now has " + str(Players[i].Ultanium) + " " + Thing + "."
                given = "true"
            if "Bread" in Thing or Thing in "Bread":
                Players[i].Bread = Players[i].Bread + Ammount
                print "** Gave " + Player + " " + str(Ammount) + " " + Thing + "."
                while Ammount > 0:
                    Players[i].worth = Players[i].worth + getWorth(Thing)
                    Ammount = Ammount - 1
                while Ammount < 0:
                    Players[i].worth = Players[i].worth - getWorth(Thing)
                    Ammount = Ammount + 1
                print "** " + Player + " now has " + str(Players[i].Bread) + " " + Thing + "."
                given = "true"
            if "Sugar" in Thing or Thing in "Sugar":
                Players[i].Sugar = Players[i].Sugar + Ammount
                print "** Gave " + Player + " " + str(Ammount) + " " + Thing + "."
                while Ammount > 0:
                    Players[i].worth = Players[i].worth + getWorth(Thing)
                    Ammount = Ammount - 1
                while Ammount < 0:
                    Players[i].worth = Players[i].worth - getWorth(Thing)
                    Ammount = Ammount + 1
                print "** " + Player + " now has " + str(Players[i].Sugar) + " " + Thing + "."
                given = "true"
            if "Salt" in Thing or Thing in "Salt":
                Players[i].Salt = Players[i].Salt + Ammount
                print "** Gave " + Player + " " + str(Ammount) + " " + Thing + "."
                while Ammount > 0:
                    Players[i].worth = Players[i].worth + getWorth(Thing)
                    Ammount = Ammount - 1
                while Ammount < 0:
                    Players[i].worth = Players[i].worth - getWorth(Thing)
                    Ammount = Ammount + 1
                print "** " + Player + " now has " + str(Players[i].Salt) + " " + Thing + "."
                given = "true"
        i = i + 1
    if Player in You.Name:
            if "Gold" in Thing or Thing in "Gold":
                You.Gold = You.Gold + Ammount
                print "** Gave " + Player + " " + str(Ammount) + " " + Thing + "."
                while Ammount > 0:
                    You.worth = You.worth + getWorth(Thing)
                    Ammount = Ammount - 1
                while Ammount < 0:
                    You.worth = You.worth - getWorth(Thing)
                    Ammount = Ammount + 1
                given = "true"
                print "** " + Player + " now has " + str(You.Gold) + " " + Thing + "."
            if "Platinum" in Thing or Thing in "Platinum":
                You.Platinum = You.Platinum + Ammount
                print "** Gave " + Player + " " + str(Ammount) + " " + Thing + "."
                while Ammount > 0:
                    You.worth = You.worth + getWorth(Thing)
                    Ammount = Ammount - 1
                while Ammount < 0:
                    You.worth = You.worth - getWorth(Thing)
                    Ammount = Ammount + 1
                given = "true"
                print "** " + Player + " now has " + str(You.Platinum) + " " + Thing + "."
            if "Silver" in Thing or Thing in "Silver":
                You.Silver = You.Silver + Ammount
                print "** Gave " + Player + " " + str(Ammount) + " " + Thing + "."
                while Ammount > 0:
                    You.worth = You.worth + getWorth(Thing)
                    Ammount = Ammount - 1
                while Ammount < 0:
                    You.worth = You.worth - getWorth(Thing)
                    Ammount = Ammount + 1
                given = "true"
                print "** " + Player + " now has " + str(You.Silver) + " " + Thing + "."
            if "Bronze" in Thing or Thing in "Bronze":
                You.Bronze = You.Bronze + Ammount
                print "** Gave " + Player + " " + str(Ammount) + " " + Thing + "."
                while Ammount > 0:
                    You.worth = You.worth + getWorth(Thing)
                    Ammount = Ammount - 1
                while Ammount < 0:
                    You.worth = You.worth - getWorth(Thing)
                    Ammount = Ammount + 1
                given = "true"
                print "** " + Player + " now has " + str(You.Bronze) + " " + Thing + "."
            if "Uranium" in Thing or Thing in "Uranium":
                You.Uranium = You.Uranium + Ammount
                print "** Gave " + Player + " " + str(Ammount) + " " + Thing + "."
                while Ammount > 0:
                    You.worth = You.worth + getWorth(Thing)
                    Ammount = Ammount - 1
                while Ammount < 0:
                    You.worth = You.worth - getWorth(Thing)
                    Ammount = Ammount + 1
                given = "true"
                print "** " + Player + " now has " + str(You.Uranium) + " " + Thing + "."
            if "Iron" in Thing or Thing in "Iron":
                You.Iron = You.Iron + Ammount
                print "** Gave " + Player + " " + str(Ammount) + " " + Thing + "."
                while Ammount > 0:
                    You.worth = You.worth + getWorth(Thing)
                    Ammount = Ammount - 1
                while Ammount < 0:
                    You.worth = You.worth - getWorth(Thing)
                    Ammount = Ammount + 1
                given = "true"
                print "** " + Player + " now has " + str(You.Iron) + " " + Thing + "."
            if "Tin" in Thing or Thing in "Tin":
                You.Tin = You.Tin + Ammount
                print "** Gave " + Player + " " + str(Ammount) + " " + Thing + "."
                while Ammount > 0:
                    You.worth = You.worth + getWorth(Thing)
                    Ammount = Ammount - 1
                while Ammount < 0:
                    You.worth = You.worth - getWorth(Thing)
                    Ammount = Ammount + 1
                given = "true"
                print "** " + Player + " now has " + str(You.Tin) + " " + Thing + "."
            if "Titanium" in Thing or Thing in "Titanium":
                You.Titanium = You.Titanium + Ammount
                print "** Gave " + Player + " " + str(Ammount) + " " + Thing + "."
                while Ammount > 0:
                    You.worth = You.worth + getWorth(Thing)
                    Ammount = Ammount - 1
                while Ammount < 0:
                    You.worth = You.worth - getWorth(Thing)
                    Ammount = Ammount + 1
                given = "true"
                print "** " + Player + " now has " + str(You.Titanium) + " " + Thing + "."
            if "Vibranium" in Thing or Thing in "Vibranium":
                You.Vibranium = You.Vibranium + Ammount
                print "** Gave " + Player + " " + str(Ammount) + " " + Thing + "."
                while Ammount > 0:
                    You.worth = You.worth + getWorth(Thing)
                    Ammount = Ammount - 1
                while Ammount < 0:
                    You.worth = You.worth - getWorth(Thing)
                    Ammount = Ammount + 1
                given = "true"
                print "** " + Player + " now has " + str(You.Vibranium) + " " + Thing + "."
            if "Ultanium" in Thing or Thing in "Ultanium":
                You.Ultanium = You.Ultanium + Ammount
                print "** Gave " + Player + " " + str(Ammount) + " " + Thing + "."
                while Ammount > 0:
                    You.worth = You.worth + getWorth(Thing)
                    Ammount = Ammount - 1
                while Ammount < 0:
                    You.worth = You.worth - getWorth(Thing)
                    Ammount = Ammount + 1
                given = "true"
                print "** " + Player + " now has " + str(You.Ultanium) + " " + Thing + "."
            if "Bread" in Thing or Thing in "Bread":
                You.Bread = You.Bread + Ammount
                print "** Gave " + Player + " " + str(Ammount) + " " + Thing + "."
                while Ammount > 0:
                    You.worth = You.worth + getWorth(Thing)
                    Ammount = Ammount - 1
                while Ammount < 0:
                    You.worth = You.worth - getWorth(Thing)
                    Ammount = Ammount + 1
                given = "true"
                print "** " + Player + " now has " + str(You.Bread) + " " + Thing + "."
            if "Sugar" in Thing or Thing in "Sugar":
                You.Sugar = You.Sugar + Ammount
                print "** Gave " + Player + " " + str(Ammount) + " " + Thing + "."
                while Ammount > 0:
                    You.worth = You.worth + getWorth(Thing)
                    Ammount = Ammount - 1
                while Ammount < 0:
                    You.worth = You.worth - getWorth(Thing)
                    Ammount = Ammount + 1
                given = "true"
                print "** " + Player + " now has " + str(You.Sugar) + " " + Thing + "."
            if "Salt" in Thing or Thing in "Salt":
                You.Salt = You.Salt + Ammount
                print "** Gave " + Player + " " + str(Ammount) + " " + Thing + "."
                while Ammount > 0:
                    You.worth = You.worth + getWorth(Thing)
                    Ammount = Ammount - 1
                while Ammount < 0:
                    You.worth = You.worth - getWorth(Thing)
                    Ammount = Ammount + 1
                given = "true"
                print "** " + Player + " now has " + str(You.Salt) + " " + Thing + "."


def Deal():
    global Player1
    global Player2
    global Player3
    global Player4
    global You
    n = 0
    for item in Players:
        Players[n].Name = Names[random.randint(0, len(Names) - 1)]
        Players[n].wants = Materials[random.randint(0, len(Materials) - 1)].Name
        #print Players[n].Name + " wants " + Players[n].wants
        n = n + 1
    i = 0
    lenPlay = 0
    for item in Players:
        lenPlay = lenPlay + 1
    for item in Materials:
        n = 0
        for item in Players:
            if Materials[i].Left / lenPlay < 5:
                giving = random.randint(0, int(Materials[i].Left * .7))
                #print giving
            else:
                giving = random.randint(0, int(Materials[i].Left * .7))
                #print giving
            givePlayer(Players[n].Name, Materials[i].Name, giving)
            takeMaterial(Materials[i].Name, giving)
            n = n + 1
        if Materials[i].Left > 1:
            giving = Materials[i].Left
            givePlayer(You.Name, Materials[i].Name, giving)
            takeMaterial(Materials[i].Name, giving)
        i = i + 1
    Num = random.randint(0, 4)
    if Num is 4:
        givePlayer(You.Name, "Ultanium", 1)
    else:
        givePlayer(Players[Num].Name, "Ultanium", 1)
def newLine():
    print ""
def getReport():
    i = 0
    newLine()
    print "** Market Report:"
    for item in Players:
        newLine()
        change = Players[i].worth - Players[i].oldworth
        if change >= 0:
            print "** " + Players[i].Name + ": " + str(Players[i].worth) + "m +" + str(change)
        else:
            print "** " + Players[i].Name + ": " + str(Players[i].worth) + "m " + str(change)
        Players[i].oldworth = Players[i].worth
        i = i + 1
    newLine()
    change = You.worth - You.oldworth
    if change >= 0:
        print "** " + You.Name + ": " + str(You.worth) + "m +" + str(change)
    else:
        print "** " + You.Name + ": " + str(You.worth) + "m " + str(change)
    You.oldworth = You.worth
    i = 0
    Ciel = getCiel()
    limit = getCiel() * .75
    newLine()
    print "**PSA: You need " + str(limit) + "m to win."
    for item in Players:
        if Players[i].worth >= limit:
            print "** " + Players[i].Name + " has won the game! Press enter to exit."
            exit()
            raw_input("")
            one = 0
            i = i + 1
        elif You.worth >= limit:
            print "** " + You.Name + " has won the game! Press enter to exit."
            exit()
            raw_input("")
            one = 0
    newLine()
turn = 0
Deal()
one = 1
while one > 0:
    turn = turn + 1
    print "** Round #" + str(turn)
    getReport()
    newLine()
    print "** It's your turn. Would you like to trade?"
    response = raw_input()
    response = response.upper()
    if "NO" in response or "PASS" in response:
        print "** " + You.Name + " passes."
    elif "YES" in response:
        print "** How would you like to trade? example: Give 1 Gold"
        Advisor()
        response = raw_input()
        response = response.split(" ")
        try:
            print You.Name + " is looking to give away " + response[1] + " " + response[2] + "."
            e = "no"
        except IndexError:
            print You.Name + " passes."
            e = "yep"
            response = [" ", " ", " "]
        n = 0
        for item in Players:
            if Players[n].wants in response[2] or response[2] in Players[n].wants and "no" in e and "-" not in response[1]:
                chosen = ["Gold", "Silver", "Bronze", "Platinum", "Uranium", "Iron", "Tin", "Titanium", "Vibranium", "Ultanium"]
                chosen = chosen[random.randint(0, len(chosen) - 1)]
                #print chosen
                giving = 0
                if "Gold" in chosen and Players[n].Gold > 0:
                    giving = random.randint(0, int(Players[n].Gold * .7))
                if "Silver" in chosen and Players[n].Silver > 0:
                    giving = random.randint(0, int(Players[n].Silver * .7))
                if "Bronze" in chosen and Players[n].Bronze > 0:
                    giving = random.randint(0, int(Players[n].Bronze * .7))
                if "Platinum" in chosen and Players[n].Platinum > 0:
                    giving = random.randint(0, int(Players[n].Platinum * .7))
                if "Uranium" in chosen and Players[n].Uranium > 0:
                    giving = random.randint(0, int(Players[n].Uranium * .7))
                if "Iron" in chosen and Players[n].Iron > 0:
                    giving = random.randint(0, int(Players[n].Iron * .7))
                if "Tin" in chosen and Players[n].Tin > 0:
                    giving = random.randint(0, int(Players[n].Iron * .7))
                if "Titanium" in chosen and Players[n].Titanium > 0:
                    giving = random.randint(0, int(Players[n].Titanium * .7))
                if "Vibranium" in chosen and Players[n].Vibranium > 0:
                    giving = random.randint(0, int(Players[n].Vibranium * .7))
                if "Ultanium" in chosen and Players[n].Ultanium > 0:
                    giving = random.randint(0, int(Players[n].Ultanium * .7))
                if "Bread" in chosen and Players[n].Bread > 0:
                    giving = random.randint(0, int(Players[n].Bread * .7))
                if "Sugar" in chosen and Players[n].Sugar > 0:
                    giving = random.randint(0, int(Players[n].Sugar * .7))
                if "Salt" in chosen and Players[n].Salt > 0:
                    giving = random.randint(0, int(Players[n].Salt * .7))
                if giving > 0 and response[1] > 0 and int(response[1]) > 0 and int(response[1]) < 1000:
                    time.sleep(1)
                    print "** " + Players[n].Name + " accepts your offer. He wishes to give you " + str(giving) + " " + chosen + " in return. Do you accept?"
                    yn = raw_input()
                    yn = yn.upper()
                    if "YES" in yn:
                        givePlayer(Players[n].Name, response[2], int(response[1]))
                        givePlayer(You.Name, response[2], int(response[1]) * -1)

                        givePlayer(Players[n].Name, chosen, giving * -1)
                        givePlayer(You.Name, chosen, giving)
                    if "NO" in yn:
                        print "** " + You.Name + " passes."
                if "n" in e:
                    time.sleep(1)
                    print "** " + Players[n].Name + " passes."
                else:
                    e = e
            else:
                time.sleep(1)
                print "** " + Players[n].Name + " passes."
            n = n + 1
    n = 0
    for item in Players:
        print "** It's " + Players[n].Name + "'s turn."
        time.sleep(1)
        Chance = ["Gold", "Silver", "Bronze", "Platinum", "Uranium", "Iron", "Tin", "Titanium", "Vibranium", "Ultanium", "Bread", "Sugar", "Salt"]
        choice = random.randint(0, 3)
        decision = Chance[choice]
        giving = 0
        if "Gold" in decision and Players[n].Gold > 0:
            giving = random.randint(0, Players[n].Gold)
        if "Silver" in decision and Players[n].Silver > 0:
            giving = random.randint(0, Players[n].Silver)
        if "Bronze" in decision and Players[n].Bronze > 0:
            giving = random.randint(0, Players[n].Bronze)
        if "Platinum" in decision and Players[n].Platinum > 0:
            giving = random.randint(0, Players[n].Platinum)
        if "Uranium" in decision and Players[n].Uranium > 0:
            giving = random.randint(0, Players[n].Uranium)
        if "Iron" in decision and Players[n].Iron > 0:
            giving = random.randint(0, Players[n].Iron)
        if "Tin" in decision and Players[n].Tin > 0:
            giving = random.randint(0, Players[n].Tin)
        if "Titanium" in decision and Players[n].Titanium > 0:
            giving = random.randint(0, Players[n].Titanium)
        if "Vibranium" in decision and Players[n].Vibranium > 0:
            giving = random.randint(0, Players[n].Vibranium)
        if "Ultanium" in decision and Players[n].Ultanium > 0:
            giving = random.randint(0, Players[n].Ultanium)
        if "Bread" in decision and Players[n].Bread > 0:
            giving = random.randint(0, Players[n].Bread)
        if "Sugar" in decision and Players[n].Sugar > 0:
            giving = random.randint(0, Players[n].Sugar)
        if "Salt" in decision and Players[n].Salt > 0:
            giving = random.randint(0, Players[n].Salt)
        if giving < 1:
            time.sleep(1)
            print  "** " + Players[n].Name + " passes."
        else:
            print "** " + Players[n].Name + " is looking to give away " + str(giving) + " " + decision + "."
            print "@insider: " + Players[n].Name + " wants " + Players[n].wants
            print "@advisor: 1 " + decision + " is worth " + str(getWorth(decision)) + "m."
            #
            b = 0
            shout = 0
            for item in Players:
                if Players[b].wants in decision:
                    givin = 0
                    giveaway = random.randint(0, len(Materials) - 1)
                    giveaway = Materials[giveaway].Name
                    if "Gold" in giveaway and Players[b].Gold > 0:
                        givin = random.randint(0, int(Players[b].Gold * .7))
                    if "Silver" in giveaway and Players[b].Silver > 0:
                        givin = random.randint(0, int(Players[b].Silver * .7))
                    if "Bronze" in giveaway and Players[b].Bronze > 0:
                        givin = random.randint(0, int(Players[b].Bronze * .7))
                    if "Platinum" in giveaway and Players[b].Platinum > 0:
                        givin = random.randint(0, int(Players[b].Platinum * .7))
                    if "Uranium" in giveaway and Players[b].Uranium > 0:
                        givin = random.randint(0, int(Players[b].Uranium * .7))
                    if "Iron" in giveaway and Players[b].Iron > 0:
                        givin = random.randint(0, int(Players[b].Iron * .7))
                    if "Tin" in giveaway and Players[b].Tin > 0:
                        givin = random.randint(0, int(Players[b].Tin * .7))
                    if "Titanium" in giveaway and Players[b].Titanium > 0:
                        givin = random.randint(0, int(Players[b].Titanium * .7))
                    if "Vibranium" in giveaway and Players[b].Vibranium > 0:
                        givin = random.randint(0, int(Players[b].Vibranium * .7))
                    if "Ultanium" in giveaway and Players[b].Ultanium > 0:
                        givin = random.randint(0, int(Players[b].Ultanium * .7))
                    if "Bread" in giveaway and Players[b].Bread > 0:
                        givin = random.randint(0, int(Players[b].Bread * .7))
                    if "Sugar" in giveaway and Players[b].Sugar > 0:
                        givin = random.randint(0, int(Players[b].Sugar * .7))
                    if "Salt" in giveaway and Players[b].Salt > 0:
                        givin = random.randint(0, int(Players[b].Salt * .7))
                    if givin > 0:
                        if Players[n].wants in Players[b].wants and shout == 0:
                            print "@troll Ha! " + Players[n].Name + " is giving away the very thing he wants!"
                            shout = 1
                        else:
                            print "** " + Players[b].Name + " accepts " + Players[n].Name + "'s offer. He wishes to give him " + str(givin) + " " + giveaway + " in return. Do you accept?"
                            yn = ""
                            if giveaway in Players[n].wants or getFair(giveaway, Players[n].wants) * giving <= int(givin):
                                yn = "yes"
                            else:
                                yn = "no"
                            #print yn
                            yn = yn.upper()
                            if "YES" in yn:
                                print "yes"
                                givePlayer(Players[b].Name, decision, giving)
                                givePlayer(Players[n].Name, decision, giving * -1)
                                
                                givePlayer(Players[n].Name, giveaway, givin)
                                givePlayer(Players[b].Name, giveaway, givin * -1)
                            if "NO" in yn:
                                print "** " + Players[n].Name + " declines the offer."
                    if givin < 1:
                        time.sleep(1)
                        print "** " + Players[b].Name + " passes."
                else:
                    time.sleep(1)
                    print "** " + Players[b].Name + " passes."
                b = b + 1
            #
            print "** Do you accept " + Players[n].Name + "'s offer?"
            response = raw_input("")
            response = response.upper()
            try:
                response = response.split(" ")
                response0 = int(response[0])
            except ValueError:
                response0 = 0
            if "YES" in response:
                if giving > 1:
                    print "@advisor: " + str(giving) + " " + decision + " are worth " + str(getFair(decision, Players[n].wants) * giving) + " " + Players[n].wants + "."
                else:
                    print "@advisor: " + str(giving) + " " + decision + " is worth " + str(getFair(decision, Players[n].wants) * giving) + " " + Players[n].wants + "."
                print "** What will you offer in return?"
                Advisor()
                response = raw_input("")
                response = response.upper()
                response = response.split(" ")
                j = 0
                passed = "false"
                try:
                    inter = int(response[0])
                    #inter1 = int(response[1])
                except ValueError:
                    response = [response[0], "0", " "]
                except IndexError:
                    response = response + " cut it cut "
                    response.split(" ")
                for item in response:
                    dont = "nvm"
                    try:
                        response[j] = response[j]
                    except TypeError:
                        dont = "go"
                    if "nvm" in dont:
                        if "PASS" in response[j]:
                            print "** " + You.Name + " passes."
                            passed = "true"
                    response[j] = response[j].capitalize()
                    j = j + 1
                huh = 0
                #print response[0]
                try:
                    huh = int(response[0])
                except ValueError:
                    response[0] = 0
                if "true" in passed:
                    j = j
                elif response[1] in Players[n].wants or getFair(response[1], Players[n].wants) * giving <= int(response[0]):
                    if getFair(response[1], Players[n].wants) * giving < int(response[0]):
                        print "@troll lol check this out! " + Players[n].Name + " just ripped off " + You.Name + "!!"
                        print "** " + You.Name + " accepts " + " " + Players[n].Name + "'s offer."
                        givePlayer(You.Name, decision, giving)  
                        givePlayer(Players[n].Name, decision, giving * -1)
                        givePlayer(You.Name, response[1], int(response[0]) * -1)
                        givePlayer(Players[n].Name, response[1], int(response[0]))
                    elif getFair(decision, Players[n].wants) * giving - 3 >= int(response[0]):
                        print "** " + Players[n].Name + " think you're trying to cheat him."
                        print "** " + Players[n].Name + " backs out of the deal."
                    elif int(response[0]) < 1:
                        print "** " + Players[n].Name + " think you're trying to cheat him."
                        print "** " + Players[n].Name + " backs out of the deal."
                    else:
                        print "** " + You.Name + " accepts " + " " + Players[n].Name + "'s offer."
                        givePlayer(You.Name, decision, giving)
                        givePlayer(Players[n].Name, decision, giving * -1)
                        givePlayer(You.Name, response[1], int(response[0]) * -1)
                        givePlayer(Players[n].Name, response[1], int(response[0]))
                else:
                    print "** " + Players[n].Name + " doesn't want " + response[1] + "."
                    print "** " + Players[n].Name + " backs out of the deal."
            if "NO" in response:
                print "** " + You.Name + " passes."
        n = n + 1
Deal()

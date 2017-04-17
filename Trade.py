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
class Material(object):
    Total = 0
    Left = 0
    Taken = 0
    Name = ""
    Worth = 0
Gold = Material()
Gold.Total = 20
Gold.Left = 20
Gold.Worth = .05
Gold.Name = "Gold"

Silver = Material()
Silver.Total = 35
Silver.Left = 35
Silver.Worth = .03
Silver.Name = "Silver"

Bronze = Material()
Bronze.Total = 50
Bronze.Left = 50
Bronze.Worth = .02
Bronze.Name = "Bronze"

Platinum = Material()
Platinum.Total = 30
Platinum.Left = 30
Platinum.Worth = .03
Platinum.Name = "Platinum"

Materials = [Gold, Silver, Bronze, Platinum]

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
Names = ["John", "Luke", "Jackson", "Steele", "Carson", "Ken", "Jack", "Lenny", "Lukas", "Patrick", "Henry", "David", "Don", "Abe", "Andrew", "Ian", "Greg", "Daniel", "Xavier", "Jonas", "Nick", "Logan", "Alex", "Zachary", "Charles", "Casey", "Lee", "Jamie", "Erik", "Tony", "Blake", "Alexei", "Francisco", "Peter", "Matt", "Wade", "Grant", "Garrett", "Fitz", "Simmons", "Archer", "Cade", "Chris", "Ryan", "Paul", "Lincoln", "Cole", "Jon", "Antoine", "Mack", "Wesley", "Lester", "Clay", "Hans", "Henri", "Isaac", "Aaron", "Sebastian", "Dominic", "Carlos", "Cameron", "Austin", "Jake", "Carter", "Nathaniel", "Nathan"]
given = "false"
def getCiel():
    GoldTote = float(Gold.Worth) * Gold.Total
    SilverTote = float(Silver.Worth) * Silver.Total
    BronzeTote = float(Bronze.Worth) * Bronze.Total
    PlatinumTote = float(Platinum.Worth) * Platinum.Total
    Totals = GoldTote + SilverTote + BronzeTote + PlatinumTote
    return Totals
def getWorth(Thing):
    if Thing in "Gold":
        return Gold.Worth
    if Thing in "Silver":
        return Silver.Worth
    if Thing in "Platinum":
        return Platinum.Worth
    if Thing in "Bronze":
        return Bronze.Worth
        i = i + 1
def getTotal(Thing):
    if Thing in "Gold":
        return Gold.Total
    if Thing in "Silver":
        return Silver.Total
    if Thing in "Platinum":
        return Platinum.Total
    if Thing in "Bronze":
        return Bronze.Total
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
            if "Gold" in Thing:
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
            if "Platinum" in Thing:
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
            if "Silver" in Thing:
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
            if "Bronze" in Thing:
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
        i = i + 1
    if Player in You.Name:
            if "Gold" in Thing:
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
            if "Platinum" in Thing:
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
            if "Silver" in Thing:
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
            if "Bronze" in Thing:
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
                giving = random.randint(0, int(Materials[i].Left * .5))
            else:
                giving = random.randint(0, int(Materials[i].Left * .6))
            givePlayer(Players[n].Name, Materials[i].Name, giving)
            takeMaterial(Materials[i].Name, giving)
            n = n + 1
        giving = Materials[i].Left
        givePlayer(You.Name, Materials[i].Name, giving)
        takeMaterial(Materials[i].Name, giving)
        i = i + 1
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
            raw_input("")
            one = 0
            i = i + 1
        elif You.worth >= limit:
            print "** " + You.Name + " has won the game! Press enter to exit."
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
        print "@adviser: You have " + str(You.Gold) + " Gold, " + str(You.Silver) + " Silver, " + str(You.Bronze) + " Bronze and " + str(You.Platinum) + " Platinum."
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
            if Players[n].wants in response[2] and "no" in e:
                chosen = ["Gold", "Silver", "Bronze", "Platinum"]
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
                if giving > 0 and response[1] > 0:
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
        Chance = ["Gold", "Silver", "Bronze", "Platinum"]
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
                print "@adviser: You have " + str(You.Gold) + " Gold, " + str(You.Silver) + " Silver, " + str(You.Bronze) + " Bronze and " + str(You.Platinum) + " Platinum."
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

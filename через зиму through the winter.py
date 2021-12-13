from os import system
myCoolTitle = "через зиму"
system("title "+myCoolTitle)
import random
from os import system, name 
import time
#clearing definition
def clear(): 
      # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux
    else: 
        _ = system('clear')
#stat presets
healthcare = 0
money = 5000
income = 0
inhabitants = 30
jobs = 0
wealth = 1
food = 30
rounds = 0
achievementinhabitants = 1
achievementhealthcare = 1
#game loop
while True:
    #event system
    PEOpayment = 0
    event = random.randint(0, 49)
    print(event)
    #plague event
    if event == 1:
        if healthcare >= wealth//2:
            print("Ein Virus hat deine Einwohner infiziert,")
            print("wenn du deine Einwohner retten möchtest musst du Impfstoff herstellen.")
            action = input("Aber sei vorsichtig, es kann viel kosten. Wenn du den Impfstoff nicht kaufst werden deine Einwohner sterben. (Y/N)")
            if action == "Y":
                if healthcare >= 10:
                    money = money - inhabitants * random.randint(1, 5)
                else:
                    money = money - inhabitants * random.randint(6, 10)
            else:
               inhabitants = inhabitants - random.randint(3, inhabitants)
    #reward event
    if event == 2:
        print("Du findest Materialien in alten sovietischen Gebäuden..")
        input("Du verwertest sie und sparst viel Geld")
        money = money + random.randint(100, 150)
    #peace treaty event
    if event == 3:
        print("You have signed a treaty with a nearby country.")
        input("")
        money = money + random.randint(50, 200)
    #earthquake event
    if event == 4:
        print("An earthquake has destroyed some houses.")
        input("Some of your people died, and some fields were destroyed")
        inhabitants = inhabitants - random.randint(0, inhabitants//2)
        if inhabitants << 0:
            inhabitants = 0
        jobs = jobs - random.randint(0, jobs//2)
        food = food - random.randint(0, food//2)
    #stats
    print("Geld: ", money, "k")
    print("Einkommen: ", income, "k")
    print("Einwohner: ", inhabitants)
    print("wealth: ", wealth)
    print("Arbeit: ", jobs)
    print("Essen: ", food)
    #upgrade system
    #housing upgrade
    print("Einwohner UP? $", 50 + wealth, "k jeweils")
    txt = input("Kaufe Anzahl:")
    if txt.isdigit() == True:
        for x in range(int(txt)):
            money = money - 50
            money = money - wealth
            inhabitants = inhabitants + 30
    #health upgrade
    print("Krankenhäuser UP? ", 150 + wealth, "k jeweils")
    txt = input("Kaufe Anzahl:")
    if txt.isdigit() == True:
        for x in range(int(txt)):
            money = money - 150
            money = money - wealth
            healthcare = healthcare + 1
            jobs = jobs + 5
    #jobs upgrade
    print("Arbeit UP? ", 200 + wealth, "k jeweils")
    txt = input("Kaufe Anzahl:")
    if txt.isdigit() == True:
        for x in range(int(txt)):
            money = money - 200
            money = money - wealth
            jobs = jobs + 30
    #food upgrade
    print("Essen UP? ", 100 +wealth, "k jeweils")
    txt = input("Kaufe Anzahl:")
    if txt.isdigit() == True:
        for x in range(int(txt)):
            money = money - 100
            money = money - wealth
            jobs = jobs + 5
            food = food + 30
    #food system
    if food <= inhabitants:
        inhabitants = food
    #jobs and payment for workless
    if inhabitants > jobs:
        workless = inhabitants - jobs
        workers = inhabitants - workless
    if inhabitants <= jobs:
        workless = inhabitants - jobs
        workers = inhabitants + workless
    else:
        workers = jobs
    workless = workless//2
    #income
    income = workers * wealth
    income = income - workless * wealth
    #funding of the P.E.O.
    PEOpayment = income//50
    print("Du wirst", wealth * PEOpayment, "k an die USA zahlen.")
    money = money - wealth * PEOpayment
    input()
    #getting your income
    money = money + income
    clear()
    #round counter
    rounds = rounds + 1
    #end of the game and score
    if money <= 0:
        print("Game over!")
        time.sleep(1)
        print("Du hast", rounds, "Monate überlebt.")
        print("Score: ", wealth + food + inhabitants + healthcare + rounds)
        time.sleep(1)
        while True:
            print("Danke fürs spielen.")
            print("Programmed by Devin")
            print("Story by Linus")
            input("Exit?")
            time.sleep(1)
            quit()
    #wealth
    #achievement inhabitants
    if inhabitants >= 100 * achievementinhabitants:
        print("Glückwunsch, du hast über", 100 * achievementinhabitants, "Einwohner.")
        print("Dafür gibt es 1 Wohlhaben.")
        wealth = wealth + 1
        achievementinhabitants = achievementinhabitants + 1
    #achievement healthcare
    if healthcare >= 5 * achievementhealthcare:
        print("Glückwunsch, du hast über", 5 * achievementhealthcare, "Krankenhäuser.")
        print("Dafür gibt es 1 Wohlhaben.")
        wealth = wealth + 1
        achievementhealthcare = achievementhealthcare + 1
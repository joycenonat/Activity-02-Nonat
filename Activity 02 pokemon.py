import random

Ferlvl = int(input("Feraligatr's level: "))
Sdef = int(input("Special defense: "))
Etyp = str(input("Enemy type: "))
gen = int(input("Generation: "))
weth = str(input("Weather: "))
tget = int(input("Target: "))


Chalvl = int(input("Charizard level: "))
Ptype = str(input("Pokemon type: "))
Splatt = int(input("Special attack: "))
Stype = str(input("Skill type: "))
Pwr = int(input("Power: "))


def modifier (tget, weth, gen, Ptype, Stype, Etyp):

#for target

    if tget == 1:
        tget = 1
    else:
        tget = .5

#for weather
    if weth == "beneficial":
        weth = 1.5
    if weth == "against":
        weth = .5
    if weth == "otherwise":
        weth = 1

#for badge
    if gen == "2":
        gen = 1.25
    else:
        gen = 1
    
#for critical
    critic = [1 , 2]
    crtca = random.choice(critic)
    if crtca == 2:
        print("\n CRITICAL HIT")
    else: 
        print("HIT")

#for random
    randm = [0.85,1]
    rndm = random.choice(randm)

#stab
    if Ptype == "fire" and Stype == "fire":
        effect = 1.5
    else:
        effect = 1

#type
    if Stype =="fire" and Etyp == "fire":
        efct = .5
    if Stype =="fire" and Etyp == "water":
        efct = .5
    if Stype =="fire" and Etyp == "flying":
        efct = 1
    
    
    type = efct

    if type <=.5:
        print ("NOT EFFECTIVE!!")
    if type >=2:
        print("SUPER EFFECTIVE!!")
    else:
        type == 1
        
#other
    other = 1

#burn
    burned = [.5 , 1]
    buurn = random.choice(burned)
    if buurn == .5:
        print("\n The Attacker is BURNED!")

#calc for modifier
    mod = tget * weth * gen * crtca * rndm * effect * type * other * buurn
    return mod
    
#calc for damage
dmge = ((((((2*Chalvl)/5)+2)* Pwr * Splatt/Sdef)/50)+2) * modifier(tget, weth, gen, Ptype, Stype, Etyp)
print("CHARIZARDS DAMAGE TO FERALIGATR :", dmge)

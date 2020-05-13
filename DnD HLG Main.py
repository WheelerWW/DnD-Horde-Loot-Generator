#Program developed by Wesley Wheeler, 2019.#
#This program streamlines the 5th Edition Dungeons and Dragons Treasure rolling system found on pages 133-149 of the Dungeon Master's Guide.#

import random

#Dictionaries

magicA={}
magicB={}
magicC={}
magicD={}
magicE={}
magicF={}
magicG={}
magicH={}
magicI={}
gemP={}
gemC={}
gemU={}
gemR={}
gemVR={}
gemL={}
artC={}
artU={}
artR={}
artVR={}
artL={}

#Open up Item Files

with open ("MagicTableA.txt") as f:
    for line in f:
        (key, value) = line.split(":")
        magicA[key] = value

with open ("MagicTableB.txt") as f:
    for line in f:
        (key, value) = line.split(":")
        magicB[key] = value

with open ("MagicTableC.txt") as f:
    for line in f:
        (key, value) = line.split(":")
        magicC[key] = value

with open ("MagicTableD.txt") as f:
    for line in f:
        (key, value) = line.split(":")
        magicD[key] = value

with open ("MagicTableE.txt") as f:
    for line in f:
        (key, value) = line.split(":")
        magicE[key] = value

with open ("MagicTableF.txt") as f:
    for line in f:
        (key, value) = line.split(":")
        magicF[key] = value

with open ("MagicTableG.txt") as f:
    for line in f:
        (key, value) = line.split(":")
        magicG[key] = value

with open ("MagicTableH.txt") as f:
    for line in f:
        (key, value) = line.split(":")
        magicH[key] = value

with open ("MagicTableI.txt") as f:
    for line in f:
        (key, value) = line.split(":")
        magicI[key] = value

with open ("GemPetty.txt") as f:
    for line in f:
        (key, value) = line.split(":")
        gemP[key] = value

with open ("GemCommon.txt") as f:
    for line in f:
        (key, value) = line.split(":")
        gemC[key] = value

with open ("GemUncommon.txt") as f:
    for line in f:
        (key, value) = line.split(":")
        gemU[key] = value

with open ("GemRare.txt") as f:
    for line in f:
        (key, value) = line.split(":")
        gemR[key] = value

with open ("GemVeryRare.txt") as f:
    for line in f:
        (key, value) = line.split(":")
        gemVR[key] = value

with open ("GemLegendary.txt") as f:
    for line in f:
        (key, value) = line.split(":")
        gemL[key] = value
        
with open ("ArtCommon.txt") as f:
    for line in f:
        (key, value) = line.split(":")
        artC[key] = value

with open ("ArtUncommon.txt") as f:
    for line in f:
        (key, value) = line.split(":")
        artU[key] = value

with open ("ArtRare.txt") as f:
    for line in f:
        (key, value) = line.split(":")
        artR[key] = value

with open ("ArtVeryRare.txt") as f:
    for line in f:
        (key, value) = line.split(":")
        artVR[key] = value

with open ("ArtLegendary.txt") as f:
    for line in f:
        (key, value) = line.split(":")
        artL[key] = value


#Classes
class Horde:
    def __init__ (self, copper, silver, electrum, gold, platinum, art, gems, magic):
        self.copper = copper
        self.silver = silver
        self.electrum = electrum
        self.gold = gold
        self.platinum = platinum
        self.art = art
        self.gems = gems
        self.magic = magic

    def printContents(self):
        print("--------Summary of treasure found--------\n\n ",self.copper,"copper coins\n ",self.silver,"silver coins\n ",\
              self.electrum,"electrum coins\n ",self.gold,"gold coins\n ",self.platinum,"platinum coins\n")

        if len(self.art) != 0:
            print("These were the art pieces found:\n")
            for x in self.art:
                print("   ",x)
        if len(self.gems) != 0:
            print("These were the gemstones found:\n")
            for x in self.gems:
                print("   ",x)
        if len(self.magic) != 0:
            print("These were the magic items found:\n")
            for x in self.magic:
                print("   ",x)

                
class Individual:
    def __init__ (self, copper, silver, electrum, gold, platinum):
        self.copper = copper
        self.silver = silver
        self.electrum = electrum
        self.gold = gold
        self.platinum = platinum

    def printContents(self):
        print("\n--------Treasure found so far--------\n ",self.copper,"copper coins\n ",self.silver,"silver coins\n ",\
              self.electrum,"electrum coins\n ",self.gold,"gold coins\n ",self.platinum,"platinum coins\n\n")




#Functions
#Functions for Manual Input
        
def ManualMode():
    print("Which treasure type would you like to choose?\n 1: Magic Items\n 2: Art \n 3: Gemstones \n 4: Exit ")
    manualChoice=str(input("Select a Treasure Type -> "))
    while manualChoice.lower() not in ("1", "magic items", "2", "art", "3", "gemstones", "4", "exit"):
        manualChoice=input("That is not a valid selection.  Be sure to select a number or the appropriate type. \nPlease try again -> ")
        
    if manualChoice.lower() in ("1", "magic items"):
        functionLoop=True
        while (functionLoop==True):
            functionLoop=MagicTables()

    if manualChoice.lower() in ("2", "art"):
        functionLoop=True
        while (functionLoop==True):
            functionLoop=ArtTables()
            
    if manualChoice.lower() in ("3", "gemstones"):
        functionLoop=True
        while (functionLoop==True):
            functionLoop=GemTables()

    if manualChoice.lower() in ("4", "exit"):
        return

    return True

def InputChecker(Dict):
    path=False
    while(path==False):
        try:
            dictSize=len(Dict)
            print("Select a Number from 1 -",dictSize,"Now -> ")
            dictKey=int(input())
            if dictKey not in range (0,dictSize+1):
                print("That number is not within the appropriate range.")
            else:
                path=True
        except ValueError:
            print("That is not a valid selection.")
    return dictKey

def MagicTables():
    magicInputs=["1","2","3","4","5","6","7","8","9","10",\
    "a","b","c","d","e","f","g","h","i","exit",\
    "table a","table b","table c","table d","table e","table f","table g","table h","table i"]
    
    print("Which item table would you like to choose?\n 1: Table A\n 2: Table B \n 3: Table C \n 4: Table D \n 5: Table E \n 6: Table F \n 7: Table G \n 8: Table H \n 9: Table I \n 10: Exit")
    magicChoice=str(input("Select a Table  -> "))
    while magicChoice.lower() not in magicInputs:
        print("That is not a valid selection.  Be sure to select a number or the table name/letter.")
        magicChoice=input("Please try again -> ")
        
    if magicChoice.lower() in ("1", "a", "table a"):
        dictKey=InputChecker(magicA)
        print("\n", magicA[str(dictKey)])
        
    elif magicChoice.lower() in ("2", "b", "table b"):
        dictKey=InputChecker(magicB)
        print("\n", magicB[str(dictKey)]) 

    elif magicChoice.lower() in ("3", "c", "table c"):
        dictKey=InputChecker(magicC)
        print("\n", magicC[str(dictKey)])
        
    elif magicChoice.lower() in ("4", "d", "table d"):
        dictKey=InputChecker(magicD)
        print("\n", magicD[str(dictKey)])
        
    elif magicChoice.lower() in ("5", "e", "table e"):
        dictKey=InputChecker(magicE)
        print("\n", magicE[str(dictKey)])
        
    elif magicChoice.lower() in ("6", "f", "table f"):
        dictKey=InputChecker(magicF)
        print("\n", magicF[str(dictKey)])
        
    elif magicChoice.lower() in ("7", "g", "table g"):
        dictKey=InputChecker(magicG)
        print("\n", magicG[str(dictKey)])
    
    elif magicChoice.lower() in ("8", "h", "table h"):
        dictKey=InputChecker(magicH)
        print("\n", magicH[str(dictKey)])

    elif magicChoice.lower() in ("9", "i", "table i"):
        dictKey=InputChecker(magicI)
        print("\n", magicI[str(dictKey)])
        
    elif magicChoice.lower() in ("10", "exit"):
        return False
    
    return True

def ArtTables():
    artInputs=["1","2","3","4","5","6","common","uncommon","rare","very rare","legendary","exit"]
    
    print("Which item table would you like to choose?\n 2: Uncommon \n 3: Rare \n 4: Very Rare \n 5: Legendary \n 6: Exit ")
    artChoice=str(input("Select a Table -> "))
    while artChoice.lower() not in artInputs:
        print("That is not a valid selection.  Be sure to select a number or the table name.")
        artChoice=input("Please try again -> ")
        
    if artChoice.lower() in ("1", "common"):
        dictKey=InputChecker(artC)
        print("\n", artC[str(dictKey)])
        
    if artChoice.lower() in ("2", "uncommon"):
        dictKey=InputChecker(artU)
        print("\n", artU[str(dictKey)])

    elif artChoice.lower() in ("3", "rare"):
        dictKey=InputChecker(artR)
        print("\n", artR[str(dictKey)])

    elif artChoice.lower() in ("4", "very rare"):
        dictKey=InputChecker(artVR)
        print("\n", artVR[str(dictKey)])

    elif artChoice.lower() in ("5", "legendary"):
        dictKey=InputChecker(artL)
        print("\n", artL[str(dictKey)])

    elif artChoice.lower() in ("6", "exit"):
        return False
    
    return True

def GemTables():
    gemInputs=["1","2","3","4","5","6","7",\
    "petty","common","uncommon","rare","very rare","legendary","exit"]
    
    print("Which item table would you like to choose?\n 1: Petty\n 2: Common \n 3: Uncommon \n 4: Rare \n 5: Very Rare \n 6: Legendary \n 7: Exit ")
    gemChoice=str(input("Select a Table -> "))
    while gemChoice.lower() not in gemInputs:
        print("That is not a valid selection.  Be sure to select a number or the table name.")
        gemChoice=input("Please try again -> ")
        
    if gemChoice.lower() in ("1", "petty"):
        dictKey=InputChecker(gemP)
        print("\n", gemP[str(dictKey)])

    elif gemChoice.lower() in ("2", "common"):
        dictKey=InputChecker(gemC)
        print("\n", gemC[str(dictKey)])

    elif gemChoice.lower() in ("3", "uncommon"):
        dictKey=InputChecker(gemU)
        print("\n", gemU[str(dictKey)])

    elif gemChoice.lower() in ("4", "rare"):
        dictKey=InputChecker(gemR)
        print("\n", gemR[str(dictKey)])

    elif gemChoice.lower() in ("5", "very rare"):
        dictKey=InputChecker(gemVR)
        print("\n", gemVR[str(dictKey)])

    elif gemChoice.lower() in ("6", "legendary"):
        dictKey=InputChecker(gemL)
        print("\n", gemL[str(dictKey)])

    elif gemChoice.lower() in ("7", "exit"):
            return False
        
    return True




#Functions for Randomly Generated Output

def RNG():
    print("\nWhat type of encounter will roll for?\n 1: Individual Encounter\n 2: Horde Encounter \n 3: Exit ")
    rngChoice=input("Select an Encounter Type -> ")
    while rngChoice.lower() not in ("1", "individual", "individual treasure", "2", "horde", "horde treasure", "3", "exit"):
        rngChoice=input("That is not a valid selection.  Be sure to select a number or an encounter type. \nPlease try again -> ")
        
    if rngChoice.lower() in ("1", "individual", "individual encounter"):
        functionLoop=True
        i=0
        while (functionLoop==True):
            functionLoop=IndRNG(i)
            i=1

    if rngChoice.lower() in ("2", "horde", "horde encounter"):
        functionLoop=True
        while (functionLoop==True):
            functionLoop=HordeRNG()

    if rngChoice.lower() in ("3", "exit"):
        return False

    return True


def DiceRolls(numRolls, dieFaces):
    i=0
    rollSum=0
    print(numRolls,dieFaces,"sided die rolled. Your dice rolls are:")
    while (i<numRolls):
        dieRoll=random.randint(1,dieFaces)
        print(" ",dieRoll)
        rollSum=rollSum+dieRoll
        i=i+1
    print("Die Sum:",rollSum,"\n")
    return rollSum


def DictionRolls(numRolls, Dict):
    i=0
    contents=[]
    while (i<numRolls):
        dieRoll=str(random.randint(1,len(Dict)))
        print(Dict[dieRoll])
        contents.append(Dict[dieRoll])
        i=i+1
    return contents

def IndRNG(i):
    if i==0:
        global indSum
        indSum=Individual(0,0,0,0,0)
    else:
        indSum.printContents()
    
    print("\nSelect the individual encounter difficulty.\n 1: Easy (Challenge 0-4)\n 2: Medium (Challenge 5-10) \n 3: Hard (Challenge 11-16) \n 4: Legendary (Challenge 17+) \n 5: Exit ")
    rngChoice=input("Select an Encounter Type -> ")
    
    while rngChoice.lower() not in ("1", "easy", "2", "medium", "3", "hard", "4", "legendary", "5", "exit"):
        rngChoice=input("That is not a valid selection.  Be sure to select a number or an encounter type. \nPlease try again -> ")

    roll=random.randint(1,100)
    if rngChoice.lower() in ("1", "easy", "e"):
        print("\nYour d100 roll is",roll,"\n")
        if roll in range(1,31):
            total=DiceRolls(5,6)
            print(total,"copper pieces were dropped.")
            indSum.copper=indSum.copper+total

        if roll in range(31,61):
            total=DiceRolls(4,6)
            print(total,"silver pieces were dropped.")
            indSum.silver=indSum.silver+total

        if roll in range(61,71):
            total=DiceRolls(3,6)
            print(total,"electrum pieces were dropped.")
            indSum.electrum=indSum.electrum+total

        if roll in range(71,96):
            total=DiceRolls(3,6)
            print(total,"gold pieces were dropped.")
            indSum.gold=indSum.gold+total

        if roll in range(96,101):
            total=DiceRolls(1,6)
            print(total,"platinum pieces were dropped.")
            indSum.platinum=indSum.platinum+total

    elif rngChoice.lower() in ("2", "medium", "m"):
        print("\nYour d100 roll is",roll,"\n")
        if roll in range(1,31):
            total=DiceRolls(4,6)
            total=total*100
            print(total,"copper pieces were dropped.")
            indSum.copper=indSum.copper+total
            total=DiceRolls(1,6)
            total=total*10            
            print(total,"electrum pieces were dropped.")
            indSum.electrum=indSum.electrum+total

        if roll in range(31,61):
            total=DiceRolls(6,6)
            total=total*10
            print(total,"silver pieces were dropped.")
            indSum.silver=indSum.silver+total
            total=DiceRolls(2,6)
            total=total*10
            print(total,"gold pieces were dropped.")
            indSum.gold=indSum.gold+total

        if roll in range(61,71):
            total=DiceRolls(3,6)
            total=total*10
            print(total,"electrum pieces were dropped.")
            indSum.electrum=indSum.electrum+total
            total=DiceRolls(2,6)
            total=total*10
            print(total,"gold pieces were dropped.")
            indSum.gold=total

        if roll in range(71,96):
            total=DiceRolls(4,6)
            total=total*10
            print(total,"gold pieces were dropped.")
            indSum.gold=indSum.electrum+total

        if roll in range(96,101):
            total=DiceRolls(2,6)
            total=total*10
            print(total,"gold pieces were dropped.")
            indSum.gold=indSum.gold+total
            total=DiceRolls(3,6)
            print(total,"platinum pieces were dropped.")
            indSum.platinum=indSum.gold+total
        
    elif rngChoice.lower() in ("3", "hard", "h"):
        print("\nYour d100 roll is",roll,"\n")
        if roll in range(1,21):
            total=DiceRolls(4,6)
            total=total*100
            print(total,"silver pieces were dropped.")
            indSum.silver=indSum.silver+total
            total=DiceRolls(1,6)
            total=total*100
            print(total,"gold pieces were dropped.")
            indSum.gold=indSum.gold+total

        if roll in range(21,36):
            total=DiceRolls(1,6)
            total=total*100
            print(total,"electrum pieces were dropped.")
            indSum.electrum=indSum.electrum+total
            total=DiceRolls(1,6)
            total=total*100
            print(total,"gold pieces were dropped.")
            indSum.gold=indSum.gold+total

        if roll in range(36,76):
            total=DiceRolls(2,6)
            total=total*100
            print(total,"gold pieces were dropped.")
            indSum.gold=indSum.gold+total
            total=DiceRolls(1,6)
            total=total*10
            print(total,"platinum pieces were dropped.")
            indSum.platinum=indSum.platinum+total

        if roll in range(76,101):
            total=DiceRolls(2,6)
            total=total*100
            print(total,"gold pieces were dropped.")
            indSum.gold=indSum.gold+total
            total=DiceRolls(2,6)
            total=total*10
            print(total,"platinum pieces were dropped.")
            indSum.platinum=indSum.platinum+total

    elif rngChoice.lower() in ("4", "legendary", "l"):
        print("\nYour d100 roll is",roll,"\n")
        if roll in range(1,16):
            total=DiceRolls(2,6)
            total=total*1000
            print(total,"electrum pieces were dropped.")
            indSum.electrum=indSum.electrum+total
            total=DiceRolls(8,6)
            total=total*100
            print(total,"gold pieces were dropped.")
            indSum.gold=indSum.gold+total

        if roll in range(16,56):
            total=DiceRolls(1,6)
            total=total*1000
            print(total,"gold pieces were dropped.")
            indSum.gold=indSum.gold+total
            total=DiceRolls(1,6)
            total=total*100
            print(total,"platinum pieces were dropped.")
            indSum.platinum=indSum.platinum+total

        if roll in range(56,101):
            total=DiceRolls(1,6)
            total=total*1000
            print(total,"gold pieces were dropped.")
            indSum.gold=indSum.gold+total
            total=DiceRolls(2,6)
            total=total*100
            print(total,"platinum pieces were dropped.")
            indSum.platinum=indSum.platinum+total

    elif rngChoice.lower() in ("5", "exit"):
        return False

    return True

#This function is a bit, uh.... hefty
def HordeRNG():
    summary=Horde(0,0,0,0,0,[],[],[])
    print("\nSelect the horde encounter difficulty.\n 1: Easy (Challenge 0-4)\n 2: Medium (Challenge 5-10) \n 3: Hard (Challenge 11-16) \n 4: Legendary (Challenge 17+) \n 5: Exit ")
    hordeChoice=input("Select an Encounter Type -> ")
    
    while hordeChoice.lower() not in ("1", "easy", "2", "medium", "3", "hard", "4", "legendary", "5", "exit"):
        hordeChoice=input("That is not a valid selection.  Be sure to select a number or an encounter type. \nPlease try again -> ")
        
    roll=random.randint(1,100)
    if hordeChoice.lower() in ("1", "easy", "e"):
        print("\n\n* * * * * * Horde Treasure Start * * * * * *\n\n")
        print("\nYour d100 dice roll is",roll,"\n")
        
        total=DiceRolls(6,6)
        total=total*1000
        summary.copper=total
        print(total,"copper pieces were found in the treasure horde.\n")
        total=DiceRolls(3,6)
        total=total*100
        summary.silver=total
        print(total,"silver pieces were found in the treasure horde.\n")
        total=DiceRolls(2,6)
        total=total*10
        summary.gold=total
        print(total,"gold pieces were found in the treasure horde.\n")

        if roll in range(1,7):
            print("There were no additional drops")
        elif roll in range(7,17):
            objRolls=DiceRolls(2,6)
            print("These petty 10 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemP)
                  
        elif roll in range(17,27):
            objRolls=DiceRolls(2,4)
            print("These common 25 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artC)
                  
        elif roll in range(27,37):
            objRolls=DiceRolls(2,6)
            print("These common 50 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemC)
                  
        elif roll in range(37,45):
            objRolls=DiceRolls(2,6)
            print("These petty 10 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemP)
            magRolls=DiceRolls(1,6)
            print("These magic items from Table A were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicA)
                  
        elif roll in range(45,53):
            objRolls=DiceRolls(2,4)
            print("These common 25 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artC)
            magRolls=DiceRolls(1,6)
            print("These magic items from Table A were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicA)
                  
        elif roll in range(53,61):
            objRolls=DiceRolls(2,6)
            print("These common 50 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemC)
            magRolls=DiceRolls(1,6)
            print("These magic items from Table A were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicA)
                  
        elif roll in range(61,66):
            objRolls=DiceRolls(2,6)
            print("These petty 10 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemP)
            magRolls=DiceRolls(1,4)
            print("These magic items from Table B were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicB)
                  
        elif roll in range(66,71):
            objRolls=DiceRolls(2,4)
            print("These common 25 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artC)
            magRolls=DiceRolls(1,4)
            print("These magic items from Table B were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicB)
                  
        elif roll in range(71,76):
            objRolls=DiceRolls(2,6)
            print("These common 50 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemC)
            magRolls=DiceRolls(1,4)
            print("These magic items from Table B were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicB)
                  
        elif roll in range(76,79):
            objRolls=DiceRolls(2,6)
            print("These petty 10 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemP)
            magRolls=DiceRolls(1,4)
            print("These magic items from Table C were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicC)
                  
        elif roll in range(79,81):
            objRolls=DiceRolls(2,4)
            print("These common 25 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artC)
            magRolls=DiceRolls(1,4)
            print("These magic items from Table C were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicC)
            
        elif roll in range(81,86):
            objRolls=DiceRolls(2,6)
            print("These common 50 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemC)
            magRolls=DiceRolls(1,4)
            print("These magic items from Table C were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicC)
                  
        elif roll in range(86,93):
            objRolls=DiceRolls(2,4)
            print("These common 25 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artC)
            magRolls=DiceRolls(1,4)
            print("These magic items from Table F were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicF)
                  
        elif roll in range(93,98):
            objRolls=DiceRolls(2,6)
            print("These common 50 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemC)
            magRolls=DiceRolls(1,4)
            print("These magic items from Table F were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicF)
                  
        elif roll in range(98,100):
            objRolls=DiceRolls(2,4)
            print("These common 25 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artC)
            magRolls=1
            print("These magic items from Table G were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicG)
            
        elif roll == 100:
            objRolls=DiceRolls(2,4)
            print("These common 50 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemC)
            magRolls=1
            print("These magic items were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicG)

    elif hordeChoice.lower() in ("2", "medium", "m"):
        print("\n\n* * * * * * Horde Treasure Start * * * * * *\n\n")
        print("\nYour d100 dice roll is",roll,"\n")
              
        total=DiceRolls(2,6)
        total=total*100
        print(total,"copper pieces were found in the treasure horde.\n")
        summary.copper=total
        total=DiceRolls(2,6)
        total=total*1000
        print(total,"silver pieces were found in the treasure horde.\n")
        summary.silver=total
        total=DiceRolls(6,6)
        total=total*100
        print(total,"gold pieces were found in the treasure horde.\n")
        summary.gold=total
        total=DiceRolls(3,6)
        total=total*10
        print(total,"platinum pieces were found in the treasure horde.\n")
        summary.platinum=total
        
        if roll in range(1,5):
            print("There were no additional drops")
            
        elif roll in range(5,11):
            objRolls=DiceRolls(2,4)
            print("These common 25 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artC)
            
        elif roll in range(11,17):
            objRolls=DiceRolls(3,6)
            print("These common 50 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemC)
            
        elif roll in range(17,23):
            objRolls=DiceRolls(3,6)
            print("These uncommon 100 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemU)
            
        elif roll in range(23,29):
            objRolls=DiceRolls(2,4)
            print("These uncommon 250 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artU)

        elif roll in range(29,33):
            objRolls=DiceRolls(2,4)
            print("These common 25 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artC)
            magRolls=DiceRolls(1,6)
            print("These magic items from Table A were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicA)

        elif roll in range(33,37):
            objRolls=DiceRolls(3,6)
            print("These common 50 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemC)
            magRolls=DiceRolls(1,6)
            print("These magic items from Table A were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicA)
            
        elif roll in range(37,41):
            objRolls=DiceRolls(3,6)
            print("These uncommon 100 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemU)
            magRolls=DiceRolls(1,6)
            print("These magic items from Table A were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicA)
            
        elif roll in range(41,45):
            objRolls=DiceRolls(2,4)
            print("These uncommon 250 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artC)
            magRollsDiceRolls(1,6)
            print("These magic items from Table A were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicA)
            
        elif roll in range(45,50):
            objRolls=DiceRolls(2,4)
            print("These common 25 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artC)
            magRolls=DiceRolls(1,4)
            print("These magic items from Table B were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicB)
            
        elif roll in range(50,55):
            objRolls=DiceRolls(3,6)
            print("These common 50 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemC)
            magRolls=magRolls=DiceRolls(1,4)
            print("These magic items from Table B were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicB)
            
        elif roll in range(55,60):
            objRolls=DiceRolls(3,6)
            print("These common 100 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemU)
            magRollsDiceRolls(1,4)
            print("These magic items from Table B were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicB)
            
        elif roll in range(60,64):
            objRolls=DiceRolls(2,4)
            print("These uncommon 250 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artC)
            magRolls=DiceRolls(1,4)
            print("These magic items from Table B were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicB)
            
        elif roll in range(64,67):
            objRolls=DiceRolls(2,4)
            print("These common 25 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artC)
            magRolls=DiceRolls(1,4)
            print("These magic items from Table C were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicC)
            
        elif roll in range(67,70):
            objRolls=DiceRolls(3,6)
            print("These common 50 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemC)
            magRolls=DiceRolls(1,4)
            print("These magic items from Table C were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicC)
            
        elif roll in range(70,73):
            objRolls=DiceRolls(3,6)
            print("These uncommon 100 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemU)
            magRolls=DiceRolls(1,4)
            print("These magic items from Table C were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicC)
            
        elif roll in range(73,75):
            objRolls=DiceRolls(2,4)
            print("These uncommon 250 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artU)
            magRolls=DiceRolls(1,4)
            print("These magic items from Table C were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicC)
            
        elif roll in range(75,77):
            objRolls=DiceRolls(2,4)
            print("These common 25 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artC)
            magRolls=1
            print("These magic items from Table D were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicD)
            
        elif roll in range(77,79):
            objRolls=DiceRolls(3,6)
            print("These common 50 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemC)
            magRolls=1
            print("These magic items from Table D were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicD)
            
        elif roll == 79:
            objRolls=DiceRolls(3,6)
            print("These uncommon 100 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemU)
            magRolls=1
            print("These magic items from Table D were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicD)
            
        elif roll == 80:
            objRolls=DiceRolls(2,4)
            print("These uncommon 250 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artU)
            magRolls=1
            print("These magic items from Table D were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicD)
            
        elif roll in range(81,85):
            objRolls=DiceRolls(2,4)
            print("These common 25 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artC)
            magRolls=DiceRolls(1,4)
            print("These magic items from Table F were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicF)
            
        elif roll in range(85,88):
            objRolls=DiceRolls(3,6)
            print("These common 50 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemC)
            magRolls=DiceRolls(1,4)
            print("These magic items from Table F were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicF)
            
        elif roll in range(89,92):
            objRolls=DiceRolls(3,6)
            print("These uncommon 100 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemU)
            magRolls=DiceRolls(1,4)
            print("These magic items from Table F were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicF)
            
        elif roll in range(92,95):
            objRolls=DiceRolls(2,4)
            print("These uncommon 250 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artU)
            magRolls=DiceRolls(1,4)
            print("These magic items from Table F were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicF)
            
        elif roll in range(95,97):
            objRolls=DiceRolls(3,6)
            print("These uncommon 100 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemU)
            magRolls=DiceRolls(1,4)
            print("These magic items from Table G were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicG)
            
        elif roll in range(97,99):
            objRolls=DiceRolls(2,4)
            print("These uncommon 250 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artU)
            magRolls=DiceRolls(1,4)
            print("These magic items from Table G were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicG)
            
        elif roll == 99:
            objRolls=DiceRolls(3,6)
            print("These common 50 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemC)
            magRolls=1
            print("These magic items from Table H were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicH)
            
        elif roll == 100:
            objRolls=DiceRolls(2,4)
            print("These uncommon 250 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artU)
            magRolls=1
            print("These magic items from Table H were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicH)
            

    elif hordeChoice.lower() in ("3", "hard", "h"):
        print("\n\n* * * * * * Horde Treasure Start * * * * * *\n\n")
        print("\nYour d100 dice roll is",roll,"\n")

        total=DiceRolls(4,6)
        total=total*1000
        print(total,"gold pieces were found in the treasure horde.\n")
        summary.gold=total
        total=DiceRolls(5,6)
        total=total*100
        print(total,"platinum pieces were found in the treasure horde.\n")
        summary.platinum=total
        
        if roll in range(1,4):
            print("There were no additional drops.")
            
        elif roll in range(4,7):
            objRolls=DiceRolls(2,4)
            print("These uncommon 250 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artU)

        elif roll in range(7,10):
            objRolls=DiceRolls(2,4)
            print("These rare 750 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artR)
            
        elif roll in range(10,13):
            objRolls=DiceRolls(3,6)
            print("These rare 500 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemR)
            
        elif roll in range(13,16):
            objRolls=DiceRolls(3,6)
            print("These very rare 1000 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemVR)
            
        elif roll in range(16,20):
            objRolls=DiceRolls(2,4)
            print("These uncommon 250 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artU)            
            magRolls=DiceRolls(1,4)
            print("These magic items from Table A that were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicA)
            magRolls=DiceRolls(1,6)
            print("These magic items from Table B that were found in the treasure horde.\n")
            mApp=DictionRolls(magRolls,magicB)
            for x in mApp:
                summary.magic.append(x)
                
        elif roll in range(20,24):
            objRolls=DiceRolls(2,4)
            print("These rare 750 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artR)            
            magRolls=DiceRolls(1,4)
            print("These magic items from Table A that were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicA)
            magRolls=DiceRolls(1,6)
            print("These magic items from Table B that were found in the treasure horde.\n")
            mApp=DictionRolls(magRolls,magicB)
            for x in mApp:
                summary.magic.append(x)
            
        elif roll in range(24,27):
            objRolls=DiceRolls(3,6)
            print("These rare 500 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemR)        
            magRolls=DiceRolls(1,4)
            print("These magic items from Table A that were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicA)
            magRolls=DiceRolls(1,6)
            print("These magic items from Table B that were found in the treasure horde.\n")
            mApp=DictionRolls(magRolls,magicB)
            for x in mApp:
                summary.magic.append(x)
            
        elif roll in range(27,30):
            objRolls=DiceRolls(3,6)
            print("These very rare 1000 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemVR)              
            magRolls=DiceRolls(1,4)
            print("These magic items from Table A that were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicA)
            magRolls=DiceRolls(1,6)
            print("These magic items from Table B that were found in the treasure horde.\n")
            mApp=DictionRolls(magRolls,magicB)
            for x in mApp:
                summary.magic.append(x)
            
        elif roll in range(30,36):
            objRolls=DiceRolls(2,4)
            print("These uncommon 250 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artU)            
            magRolls=DiceRolls(1,6)
            print("These magic items from Table C were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicC)
            
        elif roll in range(36,41):
            objRolls=DiceRolls(2,4)
            print("These rare 750 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artR)           
            magRolls=DiceRolls(1,6)
            print("These magic items from Table C were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicC)
            
        elif roll in range(41,46):
            objRolls=DiceRolls(3,6)
            print("These rare 500 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemR)            
            magRolls=DiceRolls(1,6)
            print("These magic items from Table C were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicC)
            
        elif roll in range(46,51):
            objRolls=DiceRolls(3,6)
            print("These very rare 1000 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemVR)            
            magRolls=DiceRolls(1,6)
            print("These magic items from Table C were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicC)
            
        elif roll in range(51,55):
            objRolls=DiceRolls(2,4)
            print("These uncommon 250 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artU)            
            magRolls=DiceRolls(1,4)
            print("These magic items from Table D were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicD)
            
        elif roll in range(55,59):
            objRolls=DiceRolls(2,4)
            print("These rare 750 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artR)            
            magRolls=DiceRolls(1,4)
            print("These magic items from Table D were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicD)
            
        elif roll in range(59,63):
            objRolls=DiceRolls(3,6)
            print("These rare 500 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemR)               
            magRolls=DiceRolls(1,4)
            print("These magic items from Table D were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicD)
            
        elif roll in range(63,67):
            objRolls=DiceRolls(3,6)
            print("These very rare 1000 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemVR)              
            magRolls=DiceRolls(1,4)
            print("These magic items  from Table D were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicD)
            
        elif roll in range(67,69):
            objRolls=DiceRolls(2,4)
            print("These uncommon 250 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artU)            
            magRolls=1
            print("These magic items from Table E were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicE)
            
        elif roll in range(69,71):
            objRolls=DiceRolls(2,4)
            print("These rare 750 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artR)
            magRolls=1
            print("These magic items from Table E were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicE)
            
        elif roll in range(71,73):
            objRolls=DiceRolls(3,6)
            print("These rare 500 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemR)               
            magRolls=1
            print("These magic items from Table E were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicE)
            
        elif roll in range(73,75):
            objRolls=DiceRolls(3,6)
            print("These very rare 1000 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemVR)              
            magRolls=1
            print("These magic items from Table E were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicE)
            
        elif roll in range(75,77):
            objRolls=DiceRolls(2,4)
            print("These uncommon 250 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artU)
            magRolls=1
            print("These magic items from Table F were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicF)
            magRolls=DiceRolls(1,4)
            print("These magic items from Table G were found in the treasure horde.\n")
            mApp=DictionRolls(magRolls,magicG)
            for x in mApp:
                summary.magic.append(x)
            
        elif roll in range(77,79):
            objRolls=DiceRolls(2,4)
            print("These rare 750 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artR)
            magRolls=1
            print("These magic items from Table F were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicF)
            magRolls=DiceRolls(1,4)
            print("These magic items from Table G were found in the treasure horde.\n")
            mApp=DictionRolls(magRolls,magicG)
            for x in mApp:
                summary.magic.append(x)
            
        elif roll in range(79,81):
            objRolls=DiceRolls(3,6)
            print("These rare 500 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemR)               
            magRolls=1
            print("These magic items from Table F were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicF)
            magRolls=DiceRolls(1,4)
            print("These magic items from Table G were found in the treasure horde.\n")
            mApp=DictionRolls(magRolls,magicG)
            for x in mApp:
                summary.magic.append(x)
                
        elif roll in range(81,83):
            objRolls=DiceRolls(3,6)
            print("These very rare 1000 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemVR)              
            magRolls=1
            print("These magic items from Table F were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicF)
            magRolls=DiceRolls(1,4)
            print("These magic items from Table G were found in the treasure horde.\n")
            mApp=DictionRolls(magRolls,magicG)
            for x in mApp:
                summary.magic.append(x)
            
        elif roll in range(83,86):
            objRolls=DiceRolls(2,4)
            print("These uncommon 250 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artU)            
            magRolls=DiceRolls(1,4)
            print("These magic items from Table H were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicH)
            
        elif roll in range(86,89):
            objRolls=DiceRolls(2,4)
            print("These rare 750 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artR)            
            magRolls=DiceRolls(1,4)
            print("These magic items from Table H were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicH)
            
        elif roll in range(89,91):
            objRolls=DiceRolls(3,6)
            print("These rare 500 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemR)               
            magRolls=DiceRolls(1,4)
            print("These magic items from Table H were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicH)
            
        elif roll in range(91,93):
            objRolls=DiceRolls(3,6)
            print("These very rare 1000 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemVR)              
            magRolls=DiceRolls(1,4)
            print("These magic items from Table H were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicH)
            
        elif roll in range(93,95):
            objRolls=DiceRolls(2,4)
            print("These uncommon 250 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artU)
            magRolls=1
            print("These magic items from Table I were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicI)
            
        elif roll in range(95,97):
            objRolls=DiceRolls(2,4)
            print("These rare 750 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artR)
            magRolls=1
            print("These magic items from Table I were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicI)
            
        elif roll in range(97,99):
            objRolls=DiceRolls(3,6)
            print("These rare 500 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemR)               
            magRolls=1
            print("These magic items from Table I were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicI)
            
        elif roll in range(99,101):
            objRolls=DiceRolls(3,6)
            print("These very rare 1000 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemVR)              
            magRolls=1
            print("These magic items from Table I were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicI)

            

    elif hordeChoice.lower() in ("4", "legendary", "l"):
        print("\n\n* * * * * * Horde Treasure Start * * * * * *\n\n")
        print("\nYour d100 dice roll is",roll,"\n")

        total=DiceRolls(12,6)
        total=total*1000
        print(total,"gold pieces were found in the treasure horde.\n")
        summary.gold=total
        total=DiceRolls(8,6)
        total=total*1000
        print(total,"platinum pieces were found in the treasure horde.\n")
        summary.platinum=total
        
        if roll in range(1,3):
            print("There were no additional drops.")
            
        elif roll in range(3,6):
            objRolls=DiceRolls(3,6)
            print("These very rare 1000 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemVR)           
            magRolls=DiceRolls(1,8)
            print("These magic items from Table C were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicC)

            
        elif roll in range(6,9):
            objRolls=DiceRolls(1,4)
            print("These very rare 7500 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artL)      
            magRolls=DiceRolls(1,8)
            print("These magic items from Table C were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicC)
            
        elif roll in range(9,12):
            objRolls=DiceRolls(1,10)
            print("These very rare 2500 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artVR)      
            magRolls=DiceRolls(1,8)
            print("These magic items from Table C were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicC)
            
        elif roll in range(12,15):
            objRolls=DiceRolls(1,8)
            print("These legendary 5000 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemL)      
            magRolls=DiceRolls(1,8)
            print("These magic items from Table C were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicC)
            
        elif roll in range(15,23):
            objRolls=DiceRolls(3,6)
            print("These very rare 1000 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemVR)      
            magRolls=DiceRolls(1,6)
            print("These magic items from Table D were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicD)
            
        elif roll in range(23,31):
            objRolls=DiceRolls(1,10)
            print("These very rare 2500 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artVR)      
            magRolls=DiceRolls(1,6)
            print("These magic items from Table D were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicD)
            
        elif roll in range(31,39):
            objRolls=DiceRolls(1,4)
            print("These very rare 7500 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artL)      
            magRolls=DiceRolls(1,6)
            print("These magic items from Table D were found in the treasure horde.\n")
            DictionRolls(magRolls,magicD)
            
        elif roll in range(39,47):
            objRolls=DiceRolls(1,6)
            print("These legendary 5000 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemL)      
            magRolls=DiceRolls(1,8)
            print("These magic items from Table D were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicD)
            
        elif roll in range(47,53):
            objRolls=DiceRolls(3,6)
            print("These very rare 1000 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemVR)      
            magRolls=DiceRolls(1,6)
            print("These magic items from Table E were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicE)
            
        elif roll in range(53,59):
            objRolls=DiceRolls(1,10)
            print("These very rare 2500 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artVR)      
            magRolls=DiceRolls(1,6)
            print("These magic items from Table E were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicE)
            
        elif roll in range(59,64):
            objRolls=DiceRolls(1,4)
            print("These very rare 7500 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artL)      
            magRolls=DiceRolls(1,6)
            print("These magic items from Table E were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicE)
            
        elif roll in range(64,69):
            objRolls=DiceRolls(1,8)
            print("These legendary 5000 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemL)      
            magRolls=DiceRolls(1,6)
            print("These magic items from Table E were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicE)
            
        elif roll == 69:
            objRolls=DiceRolls(3,6)
            print("These very rare 1000 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemVR)      
            magRolls=DiceRolls(1,4)
            print("These magic items from Table G were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicG)
            
        elif roll == 70:
            objRolls=DiceRolls(1,10)
            print("These very rare 2500 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artVR)      
            magRolls=DiceRolls(1,4)
            print("These magic items from Table G were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicG)
            
        elif roll == 71:
            objRolls=DiceRolls(1,4)
            print("These very rare 7500 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artL)      
            magRolls=DiceRolls(1,4)
            print("These magic items from Table G were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicG)
            
        elif roll == 72:
            objRolls=DiceRolls(1,8)
            print("These legendary 5000 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemL)      
            magRolls=DiceRolls(1,4)
            print("These magic items from Table G were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicG)
            
        elif roll in range(73,75):
            objRolls=DiceRolls(3,6)
            print("These very rare 1000 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemVR)      
            magRolls=DiceRolls(1,4)
            print("These magic items from Table H were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicH)
            
        elif roll in range(75,77):
            objRolls=DiceRolls(1,10)
            print("These very rare 2500 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artVR)      
            magRolls=DiceRolls(1,4)
            print("These magic items from Table H were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicH)
            
        elif roll in range(77,79):
            objRolls=DiceRolls(1,4)
            print("These very rare 7500 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artL)      
            magRolls=DiceRolls(1,4)
            print("These magic items from Table H were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicH)
            
        elif roll in range(79,81):
            objRolls=DiceRolls(1,8)
            print("These legendary 5000 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemL)      
            magRolls=DiceRolls(1,4)
            print("These magic items from Table H were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicH)
            
        elif roll in range(81,86):
            objRolls=DiceRolls(3,6)
            print("These very rare 1000 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemVR)      
            magRolls=DiceRolls(1,4)
            print("These magic items from Table I were found in the treasure horde.\n")
            DictionRolls(magRolls,magicI)
            
        elif roll in range(86,91):
            objRolls=DiceRolls(1,10)
            print("These very rare 2500 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artVR)     
            magRolls=DiceRolls(1,4)
            print("These magic items from Table I were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicI)
            
        elif roll in range(91,96):
            objRolls=DiceRolls(1,4)
            print("These very rare 7500 gp art objects were found in the treasure horde.\n")
            summary.art=DictionRolls(objRolls,artL)     
            magRolls=DiceRolls(1,4)
            print("These magic items from Table I were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicI)
            
        elif roll in range(96,101):
            objRolls=DiceRolls(1,8)
            print("These legendary 5000 gp gems were found in the treasure horde.\n")
            summary.gems=DictionRolls(objRolls,gemL)     
            magRolls=DiceRolls(1,4)
            print("These magic items from Table I were found in the treasure horde.\n")
            summary.magic=DictionRolls(magRolls,magicI)

            
    elif hordeChoice.lower() in ("5", "exit"):
        return False

    print("\n* * * * * * End Horde Treasure * * * * * *\n\n\n")
    summary.printContents()
    return True




#Main Line
input("Hello.  Welcome to the Dungeon's and Dragon's 5th Edition Treasure Generator made by me, Wesley Wheeler.  Please press enter to get started -> ")
while(1):
    module=str(input("\nWhich module would you like to run?\n 1: Manual Input\n 2: Randomly Generated \n -> ")) 
    while module.lower() not in ("1", "manual", "manual input", "2", "random", "randomly generated"):
        module=str(input("That is not a valid selection.  Be sure to select a number or the appropriate module name. \nPlease try again -> "))

    if module.lower() in ("1", "manual", "manual input"):
        moduleLoop=True
        while (moduleLoop==True):
            moduleLoop=ManualMode()
    elif module.lower() in ("2", "random", "randomly generated"):
        moduleLoop=True
        while (moduleLoop==True):
            moduleLoop=RNG()


        

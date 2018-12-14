####################################
# Made by Joshua Donahue


####################################
import randCharGeneration
from randCharGeneration import *

import random

import pygame

pygame.init()

### charData ###################################################
# object class that decides and stores all data related to
# game characters







################################################################
class charData(object):
    #records the size of the party
    __partySize = 0
    def __init__(self, name, isMain):
        #adds a party member every time a new instance of the class charData is created
        __partySize+=1

        #checks via boolean to see if user is creating the main character or not
        if isMain == True:
            self.__name = name
            active = True

            #while loop used to determine 
            while active == True:
                self.__gender = str(input("What is your gender?\n"))
                #Each area provides a different set of stats indicitive of where you grew up
                self.__startArea = str(input("Where did you grow up?\n(City, Barracks, Lab)\n"))
                if self.startArea == "City":   #More Brutish
                    self.__health = random.randint(50,65)
                    self.__strength = random.randint(6,8)
                    self.__defence = random.randint(4,7)
                    self.__vitality = random.randint(32,35)
                    self.__intellect = random.randint(1,3)
                    self.__luck = random.randint(1,10)
                    active = False
                elif self.startArea == "Barracks":   #Middle of the Road
                    self.__health = random.randint(55,75)
                    self.__strength = random.randint(4,7)
                    self.__defence = random.randint(3,6)
                    self.__vitality = random.randint(28,32)
                    self.__intellect = random.randint(3,5)
                    self.__luck = random.randint(1,10)
                    active = False
                elif self.startArea == "Lab":   #Usually of higher education (A little lucky too)
                    self.__health = random.randint(50,75)
                    self.__strength = random.randint(3,5)
                    self.__defence = random.randint(2,6)
                    self.__vitality = random.randint(25,30)
                    self.__intellect = random.randint(6,9)
                    self.__luck = random.randint(3,10)
                    active = False
                else:
                    print(self.start, " is not a place.")
        else:
            self.__name,self.gender = firstNameGenerator()
            self.__name+= lastNameGenerator()
            #Sets a random personlity influencing their intelligence and aggresiveness
            #self.__personality = personalityGenerator(gender)   #make later
            self.__health = random.randint(40,75)
            self.__strength = random.randint(3,8)
            self.__defence = random.randint(2,7)
            self.__vitality = random.randint(25,35)
            self.__intellect = random.randint(1,8)
            self.__luck = random.randint(1,10)
            
    #modify parameters:
    def set_health(self,healthMod):
        self.__health+=healthMod
        
    def set_atk(self,strMod):
        self.__strength+=atkMod
        
    def set_def(self,defMod):
        self.__defence+=defMod
        
    def set_vit(self,vitMod):
        self.__vitality+=vitMod
        
    def set_int(self,intMod):
        self.__intelligence+=intMod
        
    def set_luck(self,luckMod):
        self.__luck+=luckMod
        
    #get parameters:
    def get_gender(self):
        return self.__gender
    def get_health(self):
        return self.__health
    def get_attack(self):
        return self.__strength
    def get_defense(self):
        return self.__defence
    def get_vit(self):
        return self.__vitality
    def get_int(self):
        return self.__intellect
    def get_luck(self):
        return self.luck
    def __str__(self): #prints all stats
        print("Stats of ",self.__name,":\nGender: ",self.__gender,", Health: ",self.__health,", Strenth: ",self.__strength,", Defense: ",self.__defence,", Vitality: ",self.__vitality,", Intellect: ",self.__intellect,", Luck: ",self.__luck,"\n")

### partySetup() ##################################################
#Defines a party list with object attributes from class charData()



#--- Plans for party design: -------
#an array containing up to three party members 

###################################################################

def mainSetup(isStart):
#never runs this code again
    name = str(input("Please enter a name for your character: "))
    mainChar = charData(name, True) #True makes it so 'inputName' is used
    mainChar.allStats()
    print(mainChar.get_attack())

def party(location):     
    #Creates party from diffrent locations
    party = []
    for chars in range (0,3):
        party.append(charData("zzz",False))
    for i in party:
        i.__str__()
 




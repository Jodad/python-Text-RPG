# Stores information regarding materials

import random
import math

### toolMaterials #########################################################
# Universal Materials Class (used as toolMaterials."material name")
# Has three (3) stats with slight varience
# Name of matrial is auto assigned by the method to the class object
#
# = Matrials: (4 main materials tools can be made of)
# * Iron: Weakest material with lacking efficiency
# * Silver: Not rare and usually contains a slight amount of magic
#           not enough to be of any use besides its unnatural durability
#           Magic infused so it comes with a gem slot
# * Steel: Tough metal used by knights, decent durability and efficiency
# * Mythril: Legendary hard to come by material lighter yet more durable
#            than steel. Magic infused so it comes with a gem slot
#
# Each tool material comes with stats in durability, efficiency and a boolean
# for gems (If there is one or not)
#
# = Stats: (4 main weapon stats)
# * Durability: Determines how long tool will last
# * Efficeincy: How much of its task it is able to accomplish in one use
# * gemSlot: boolean determining whether there is a slot to put gems
#            (Gem slots can be added with magic enfusion)
###########################################################################
class toolMaterials(object):
    
    def iron():
        dur = random.randint(300,400)       #durability
        #Next part determines what name tag will be assigned for its quality
        dur_tag = ""                        #Defaults to nothing
        if dur <= 320:
            dur_tag = "Shabby"
        elif dur == 390:
            dur_tag = "Perfect"
        eff = 1                             #efficiency
        gemSlot = False
        dataList = ["iron", dur, dur_tag, gemSlot, eff]
        return dataList
                    #{'metal type':"iron", 'durability':dur, 'name tag':dur_tag, 'gem slot':gemSlot, 'efficiency':eff}    #name, durability, tag, gemSlot, efficiency
    
    def silver():
        dur = random.randint(350,450)       #durability
        #Next part determines what name tag will be assigned for its quality
        dur_tag = ""                        #Defaults to nothing
        if dur < 370:
            dur_tag = "Shabby"
        elif dur >= 440:
            dur_tag = "Perfect"
        eff = 1                             #efficiency
        gemSlot = True
        return ("silver", dur, dur_tag, gemSlot, eff)    #name, durability, tag, gemSlot, efficiency
    
    def steel():
        dur = random.randint(550,800)       #durability
        #Next part determines what name tag will be assigned for its quality
        dur_tag = ""                        #Defaults to nothing
        if dur <= 580:
            dur_tag = "Shabby"
        elif dur >= 790:
            dur_tag = "Perfect"
        eff = 2                             #efficiency
        gemSlot = False
        return ("steel", dur, dur_tag, gemSlot, eff)    #name, durability, tag, gemSlot, efficiency
    
    def mythril():
        dur = random.randint(900,1200)      #durability
        #Next part determines what name tag will be assigned for its quality
        dur_tag = ""                        #Defaults to nothing
        if dur <= 950:
            dur_tag = "Shabby"
        elif dur >= 1180:
            dur_tag = "Perfect"
        eff = 3                             #efficiency
        gemSlot = True
        return ("mythril", dur, dur_tag, gemSlot, eff)    #name, durability, tag, gemSlot, efficiency

### weaponMaterials #############################################################
# Universal Materials Class (used as weaponMaterials."material name")
# Has four (4) stats with slight varience
# Name of matrial is auto assigned by the method to the class object
#
# = Matrials: (4 main materials weapoins can be made of)
# * Iron: Weakest material with lacking efficiency
# * Silver: Not rare and usually contains a slight amount of magic
#           not enough to be of any use besides its unnatural durability
#           Magic infused so it comes with a gem slot
# * Steel: Tough metal used by knights, decent durability and efficiency
# * Mythril: Legendary hard to come by material lighter yet more durable
#            than steel. Magic infused so it comes with a gem slot
#
# Each weapon material comes with stats in durability, efficiency, attack damage
# and a boolean for gems (If there is one or not)
#
# = Stats: (4 main weapon stats)
# * Durability: Determines how long tool will last
# * Efficeincy: How much of its task it is able to accomplish in one use
# * Attack: int influcenced by the weapons level. It's just a base attak damage
#           that will be modified later
# * gemSlot: boolean determining whether there is a slot to put gems
#            (Gem slots can be added with magic enfusion)
#################################################################################
class weaponMaterials(object):

    def iron(weap_level):
        dur = randint(300,400)              #durability
        #Next part determines what name tag will be assigned for its quality
        dur_tag = ""                        #Defaults to nothing
        if dur <= 320:
            dur_tag = "Shabby"
        elif dur >= 390:
            dur_tag = "Perfect"
        eff = 1                             #efficiency
        atk = randint( (4 + math.ceil(weap_level/5)), (5 + math.ceil(weap_level/4)) )          #attack
        gemSlot = False
        return "iron", dur, dur_tag, gemSlot, eff, atk        #name,durability,effieciency
    
    def silver(weap_level):
        dur = randint(350,450)              #durability
        #Next part determines what name tag will be assigned for its quality
        dur_tag = ""                        #Defaults to nothing
        if dur <= 375:
            dur_tag = "Shabby"
        elif dur >= 440:
            dur_tag = "Perfect"
        eff = 1                             #efficiency
        atk = randint( (7 + math.ceil(weap_level/4)), (9 + math.ceil(weap_level/4)) )          #attack
        gemSlot = True
        return "silver", dur, dur_tag, gemSlot, eff, atk        #name,durability,effieciency
    
    def steel(weap_level):
        dur = randint(550,800)              #durability
        #Next part determines what name tag will be assigned for its quality
        dur_tag = ""                        #Defaults to nothing
        if dur <= 580:
            dur_tag = "Shabby"
        elif dur >= 790:
            dur_tag = "Perfect"
        eff = 2                             #efficiency
        atk = randint( (12 + math.ceil(weap_level/4)), (16 + math.ceil(weap_level/3)) )          #attack
        gemSlot = False
        return "steel", dur, dur_tag, gemSlot, eff, atk        #name,durability,effieciency

    
    def mythril(weap_level):
        dur = randint(900,1200)             #durability
        #Next part determines what name tag will be assigned for its quality
        dur_tag = ""                        #Defaults to nothing
        if dur <= 950:
            dur_tag = "Shabby"
        elif dur >= 1180:
            dur_tag = "Perfect"
        eff = 3                             #efficiency
        atk = randint( (20 + math.ceil(weap_level/3)), (26 + math.ceil(weap_level/3)) )          #attack
        gemSlot = True
        return "mythril", dur, dur_tag, gemSlot, eff, atk        #name,durability,effieciency


### armorMaterials #############################################################
# Universal Materials Class (used as armorMaterials."material name")
# Has four (4) stats with slight varience
# Name of matrial is auto assigned by the method to the class object
#
# = Matrials: (4 main materials armors can be made of)
# * Iron: Weakest material with lacking efficiency
# * Silver: Not rare and usually contains a slight amount of magic
#           not enough to be of any use besides its unnatural durability
#           Magic infused so it comes with a gem slot
# * Steel: Tough metal used by knights, decent durability and efficiency
# * Mythril: Legendary hard to come by material lighter yet more durable
#            than steel. Magic infused so it comes with a gem slot
#
# Each armor material comes with stats in durability, efficiency, defense
# and a boolean for gems (If there is one or not)
#
# = Stats: (4 main weapon stats)
# * Durability: Determines how long tool will last
# * Efficeincy: How much of its task it is able to accomplish in one use
# * Defense: int influcenced by the weapons level. It's just a base attak damage
#           that will be modified later
# * gemSlot: boolean determining whether there is a slot to put gems
#            (Gem slots can be added with magic enfusion)
#################################################################################
class weaponMaterials(object):

    def iron(weap_level):
        dur = randint(300,400)              #durability
        #Next part determines what name tag will be assigned for its quality
        dur_tag = ""                        #Defaults to nothing
        if dur <= 320:
            dur_tag = "Shabby"
        elif dur >= 390:
            dur_tag = "Perfect"
        eff = 1                             #efficiency
        defn = randint( (3 + math.ceil(weap_level/5)), (4 + math.ceil(weap_level/4)) )          #attack
        gemSlot = False
        return "iron", dur, dur_tag, gemSlot, eff, defn        #name,durability,effieciency
    
    def silver(weap_level):
        dur = randint(350,450)              #durability
        #Next part determines what name tag will be assigned for its quality
        dur_tag = ""                        #Defaults to nothing
        if dur <= 370:
            dur_tag = "Shabby"
        elif dur >= 440:
            dur_tag = "Perfect"
        eff = 1                             #efficiency
        defn = randint( (5 + math.ceil(weap_level/4)), (7 + math.ceil(weap_level/4)) )          #attack
        gemSlot = True
        return "silver", dur, dur_tag, gemSlot, eff, defn       #name,durability,effieciency
    
    def steel(weap_level):
        dur = randint(550,800)              #durability
        #Next part determines what name tag will be assigned for its quality
        dur_tag = ""                        #Defaults to nothing
        if dur <= 600:
            dur_tag = "Shabby"
        elif dur >= 790:
            dur_tag = "Perfect"
        eff = 2                             #efficiency
        defn = randint( (8 + math.ceil(weap_level/4)), (12 + math.ceil(weap_level/3)) )          #attack
        gemSlot = False
        return "steel", dur, dur_tag, gemSlot, eff, defn        #name,durability,effieciency
    
    def mythril(weap_level):
        dur = randint(900,1200)             #durability
        #Next part determines what name tag will be assigned for its quality
        dur_tag = ""                        #Defaults to nothing
        if dur <= 950:
            dur_tag = "Shabby"
        elif dur >= 1180:
            dur_tag = "Perfect"
        eff = 3                             #efficiency
        defn = randint( (15 + math.ceil(weap_level/3)), (19 + math.ceil(weap_level/3)) )          #attack
        gemSlot = True
        return "mythril", dur, dur_tag, gemSlot, eff, defn        #name,durability,effieciency



def main():
    a = toolMaterials.iron
    print(a)



main()



        

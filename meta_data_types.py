#Metadata for tools, weapons and armors

import random


### toolMeta_data ##########################################
# Universal class that assigns bonuses to tools in game
# takes a 'data_type' that assigns an enhancement a tool
# with slight variance
# For tools, influence efficiency and durability
# * Efficiency: More items or Faster
# * Durability: Tool and Effects last longer
#
# = Enhancements:
# * Basic: No additional effects
# * Uncommon: Small durability bonus
# * Rare: Mid durabillity and efficiency bonus
# * Relic: High durability and effieciency bonus
# 
########################################################
class toolMeta_data(object):

    def __init__(self, data_type):
        if data_type == "basic":
            self.__rarity = data_type
            
        elif data_type == "uncommon":
            self.__rarity = data_type
            self.__dur_bonus = random.randint(100,200)
            self.__eff_bonus = 0
            
        elif data_type == "rare":
            self.__rarity = data_type
            self.__dur_bonus = random.randint(200,400)
            self.__eff_bonus = random.randint(0,1)

        elif data_type == "relic":
            self.__rarity = data_type
            self.__dur_bonus = random.randint(600,1000)
            self.__eff_bonus = random.randint(1,2)

    def getRarity(self):
        return self.__rarity

    def getDurBonus(self):
        return self.__dur_bonus

    def getEffBonus(self):
        return self.__eff_bonus

    def increaseRarity(self, data_type):
        if data_type == "basic":
            self.__rarity = data_type
            
        elif data_type == "uncommon":
            self.__rarity = data_type
            self.__dur_bonus = random.randint(100,200)
            self.__eff_bonus = 0
            
        elif data_type == "rare":
            self.__rarity = data_type
            self.__dur_bonus = random.randint(200,400)
            self.__eff_bonus = random.randint(0,1)

        elif data_type == "relic":
            self.__rarity = data_type
            self.__dur_bonus = random.randint(600,1000)
            self.__eff_bonus = random.randint(1,2)
        
            
### weaponMeta_data ##########################################
# Universal class that assigns bonuses to tools in game
# takes a 'data_type' that assigns an enhancement a tool
# with slight variance
# For tools, influence efficiency and durability
# * Efficiency: More items or Faster
# * Durability: Tool and Effects last longer
#
# = Enhancements:
# * Basic: No additional effects
# * Uncommon: Small durability bonus
# * Rare: Mid durabillity and efficiency bonus
# * Relic: High durability and effieciency bonus
# 
########################################################
class weaponMeta_data(object):
    
    def __init__(self, data_type):
        if data_type == "Basic":
            None

### armorMeta_data ##########################################
# Universal class that assigns bonuses to tools in game
# takes a 'data_type' that assigns an enhancement a tool
# with slight variance
# For tools, influence efficiency and durability
# * Efficiency: More items or Faster
# * Durability: Tool and Effects last longer
#
# = Enhancements:
# * Basic: No additional effects
# * Uncommon: Small durability bonus
# * Rare: Mid durabillity and efficiency bonus
# * Relic: High durability and effieciency bonus
# 
########################################################
class armorMeta_data(object):

    def __init__(self, data_type):
        if data_type == "Basic":
            None

### itemMeta_data ##########################################
# Universal class that assigns bonuses to tools in game
# takes a 'data_type' that assigns an enhancement a tool
# with slight variance
# For tools, influence efficiency and durability
# * Efficiency: More items or Faster
# * Durability: Tool and Effects last longer
#
# = Enhancements:
# * Basic: No additional effects
# * Uncommon: Small durability bonus
# * Rare: Mid durabillity and efficiency bonus
# * Relic: High durability and effieciency bonus
# 
########################################################       
class itemMeta_data(object):

    def __init__(self, data_type):
        if data_type == "Basic":
            None

            
        

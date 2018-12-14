#Stores information regarding models, texture and stats for weapons
import meta_data_types

class weapon_data(object):

    def __init__(self,weapon_name,weapon_type,weapon_material,meta_data):
        if weapon_type != "Sword" or weapon_type != "Spear" or weapon_type != "Bow" or weapon_type != "Shield":
            print("Error in 'weapon_data'\nInvalid weapon type: ", weapon_type, "\nFor weapon: ", weapon_name)
            input()
            quit()

        self.__weapon_name = weapon_name
        self.__weapon_type = weapon_type
        self.__weapon_type,self.__weapon_dur,self.__weapon_eff, self.__weapon_attack = weapon_material #Uses subclass in 
        
        
        

#######################

def main(): #Test main
    sword = weapon_data("Sword","Sword","Iron")
    

main()

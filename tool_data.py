#Stores information regarding models, texture and stats for tools
from meta_data_types import toolMeta_data
from materials_data import toolMaterials

### tool_data ###########################################################
#
#
# tool_name doesn't have to be filled unless user wants to make own tool
# with custom name
#########################################################################
class tool_data(object):

    def __init__(self,tool_name, tool_type, tool_material, meta_data):
        #if tool_type != "axe" or tool_type != "pickaxe" or tool_type != "hammer":
        #    print("Error in 'tool_data'\nInvalid tool_type: ", tool_type, "\nFor tool: ", tool_name)
        #    input()
        #    quit()
            
        self.__tool_type = tool_type
        (self.__tool_material,self.__tool_dur,self.__tool_dur_tag,self.__tool_eff) = tool_material
        self.__tool_rarity, self.__tool_dur_bonus, self.__tool_eff_bonus = meta_data    #pulls from meta_data_types.py
        if tool_name == "":
            self.__tool_name = self.__tool_rarity + self.__tool_dur_tag + self.__tool_material + self.__tool_type
        else:
            self.__tool_name = tool_name

    def getToolName(self):
        return self.__tool_name
        
        
        

#######################

def main(): #Test for forge menu 
    #Forge inputs:

    #name = str(input("Enter a name or hit enter to auto generate: "))
    #tool_type = str(input("Enter a tool type: "))
    #material = str(input("Enter a material: "))
    #rarity = str(input("Rarity: "))
    #axe = tool_data(name,tool_type,material,rarity)

    pick = tool_data("", "axe", toolMaterials.iron, toolMeta_data("uncommon"))
    print(pick.getToolName())

main()

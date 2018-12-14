### Credit #######################################
# Created by Joshua Donahue
# EMail: Jdonahue98@gmail.com or Jadonahue@mun.ca
#
# With help from Charles Atisele
##################################################

import randCharGeneration
import class_list

import random

### char_data ####################################################
# Generates character data with class
#
#
##################################################################
class char_data(object):

    def __init__(self,name,char_class):
        self.__name = name
        self.__class_data = class_data(char_class)


def main():
    name = str(input("Enter a name: "))
    mainclass = str(input("Pick a class: "))
    
    maincharacter = char_data(name, mainclass)
    

main()
    

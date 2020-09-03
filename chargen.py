__version__ = '0.2'
__author__ = 'Lorkh4n' # I need to change this name, am open to suggestions

import random
import time
import json
from distutils import util
from more_itertools import locate

class Character:
    def __init__(self,level,owner,name,race,profession,stats,background,equipment):
        self.level = 1
        self.owner = owner
        self.name = name
        self.race = race
        self.profession = profession
        self.stats = stats
        self.background = background
        self.equipment = equipment
    
    def __str__(self):
        return f"\n{self.name}\n Level {self.level} {self.profession}\n {self.stats}"

    def levelup(self):
        pass
    
class CreateCharacter:
    basic_details = "CreateCharacter(owner,name)"
    profession_list = ["artificer","barbarian","bard","cleric","druid","fighter","monk","paladin","ranger","rogue","sorcerer","warlock","wizard"]
    race_list = ["dwarva","forged","human","kirku","mabonde","muti","oread","ronahi","semayawi","tewagi","vekiri","volyri","wulfe","yuan"]
    stats_list = ["strength","wisdom","charisma","dexterity","constitution","intelligence"]
    character_dict = {}
    rd = open("race_dict.json")
    race_dict = json.load(rd)
    
    def __init__(self,owner,name,seed=None):
        self.owner = owner
        self.name = name
        self.seed = str(owner + "_" + str(time.monotonic_ns())[3:9] + "_" + name)

    def function_call(self,function,arguments=None):
        function_call = getattr(self,function)
        function_call(arguments)

    def build_background(self):
        pass

    def build_equipment(self):
        pass

    def build_level(self):
        pass

    def build_profession(self,listed_professions = profession_list,profession_choice = False):
        if profession_choice == False:
            profession_choice = input("Please enter your class: ")
        profession_index = []
        for i in range(0,len(listed_professions)):
            if profession_choice.lower() in listed_professions[i]:
                profession_index.append(listed_professions[i])
        else:
            if len(profession_index) > 1:
                final_profession = input("There are " + str(len(profession_index)) + " options for \"" + profession_choice + "\". Which would you like:\n" + "\n".join(profession_index) + "\n\n")
                self.build_profession(profession_index,final_profession)
            elif len(profession_index) == 1:
                print(profession_index)
                self.function_call("confirm_profession",profession_index[0])
            else: 
                print("You haven't selected a valid class. Please enter one of the following:\n" + "\n".join(self.profession_list))
                self.build_profession()

    def build_race(self,listed_races = race_list,race_choice = False):
        if race_choice == False:
            race_choice = input("Please enter your race: ")
        race_index = []
        for i in range(0,len(listed_races)):
            if race_choice.lower() in listed_races[i]:
                race_index.append(listed_races[i])
        else:
            if len(race_index) > 1:
                final_race = input("There are " + str(len(race_index)) + " options for \"" + race_choice + "\". Which would you like:\n" + "\n".join(race_index) + "\n\n")
                self.build_race(race_index,final_race)
            elif len(race_index) == 1:
                print(race_index)
                self.function_call("confirm_race",race_index[0])
            else: 
                print("You haven't selected a valid race. Please enter one of the following:\n" + "\n".join(self.race_list))
                self.build_race()

    def build_stats(self):
        print(self.seed)
        attributes = [element.lower() for element in self.stats_list]
        print("\nSTATS\n")
        final_stat = "Ready"
        stats_dict = {}
        sublist_counter = 5
        while attributes:
            die_roll = random.randint(1,6)
            stat_array = [die_roll, die_roll, die_roll]
            if final_stat == "Ready":
                final_stat = sum(stat_array)
            print("You rolled: " + str(final_stat) + ".\n")
            choice = input("What would you like to put this stat in? Your choices are: " + str(attributes) + ":\n")
            for item in attributes:
                if choice.lower() in item:
                    print("Your " + item.title() + " stat is: " + str(final_stat) + ".\n")
                    attributes.remove(item)
                    stats_dict[item] = final_stat
                    final_stat = "Ready"
                    break
                else:
                    sublist_counter -= 1
                    if sublist_counter == 0:
                        print("Sorry, that isn't an available choice. Please select from the following:\n" + str(attributes))
        else:
            self.writeback("stats",stats_dict)

    def random_background(self):
        pass

    def random_equipment(self):
        pass

    def random_level(self):
        pass

    def random_profession(self):
        pass

    def random_race(self):
        pass

    def random_stats(self):
        pass

    def this_test(self):
        print(self.race_dict["dwarva"])

    def writeback(self,character_key,character_value):
        self.character_dict[character_key] = character_value

    def confirm_race(self,race,first_try=True):
        if first_try == True:
            print(self.race_dict[race]) ################################### FIX THIS SHIT, FUCKER
        confirm_race = input("Is this the race you choose? yes/no\n")
        if confirm_race in "yes":
            self.character_dict["race"]:race
        elif confirm_race in "no":
            self.build_race(self.race_list,False)
        else:
            print("Please type either \"yes\" or \"no\".\n")
            self.confirm_race(race,False)


    # def choose_dwarva(self,first_try=True):
    #     if first_try == True:
    #         print("The Dwarva of the undermountain caverns of Lia Fál are a proud and stoic race. They reside in catacombic tunnels hollowed out over centuries from natural karsts and pyroducts, and their time in this harsh subterranean climate has hardened them both physically and mentally.\n")
    #     confirm_race = input("Is this the race you choose? yes/no\n")
    #     if confirm_race in "yes":
    #         self.character_dict["race"]:"Dwarva"
    #     elif confirm_race in "no":
    #         self.build_race(self.race_list,False)
    #     else:
    #         print("Please type either \"yes\" or \"no\".\n")
    #         self.choose_dwarva(False)


    # def choose_forged(self,first_try=True):
    #     if first_try == True:
    #         print("Arriving in Rodinia after fleeing their far off homeland to the West that they are unwilling, or unable, to discuss, the Forged are more machine than man. They often put their bodies completely on the line in battle, as their mechanical bodies enable them to replace any broken parts.\n")
    #     confirm_race = input("Is this the race you choose? yes/no\n")
    #     if confirm_race in "yes":
    #         self.character_dict["race"]:"Forged"
    #     elif confirm_race in "no":
    #         self.build_race(self.race_list,False)
    #     else:
    #         print("Please type either \"yes\" or \"no\".\n")
    #         self.choose_forged(False)

    # def choose_human(self,first_try=True):
    #     if first_try == True:
    #         print("Humans are known for living abnormally long lives for adventurers, thanks almost entirely to the race's unrelenting tenacity. Humans have had to fight tooth and nail for every inch of land they own, and continue to fight on all fronts to prevent this same land from being reconquered.\n")
    #     confirm_race = input("Is this the race you choose? yes/no\n")
    #     if confirm_race in "yes":
    #         self.character_dict["race"]:"Human"
    #     elif confirm_race in "no":
    #         self.build_race(self.race_list,False)
    #     else:
    #         print("Please type either \"yes\" or \"no\".\n")
    #         self.choose_human(False)

    # def choose_kirku(self):
    #     pass
    
    # def choose_mabonde(self):
    #     pass
    
    # def choose_muti(self):
    #     pass
    
    # def choose_oread(self):
    #     pass

    # def choose_ronahi(self):
    #     pass

    # def choose_semayawi(self):
    #     pass

    # def choose_tewagi(self):
    #     pass

    # def choose_vekiri(self):
    #     pass

    # def choose_volyri(self):
    #     pass

    # def choose_wulfe(self):
    #     pass

    # def choose_yuan(self):
    #     pass

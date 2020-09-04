__version__ = '0.2'
__author__ = 'Lorkh4n' # I need to change this name, am open to suggestions

import random
import time
import json
import re
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
    profession_list = ["artificer","barbarian","bard","cleric","druid","fighter","monk","paladin","ranger","rogue","sorcerer","warlock","wizard"]
    race_list = ["dwarva","forged","human","kirku","ghena","ravodit","oread","ronahi","semayawi","vadasj","vekiri","volyri","wulfe","yuan"]
    stats_list = ["strength","wisdom","charisma","dexterity","constitution","intelligence"]
    choice_dict = {"build":"build_","random":"random_"}
    basic_choice_list = ["race","class","stats","background","equipment","level"]
    exception_dict = {"build":"random_","random":"build_"}
    character_dict = {}
    race_dict = json.load(open("race_dict.json"))
    profession_dict = json.load(open("profession_dict.json"))
    
    def __init__(self,owner,name,seed=None):
        self.owner = owner
        self.name = name
        self.seed = str(owner + "_" + str(time.monotonic_ns())[3:9] + "_" + name)

    def function_call(self,function,arguments=False):
        function_call = getattr(self,function)
        if arguments:
            function_call(arguments)
        elif arguments == False:
            function_call()
        else:
            print("This has errored in an unforseen way. Oops.")
            exit()   

    def build_background(self):
        pass

    def build_equipment(self):
        pass

    def build_level(self):
        pass

    def build_class(self,listed_professions = profession_list,profession_choice = False):
        if profession_choice == False:
            profession_choice = input("Please enter your class: ")
        profession_index = []
        for i in range(0,len(listed_professions)):
            if profession_choice.lower() in listed_professions[i]:
                profession_index.append(listed_professions[i])
        else:
            if len(profession_index) > 1:
                final_profession = input("There are " + str(len(profession_index)) + " options for \"" + profession_choice + "\". Which would you like:\n" + "\n".join(profession_index) + "\n\n")
                self.build_class(profession_index,final_profession)
            elif len(profession_index) == 1:
                print(profession_index)
                self.function_call("confirm_profession",profession_index[0])
            else: 
                print("You haven't selected a valid class. Please enter one of the following:\n" + "\n".join(self.profession_list))
                self.build_class()

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

    def random_class(self):
        profession_seed = random.randint(0,12)
        profession = list(self.profession_dict.keys())[profession_seed]
        self.writeback("Class",profession)
        print(self.character_dict)

    def random_race(self):
        race_seed = random.randint(0,13)
        race = list(self.race_dict.keys())[race_seed]
        self.writeback("Race",race)

    def random_stats(self):
        pass

    def this_test(self):
        print(self.race_dict["dwarva"])

    def writeback(self,character_key,character_value):
        self.character_dict[f"{character_key}"] = character_value

    def confirm_race(self,race,first_try=True):
        if first_try == True:
            print(self.race_dict[race])
        confirm_race = input("Is this the race you choose? yes/no\n")
        if confirm_race in "yes":
            self.writeback("race",race)
        elif confirm_race in "no":
            self.build_race(self.race_list,False)
        else:
            print("Please type either \"yes\" or \"no\".\n")
            self.confirm_race(race,False)

    def confirm_profession(self,profession,first_try=True):
        if first_try == True:
            print(self.profession_dict[profession])
        confirm_profession = input("Is this the class you choose? yes/no\n")
        if confirm_profession in "yes":
            self.writeback("class",profession)
        elif confirm_profession in "no":
            self.build_race(self.profession_list,False)
        else:
            print("Please type either \"yes\" or \"no\".\n")
            self.confirm_profession(profession,False)
    
    def initial_function(self):
        self.writeback("name",self.name)
        self.writeback("player",self.owner)
        player_choice = input("Would you like to \"build\" your character, or leave it to \"random\"isation?\nFeel free to make an \"except\"ion for \"race\", \"class\", \"stats\", \"background\", \"equipment\", or \"level\".\nYour choice: ")
        parsed_choice = player_choice.lower().split()
        if "build" or "random" in parsed_choice[0]:
            while parsed_choice[1] in "except":
                regex_search = re.compile(f"{parsed_choice[1]}(.*)$").search(player_choice).group(1).split()
                for char_attribute in regex_search:
                    exception_bor = self.exception_dict[parsed_choice[0]]
                    function_name = f"{exception_bor}{char_attribute}"
                    self.function_call(function_name)
                    self.basic_choice_list.remove(char_attribute)
                else:
                    parsed_choice.remove(parsed_choice[1])
            while self.basic_choice_list:
                for char_attribute in self.basic_choice_list:
                    choice_bor = self.choice_dict[parsed_choice[0]]
                    function_name = f"{choice_bor}{char_attribute}"
                    self.function_call(function_name)
                    self.basic_choice_list.remove(char_attribute)

    def character_attributes(self):
        print(self.character_dict)
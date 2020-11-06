__version__ = '0.2'
__author__ = 'Chyr0s' 

import pyperclip
import random
import time
import json
import os
import string
from backgrounds import character_backgrounds

def clear():
    if os.name == "nt":
        _ = os.system("cls")
    elif os.name == "posix":
        _ = os.system("clear")
    else:
        print("Unable to determine OS.")


class Character:
    def __init__(self,owner,level,name,race,profession,stats,background,equipment):
        self.level = level
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
    race_dict = json.load(open("race_dict.json"))
    profession_dict = json.load(open("profession_dict.json"))
    overall_choice = {'bor':[],'eyn':[]}
    profession_list = list(profession_dict)
    race_list = list(race_dict)
    stats_list = ["strength","wisdom","charisma","dexterity","constitution","intelligence"]
    choice_dict = {"build":"build_","random":"random_"}
    basic_choice_list = ["race","class","stats","background","equipment"]
    exception_dict = {"build":"random_","random":"build_"}
    character_dict = {}
    player_choice_held = []
    punct_table = str.maketrans(dict.fromkeys(string.punctuation))
    
    def __init__(self,owner,name,seed=None):
        self.owner = owner
        self.name = name
        self.seed = str(owner + "_" + str(time.perf_counter_ns())[0:6] + "_" + name)

    def build_background(self):
        background_choice = input("What background would you like?\n").lower()
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
                clear()
                self.confirm_profession(profession_index[0])
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
                clear()
                self.confirm_race(race_index[0])
            else: 
                print("You haven't selected a valid race. Please enter one of the following:\n" + "\n".join(self.race_list))
                self.build_race()

    def build_stats(self):
        attributes = [element.lower() for element in self.stats_list]
        print("\nSTATS")
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
            self.writeback("Stats",stats_dict)

    def random_background(self):
        pass

    def random_equipment(self):
        pass

    def random_level(self):
        pass

    def random_class(self):
        profession_seed = random.randint(0,len(self.profession_list)-1)
        profession = list(self.profession_dict.keys())[profession_seed]
        self.writeback("Class",profession)

    def random_race(self):
        race_seed = random.randint(0,len(self.race_list)-1)
        race = list(self.race_dict.keys())[race_seed]
        self.writeback("Race",race)

    def random_stats(self):
        stats_dict = {}
        attributes = self.stats_list
        while attributes:
            for attribute in attributes:
                seed = self.seed + attribute
                random.seed(seed)
                die_roll = random.randint(1,6)
                stat_array = [die_roll, die_roll, die_roll, die_roll]
                del stat_array[stat_array.index(min(stat_array))]
                final_stat = sum(stat_array)
                stats_dict[attribute] = final_stat
                attributes.remove(attribute)
        else:
            self.writeback("Stats",stats_dict)

    def writeback(self,character_key,character_value):
        self.character_dict[f"{character_key}"] = character_value

    def confirm_race(self,race,first_try=True):
        if first_try == True:
            print(self.race_dict[race])
        confirm_race = input("Is this the race you choose? yes/no\n")
        if confirm_race in "yes":
            self.writeback("Race",race)
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
            self.writeback("Class",profession)
        elif confirm_profession in "no":
            self.build_race(self.profession_list,False)
        else:
            print("Please type either \"yes\" or \"no\".\n")
            self.confirm_profession(profession,False)
    
    def initial_function(self,bor=False):
        self.writeback("Name",self.name)
        self.writeback("Player",self.owner)
        if bor == False:
            bor = input('Would you like to "build" your character, or leave it to "random"isation?\nYour choice: ')
        if bor in 'build':
            bor = 'build'
            self.overall_choice['bor'] = bor
        elif bor in 'random':
            bor = 'random'
            self.overall_choice['bor'] = bor
        else:
            print("That's neither 'build' nor 'random'. Try again.")
            self.initial_function()
        eyn = input('Would you like to make an exception for any aspect of your character?\nie if you chose to build your character, but want to randomise your stats for instance, type "yes"; if not, type "no".\n')
        if eyn in 'yes':
            self.overall_choice['eyn'] = 'yes'
            print(self.overall_choice['eyn'])
        elif eyn in 'no':
            self.overall_choice['eyn'] = 'no'
        else:
            print("That's not 'yes' or 'no'. Try again.")
            self.initial_function(bor)
        self.initial_function_except(bor)
        
    def initial_function_except(self,bor):
        if self.overall_choice['eyn'] == 'yes':
            exception_str = input('Please enter the aspect(s) you would like to make exceptions for, out of "background", "class", "race", and "stats".\n')
            remove_punct = exception_str.translate(self.punct_table)
            chc = remove_punct.split()
            for ex in chc:
                if ex in self.basic_choice_list:
                    func_str = f"{self.exception_dict[bor]}{ex}"
                    call = getattr(self,func_str)
                    call()
                    self.basic_choice_list.remove(ex)                    
                else:
                    retry = input("Your choice of " + ex + " has caused an error. Would you like to select your exceptions again? y/n\n")
                    if retry in "yes":
                        self.initial_function_except(bor)
                    else:
                        print("OK, I will ignore that selection and continue.")
                        chc.remove(ex)
            else:
                self.initial_function_noexcept(bor)
        else:
            self.initial_function_noexcept(bor)

    def initial_function_noexcept(self,bor):
        self.overall_choice['eyn'] = None
        chc = self.basic_choice_list
        for choice in chc:
            func_str = f"{self.choice_dict[bor]}{choice}"
            call = getattr(self,func_str)
            call()

    def character_attributes(self):
        print(self.character_dict)

    def final_confirmation(self,player_choice=player_choice_held,first_try=True):
        if first_try == True:
            print(f"{self.character_dict}\n")
        confirm = input("Is this the character you choose? yes/no\n")
        if confirm in "yes":
            pyperclip.copy(f"{self.character_dict}")
            print("Confirmed. Your character attributes have been copied to your clipboard.")
            exit()
        elif confirm in "no":
            print("Denied. Sending character back into the aether. Please wait...")
            time.sleep(5)
            self.initial_function(player_choice)
        else:
            print("I am unable to decipher that response. Please try again.")
            time.sleep(1)
            self.final_confirmation(False)
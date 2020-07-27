#IMPORTS
import random
import os
import time

#GLOBALS
SEED = input("Please enter your character name: ")
ATTRIBUTES = ["strength","wisdom","charisma","dexterity","constitution","intelligence"]
CLASS_DICT = {"barbarian":["barbarian","berserker","berzerker"],
    "bard":["bard","minstrel","poet"],
    "cleric":["cleric","priest","healer"],
    "druid":["druid"],
    "fighter":["fighter","warrior"],
    "monk":["monk","pilgrim","martial artist"],
    "paladin":["paladin","crusader","zealot","pally"],
    "ranger":["ranger","hunter","wanderer"],
    "rogue":["rogue","thief","assassin"],
    "sorcerer":["sorcerer"],
    "warlock":["warlock","occultist"],
    "wizard":["wizard","Academic","academic"],
    "artificer":["artificer","tinkerer","inventor"]}
RACE_DICT = {"dwarva":["dwarva","dwarf","gnome"],
    "human":["human","man","person"],
    "kirku":["kirku"],
    "mabonde":["mabonde","plains","orc"],
    "muti":["muti","treeorc","barkskin"],
    "oread":["oread","roman"],
    "ronahi":["ronahi","missing","nomad"],
    "semayawi":["semayawi","celestial","angel"],
    "tewagi":["tewagi","hunter","roaming"],
    "vekiri":["vekiri","devil","demon"],
    "volyri":["volyri","frog","pixie"],
    "wulfe":["wulfe","werewolf","wolfkin"],
    "yuan":["yuan","apeling","monkey"],
    "forged":["forged","machine","cyborg"]}
CHOICE_LIST = [["build_race","roll_race"],["build_class","roll_class"],["choose_stats","roll_stats"]]
TOTAL_SEED = SEED + str(time.monotonic_ns())
random.seed(TOTAL_SEED)

#FUNCTIONS
def build_class():
    CLASS_CONTINUE = False
    profession,class_true = choose_class()
    while CLASS_CONTINUE == False:
        if class_true == True:
            print(profession)
            CLASS_CONTINUE = True
        elif class_true == False:
            print("\nNo, wait. That isn't right. Try again.\nChoose from the following:\n" + str(list(CLASS_DICT)))
            profession,class_true = choose_class()

def choose_class():
    char_class = input("Please enter your class: ")
    class_true = False
    for profession in CLASS_DICT:
        if char_class.lower() in CLASS_DICT[profession]:
            class_true = True
            break
    return(profession,class_true)

def roll_class():
    profession_seed = random.randint(0,12)
    profession = list(CLASS_DICT.keys())[profession_seed]
    print(profession)
    return(profession)

def build_race():
    RACE_CONTINUE = False
    race,race_true = choose_race()
    while RACE_CONTINUE == False:
        if race_true == True:
            print(race)
            RACE_CONTINUE = True
            return(RACE_CONTINUE)
        elif race_true == False:
            print("\nThat's not a race you fucking donkey. Try again.\nChoose from the following:\n" + str(list(RACE_DICT)))
            race,race_true = choose_race()

def choose_race():
    char_race = input("Please enter your race: ")
    race_true = False
    for race in RACE_DICT:
        if char_race.lower() in RACE_DICT[race]:
            race_true = True
            break
    return(race,race_true)

def roll_race():
    race_seed = random.randint(0,13)
    race = list(RACE_DICT.keys())[race_seed]
    print(race)
    return(race)

def build_stats():
    random.seed(SEED)
    attributes = [element.lower() for element in ATTRIBUTES]
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
        return(stats_dict)

def roll_stats():
    stats_dict = {}
    attributes = ATTRIBUTES
    while attributes:
        for attribute in attributes:
            seed = SEED + attribute
            random.seed(seed)
            die_roll = random.randint(1,6)
            stat_array = [die_roll, die_roll, die_roll, die_roll]
            del stat_array[stat_array.index(min(stat_array))]
            final_stat = sum(stat_array)
            stats_dict[attribute] = final_stat
            attributes.remove(attribute)
    else:
        print(stats_dict)
        return(stats_dict)

def no_exceptions(choice):
    if 'build' in choice:
        for item in CHOICE_LIST:
            if item[0] in globals():
                globals()[item[0]]()
    elif 'fates' in choice:
            for item in CHOICE_LIST:
                if item[1] in globals():
                    globals()[item[1]]()
    else:
        print("Either you've typo'd it or you tried breaking the code.")
        pick_n_choose()

def pick_n_choose():
    player_choice = input("Would you like to \"build\" your character, or leave it to the \"fates\"?\nFeel free to make an \"except\"ion for \"race\", \"class\", or \"stats\".\nYour choice: ")
    choice_dict = {"build":"build_","fates":"roll_"}
    basic_choice_list = ["race","class","stats"]
    exception_dict = {"build":"roll_","fates":"build_"}
    parsed_choice = player_choice.lower().split()
    if "except" in parsed_choice:
        exception = parsed_choice[parsed_choice.index("except") + 1]
        build_or_fates = parsed_choice[parsed_choice.index("except") - 1]
        for choice in basic_choice_list:
            if exception == choice:
                globals()[exception_dict[build_or_fates] + exception]()
            else:
                globals()[choice_dict[build_or_fates] + choice]()
    else:
        no_exceptions(parsed_choice)

#LETSGO
pick_n_choose()
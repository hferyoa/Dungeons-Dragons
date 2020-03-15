import random
import os

SEED = input("Please enter your character name: ")
ATTRIBUTES = ["Strength","Wisdom","Charisma","Dexterity","Constitution","Intelligence"]
ATTRIBUTE_DICT = {"Strength":["Strength","strength","STR","Str","str"],
    "Wisdom":["Wisdom","wisdom","WIS","Wis","wis"],
    "Charisma":["Charisma","charisma","CHA","Cha","cha"],
    "Dexterity":["Dexterity","dexterity","DEX","Dex","dex"],
    "Constitution":["Constitution","constitution","CON","Con","con"],
    "Intelligence":["Intelligence","intelligence","INT","Int","int"]}
CLASS_DICT = {"Barbarian":["Barbarian","barbarian","Berserker","berserker","Berzerker","berzerker","Barb","barb"],
    "Bard":["Bard","bard","Minstrel","minstrel","Poet","poet"],
    "Cleric":["Cleric","cleric","Priest","priest","Healer","healer"],
    "Druid":["Druid","druid","Drood","drood","Natureboi","natureboi"],
    "Fighter":["Fighter","fighter","Warrior","warrior","Grunt","grunt"],
    "Monk":["Monk","monk","Pilgrim","pilgrim","Martial Artist","martial artist","Martial artist"],
    "Paladin":["Paladin","paladin","Crusader","crusader","Zealot","zealot","Pally","pally"],
    "Ranger":["Ranger","ranger","Hunter","hunter","Wanderer","wanderer"],
    "Rogue":["Rogue","rogue","Thief","thief","Assassin","assassin"],
    "Sorcerer":["Sorcerer","sorcerer","Sorc","sorc","Haemagos","haemagos"],
    "Warlock":["Warlock","warlock","Lock","lock","Occultist","occultist"],
    "Wizard":["Wizard","wizard","Scientist","scientist","Academic","academic","Wiz","wiz"],
    "Artificer":["Artificer","artificer","Tinkerer","tinkerer","Inventor","inventor"]}
RACE_DICT = {"Dwarva":["Dwarva","dwarva","Dwarf","dwarf","Gnome","gnome"],
    "Human":["Human","human","Man","man","Person","person"],
    "Kirku":["Kirku","kirku","Zen","zen","Buddhist","buddhist"],
    "Mabonde":["Mabonde","mabonde","Plains","plains","Orc","orc"],
    "Muti":["Muti","muti","Treeorc","treeorc","Barkskin","barkskin"],
    "Oread":["Oread","oread","Roman","roman","Cold","cold"],
    "Ronahi":["Ronahi","ronahi","Missing","missing","Nomad","nomad"],
    "Semayawi":["Semayawi","semayawi","Celestial","celestial","Radiant","radiant"],
    "Tewagi":["Tewagi","tewagi","Hunter","hunter","Roaming","roaming"],
    "Vekiri":["Vekiri","vekiri","Devilkin","devilkin","Pact","pact"],
    "Volyri":["Volyri","volyri","Frog","frog","Pixie","pixie"],
    "Wulfe":["Wulfe","wulfe","Werewolf","werewolf","Wolfkin","wolfkin"],
    "Yuan":["Yuan","yuan","Apeling","apeling","Monkey","monkey"],
    "Forged":["Forged","forged","Machine","machine","Cyborg","cyborg"]}
random.seed(SEED)

def choose_class():
    char_class = input("Please enter your class: ")
    class_true = False
    for profession in CLASS_DICT:
        if char_class in CLASS_DICT[profession]:
            class_true = True
            break
    return(profession,class_true)
    
def roll_class():
    profession_seed = random.randint(0,12)
    profession = list(CLASS_DICT.keys())[profession_seed]
    return(profession)
    
def choose_race():
    char_race = input("Please enter your race: ")
    race_true = False
    for race in RACE_DICT:
        if char_race in RACE_DICT[race]:
            race_true = True
            break
    return(race,race_true)

def roll_race():
    race_seed = random.randint(0,13)
    race = list(RACE_DICT.keys())[race_seed]
    return(race)

def choose_stats():
    random.seed(SEED)
    attributes = ATTRIBUTES
    attribute_alias = ATTRIBUTE_DICT.values()
    print("\nSTATS\n")
    final_stat = "Ready"
    stats_dict = {}
    while attributes:
        die_roll = random.randint(1,6)
        stat_array = [die_roll, die_roll, die_roll]
        if final_stat == "Ready":
            final_stat = sum(stat_array)
        print("You rolled: " + str(final_stat) + ".\n")
        choice = input("What would you like to put this stat in? Your choices are: " + str(attributes) + ":\n")
        if choice in ATTRIBUTE_DICT[attribute_alias]:
            print("Fuckinghellthisworked")
            # print("Your " + choice + " stat is: " + str(final_stat) + ".\n")
            # attributes.remove(choice)
            # stats_dict[choice] = final_stat
            # final_stat = "Ready"
        else:
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
        return(stats_dict)

def pick_n_choose():
    player_choice = input("Would you like to \"build\" your character, or leave it to the \"fates\"?\nFeel free to make an \"except\"ion for \"race\", \"class\", or \"stats\".\nYour choice: ")
    parsed_choice = player_choice.split()
    choice_list = [["build_race","roll_race"],["build_class","roll_class"],["choose_stats","roll_stats"]]
    function_dict = {"build_race":build_race,"build_class":build_class,"choose_stats":choose_stats,"roll_race":roll_race,"roll_class":roll_class,"roll_stats":roll_stats}
    error_list = ["A Barbarian crushed your input. Try again.", "A Bard distracted your computer. Try again.", "This Cleric can't heal your input. Try again.", "A Druid polymorphed your input into a sheep. Try again.","A Fighter beat your choice in a duel. Try again.","Your choice has decided to leave and become a Monk. Try again.","A Paladin smited (smote?) your input. Try again.","A Ranger fed your input to her pet. Try again.","A Rogue assassinated your choice of words. Try again.","A Sorcerer incinerated your input. Try again.","A Warlock summoned and made a pact with a greater daemon just to turn your input to gibberish. Try again.","A Wizard turned the internals of the computer to jelly by mistake. Try again.","An Artificer didn't code this properly so it didn't work. Try again."]
    if "except" in parsed_choice:
        exception = parsed_choice[parsed_choice.index("except") + 1]
        except_choice = parsed_choice[parsed_choice.index("except") - 1]
        print(exception + " " + except_choice)
    else:
        if "build" in parsed_choice:
            for item in choice_list:
                if item[0] in function_dict:
                    function_dict[item[0]]()
        else:
            if "fates" in parsed_choice:
                print("fates")
            else:
                error_rng = random.randint(0,12)
                print(error_list[error_rng])
                return("try_again")

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
    
def build_race():
    RACE_CONTINUE = False
    race,race_true = choose_race()
    while RACE_CONTINUE == False:
        if race_true == True:
            print(race)
            RACE_CONTINUE = True
        elif race_true == False:
            print("\nThat's not a race you fucking donkey. Try again.\nChoose from the following:\n" + str(list(RACE_DICT)))
            race,race_true = choose_race()

def build(rorcors,to_build):
    rorcors_dict = {"race":RACE_DICT,"class":CLASS_DICT,"stats":ATTRIBUTE_DICT}
    tb_continue = False
    race_class_stats,r_c_s_true = to_build()
    while tb_continue == False:
        if r_c_s_true == True:
            print(r_c_s_true)
            tb_continue = True
        elif r_c_s_true == False:
            if rorcors in rorcors_dict:
                print("\nThat's not a " + rorcors + " you fucking donkey. Try again.\nChoose from the following:\n" + str(list(rorcors_dict[rorcors])))
                race_class_stats,r_c_s_true = to_build()

build("race",build_race)

# pick_n_choose()
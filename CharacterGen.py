import random
import os

SEED = input("Please enter your character name: ")
attributes = ["Strength","Wisdom","Charisma","Dexterity","Constitution","Intelligence"]
CLASS_DICT = {"Barbarian":["Barbarian","barbarian","Berserker","berserker","Berzerker","berzerker","Zerkah","zerkah"],
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
    for profession in CLASS_DICT:
        if char_class in CLASS_DICT[profession]:
            return(profession)

def roll_class():
    profession_seed = random.randint(0,12)
    profession = list(CLASS_DICT.keys())[profession_seed]
    return(profession)
    
def choose_race():
    char_race = input("Please enter your race: ")
    for race in RACE_DICT:
        if char_race in RACE_DICT[race]:
            return(race)

def roll_race():
    race_seed = random.randint(0,13)
    race = list(RACE_DICT.keys())[race_seed]
    return(race)

def choose_stats(race, profession, attributes):
    random.seed(SEED + race + profession)
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
        if choice in attributes:
            print("Your " + choice + " stat is: " + str(final_stat) + ".\n")
            attributes.remove(choice)
            stats_dict[choice] = final_stat
            final_stat = "Ready"
        else:
            print("Sorry, that isn't an available choice. Please select from the following:\n" + str(attributes))
    else:
        return(stats_dict)

def roll_stats(attributes):
    stats_dict = {}
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
    choice_dict = {"race":["choose_race","roll_race"],"class":["choose_class","roll_class"],"stats":["choose_stats","roll_stats"]}
    error_list = ["A Barbarian crushed your input. Try again.", "A Bard distracted your computer. Try again.", "This Cleric can't heal your input. Try again.", "A Druid polymorphed your input into a sheep. Try again.","A Fighter beat your choice in a duel. Try again.","Your choice has decided to leave and become a Monk. Try again.","A Paladin smited (smote?) your input. Try again.","A Ranger fed your input to her pet. Try again.","A Rogue assassinated your choice of words. Try again.","A Sorcerer incinerated your input. Try again.","A Warlock summoned and made a pact with a greater daemon just to turn your input to gibberish. Try again.","A Wizard turned the internals of the computer to jelly by mistake. Try again.","An Artificer didn't code this properly so it didn't work. Try again."]
    if "except" in parsed_choice:
        exception = parsed_choice[parsed_choice.index("except") + 1]
        except_choice = parsed_choice[parsed_choice.index("except") - 1]
        
    else:
        if "build" in parsed_choice:
            print("build")
        else:
            if "fates" in parsed_choice:
                print("fates")
            else:
                error_rng = random.randint(0,12)
                print(error_list[error_rng])
                return("try_again")
        
pick_n_choose()


# profession = roll_class()
# race = roll_race()

# print(choose_stats(race,profession,attributes))


# def stats():
#     array1 = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
#     array2 = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
#     array3 = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
#     array4 = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
#     array5 = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
#     array6 = [random.randint(1,6), random.randint(1,6), random.randint(1,6), random.randint(1,6)]
#     del array1[array1.index(min(array1))]
#     del array2[array2.index(min(array2))]
#     del array3[array3.index(min(array3))]
#     del array4[array4.index(min(array4))]
#     del array5[array5.index(min(array5))]
#     del array6[array6.index(min(array6))]
#     stat1 = sum(array1)
#     stat2 = sum(array2)
#     stat3 = sum(array3)
#     stat4 = sum(array4)
#     stat5 = sum(array5)
#     stat6 = sum(array6)
#     bonus1 = ((stat1-10)//2)
#     bonus2 = ((stat2-10)//2)
#     bonus3 = ((stat3-10)//2)
#     bonus4 = ((stat4-10)//2)
#     bonus5 = ((stat5-10)//2)
#     bonus6 = ((stat6-10)//2)
#     print("Str: " + str(stat1) + "(" + str(bonus1) + ")")
#     print("Dex: " + str(stat2) + "(" + str(bonus2) + ")")
#     print("Con: " + str(stat3) + "(" + str(bonus3) + ")")
#     print("Int: " + str(stat4) + "(" + str(bonus4) + ")")
#     print("Wis: " + str(stat5) + "(" + str(bonus5) + ")")
#     print("Cha: " + str(stat6) + "(" + str(bonus6) + ")")
    
# stats()
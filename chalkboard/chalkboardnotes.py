
#     def determine(self,rocos,bor):
#         try:
#             globals()[bor](rocos)
#         except:
#             print("Error when trying to '" + bor + "' your " + rocos)

#     def build(self,tobuild):
#         if self.tobuild == "stats":
#             build_stats()
#         elif tobuild == "race" or "class":
#             char_attribute = input("Please enter your choice of " + tobuild + ": ")
#             POTENTIAL_DICT = globals()[tobuild + "_DICT"]
#             for attribute in POTENTIAL_DICT:
#                 if char_attribute.lower() in POTENTIAL_DICT[attribute]:
#                     tobuild = attribute
#                     global tobuild
#                     break
#                 else:
#                     print("That's not a " + tobuild + " you fucking donkey. Let's try again:\n")
#                     build(self,tobuild)
#         else:
#             print("You failed at the (metaphomorical) first step. Try again.")
#             exit()

#     def randomize(self,torandomize):
#         if torandomize == "stats":
#             randomize_stats()
#         elif torandomize == "race" or "class":
#             random_seed = self.name + str(time.monotonic_ns())
#         else:
#             print("You failed at the first step. Try again.")
#             exit()
    
#     def build_stats():
#         pass

#     def randomize_stats():
#         pass

# class NonPlayerChar(Character):
#     def __init__(self,name,race,charclass,stats,merchandise):
#         self.charclass = charclass
#         self.merchandise = merchandise
#         Character.__init__(self,name,race,charclass,stats)

# class PlayerChar(Character):
#     def __init__(self,name,race,charclass,stats,background,equipment):
#         self.background = background
#         self.equipment = equipment
#         Character.__init__(self,name,race,charclass,stats)


###
# dict1 = {"xyz":"uvw"}     
# print(dict1)
# def dict_test(dict1,name1,value1):
#     dict1.update({name1:value1})

# dict_test(dict1,"abc","def")
# print(dict1)

# dict_test(dict1,"ghi","jkl")
# print(dict1)

###
# def try1(arguments=None):
#     try2(arguments)

# def try2(arguments=None):
#     if arguments >= 0:
#         print("Success!")

# try1(2)


# confirm_choice = input("Your profession is " + profession + ". Is this correct? y/n\n")
#             if util.strtobool(confirm_choice) == True:
#                 self.function_call("character","dict",{"Profession":profession})
#             else:
#                 print("Let's try this again.")
#                 self.build_profession()
#         else:
#             print("That's not an available profession. Please select from the following: ")
#             print("\n".join(self.profession_list))



# if parsed_choice[0] in ("build", "random"):
#             if len(parsed_choice) >= 3:
#                 while parsed_choice[1] in "except":
#                     regex_search = re.compile(f"{parsed_choice[1]}(.*)$").search(player_choice).group(1).split()
#                     while regex_search:
#                         for char_attribute in regex_search:
#                             exception_bor = self.exception_dict[parsed_choice[0]]
#                             function_name = f"{exception_bor}{char_attribute}"
#                             if hasattr(self,function_name):
#                                 call = getattr(self,function_name)
#                                 call()
#                                 regex_search.remove(char_attribute)
#                                 choice_list.remove(char_attribute)
#                             else:
#                                 clear()
#                                 print("That's not a valid exception. Let's try again.")
#                                 self.initial_function()
#                 else:
#                     parsed_choice.remove(parsed_choice[1])
#             else:
#                 parsed_choice = parsed_choice[0]
#                 while choice_list:
#                     choice_bor = self.choice_dict[parsed_choice]
#                     for char_attribute in choice_list:
#                         function_name = f"{choice_bor}{char_attribute}"
#                         call = getattr(self,function_name)
#                         call()
#                         choice_list.remove(char_attribute)
#         else:
#             clear()
#             print("That isn't one of the choices I gave you. Try again.")
#             self.initial_function()

list1 = ["a","b","c"]
print(list1[0])
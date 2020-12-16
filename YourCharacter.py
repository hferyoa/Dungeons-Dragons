from chargen import CreateCharacter

PLAYER_NAME = input("Please enter your real name: ")
CHARACTER_NAME = input("Please enter your character name: ")
BELPRS = ["background","equipment","level","profession","race","stats"]
BOR = ["random","build"] #add create possibility?
CC_API = CreateCharacter(PLAYER_NAME,CHARACTER_NAME)



CC_API.initial_function()
CC_API.character_attributes()
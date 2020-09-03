from chargen import CreateCharacter

PLAYER_NAME = input("Please enter your real name: ")
CHARACTER_NAME = input("Please enter your character name: ")
BELPRS = ["background","equipment","level","profession","race","stats"]
BOR = ["random","build"] #add create possibility?
CC_API = CreateCharacter(PLAYER_NAME,CHARACTER_NAME)





# CC_API.determine(PLAYER_NAME,CHARACTER_NAME,"this","test") #change this test to BOR and BPRS
CC_API.build_race()
CC_API.build_profession()
CC_API.build_stats()
print(CC_API.character_dict)
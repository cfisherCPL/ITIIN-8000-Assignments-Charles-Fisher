import random
import os
spawn_locations ={
    "0":  ["BellTower", 9515, 6970],
    "1":  ["LibraryLot", 7745, 6677],
    "2":  ["DurhamLot", 8935, 7848],
    "3":  ["WestFacLotFar", 2975, 7668],
    "4":  ["WestFacLotNear", 4335, 5688],
    "5":  ["WestGarage", 1635, 4849],
    "6":  ["MavVillage", 2405, 3529],
    "7":  ["UniversityVillage", 6145, 5089],
    "9":  ["H&KLot", 10005, 4837],
    "10": ["AlineCPACLot", 11575, 5769],
    "11": ["EppleyLot", 14457, 8077],
    "12": ["NECornerLot", 17415, 8937],
    "13": ["AshLot", 17735, 6207],
    "14": ["EastGarage", 16705, 5327],
    "15": ["BioMechLot", 13293, 2619],
}

rand_int = random.randint(0,8)
# print(spawn_locations)
print(rand_int)
print(spawn_locations.get(str(rand_int))[1])
print(spawn_locations.get(str(rand_int))[2])
print(os.getcwd())
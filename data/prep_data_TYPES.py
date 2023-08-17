# This code prepares the json data file for TYPES
# TYPES represent the different item/gear types in the Epic Seven game
# There are 6 different types of items: Weapon, Helm, Armor, Necklace, Ring, and Boots
# The mainstat key holds the id's of allowed stats (stored in STATS.json)
# The substat key holds the id's of the allowed stats (stored in STATS.json)
# Codes: 0 ATK, 1 ATK%, 2 HP, 3 HP%, 4 DEF, 5 DEF%, 6 CRIT, 7 CDMG, 8 EFF,
# 9 ER, 10 Speed

import json

TYPES = {
    'weapon': {
        'mainstat': [0],
        'substat': [1, 2, 3, 6, 7, 8, 9, 10]
    },
    'helm': {
        'mainstat': [2],
        'substat': [0, 1, 3, 4, 5, 6,  7, 8, 9, 10]
    },
    'armor': {
        'mainstat': [4],
        'substat': [2, 3, 5, 6, 7, 8, 9, 10]
    },
    'necklace': {
        'mainstat': [0, 1, 2, 3, 4, 5, 6, 7],
        'substat': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    },
    'ring': {
        'mainstat': [0, 1, 2, 3, 4, 5, 8, 9],
        'substat': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    },
    'boots': {
        'mainstat': [0, 1, 2, 3, 4, 5, 10],
        'substat': [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    }
}

# Save the data to a JSON file
with open('types.json', 'w') as json_file:
    json.dump(TYPES, json_file, indent=4)
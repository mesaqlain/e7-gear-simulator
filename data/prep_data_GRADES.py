# This code prepares the json data file for GRADES
# GRADES represent the different grades of items that can be acquired in Epic Seven
# There are 5 different types of grades: Normal, Good, Rare, Heroic, and Epic
# The starting_substats key specifies how many substats this grade of item starts with
# The max_substats key specifies the max number of substats this grade of item may hold
# The weight key is the probability rate of acquiring a certain grade of item (set
# to values found in crafting section in the game)

import json

GRADES = {
    'normal': {
        'starting_substats': 0,
        'max_substats': 4,
        'weight': 0
    },
    'good': {
        'starting_substats': 1,
        'max_substats': 4,
        'weight': 0
    },
    'rare': {
        'starting_substats': 2,
        'max_substats': 4,
        'weight': 0.35
    },
    'heroic': {
        'starting_substats': 3,
        'max_substats': 4,
        'weight': 0.53
    },
    'epic': {
        'starting_substats': 4,
        'max_substats': 4,
        'weight': 0.12
    }
}

# Save the data to a JSON file
with open('grades.json', 'w') as json_file:
    json.dump(GRADES, json_file, indent=4)
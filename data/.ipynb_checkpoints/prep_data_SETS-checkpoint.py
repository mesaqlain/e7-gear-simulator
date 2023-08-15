# This code prepares the json data file for SETS
# SETS represent the different sets an item belongs to in the Epic Seven game
# The text key holds a description of the set
# The items_req key holds how many items of this set are required to activate its effect
# The key_stat key holds the stat value that is modified on a Hero
# The value key specifies the value by which the key_stat is modified
# There are many different sets as show below. The number in parentheses
# show how many items of that set are required to be equipped by a hero to
# activate its effects
# Health – Gives +15% health (2 pieces)
# Defense – Gives +15% defense (2 pieces)
# Attack – Gives +35% attack (4 pieces)
# Speed – Gives 25% speed (4 pieces)
# Critical – Gives +12% critical rate (2 pieces)
# Hit Rate – Gives +20% effectiveness(2 pieces)
# Destruction – Gives +40% critical damage (4 pieces)
# Lifesteal – Gives +20% lifesteal of the damage dealt to enemies (4 pieces)
# Counter – Gives +20 chance to counter attack when attacked. (4 pieces)
# Resist – Gives +20% effect resistance(2 pieces)
# Unity – Gives +4% chance to trigger dual attack (2 pieces)
# Rage – Gives +30% damage when the enemy is debuffed (4 pieces)
# Immunity – Gives 1 turn immunity buff at the start of each battle phase
# (2 pieces)
# TO-DO
# Add the later sets

import json

SETS = {
    'Health': {
        'text': 'Health – Gives +15% health (2 pieces)',
        'items_req': 2,
        'key_stat': 'health_percent',
        'value': 15
    },
    'Defense': {
        'text': 'Defense – Gives +15% defense (2 pieces)',
        'items_req': 2,
        'key_stat': 'def_percent',
        'value': 15
    },
    'Speed': {
        'text': 'Speed – Gives 25% speed (4 pieces)',
        'items_req': 4,
        'key_stat': 'speed_percent',
        'value': 25
    },
    'Attack': {
        'text': 'Attack – Gives +35% attack (4 pieces)',
        'items_req': 4,
        'key_stat': 'atk_percent',
        'value': 35
    },
    'Critical': {
        'text': 'Gives +12% critical rate (2 pieces)',
        'items_req': 2,
        'key_stat': 'crit_rate',
        'value': 12
    },
    'Hit': {
        'text': 'Gives +20% effectiveness(2 pieces)',
        'items_req': 2,
        'key_stat': 'effectiveness',
        'value': 20
    },
    'Destruction': {
        'text': 'Gives +40% critical damage (4 pieces)',
        'items_req': 4,
        'key_stat': 'crit_Damage',
        'value': 40
    },
    'Lifesteal': {
        'text': 'Gives +20% lifesteal of the damage dealt to enemies (4 pieces)',
        'items_req': 4,
        'key_stat': 'lifesteal',
        'value': 20
    },
    'Counter': {
        'text': 'Gives +20 chance to counter attack when attacked. (4 pieces)',
        'items_req': 4,
        'key_stat': 'counter',
        'value': 20
    },
    'Resist': {
        'text': 'Gives +20% effect resistance(2 pieces)',
        'items_req': 2,
        'key_stat': 'eff_res',
        'value': 20
    },
    'Unity': {
        'text': 'Gives +4% chance to trigger dual attack (2 pieces)',
        'items_req': 2,
        'key_stat': 'dual_atk',
        'value': 4
    },
    'Rage': {
        'text': 'Gives +30% damage when the enemy is debuffed (4 pieces)',
        'items_req': 4,
        'key_stat': 'debuff_dmg',
        'value': 30
    },
    'Immunity': {
        'text': 'Gives 1 turn immunity buff at the start of each battle phase (2 pieces)',
        'items_req': 2,
        'key_stat': 'immunity',
        'value': 1
    }
}

# Save the data to a JSON file
with open('sets.json', 'w') as json_file:
    json.dump(SETS, json_file, indent=4)
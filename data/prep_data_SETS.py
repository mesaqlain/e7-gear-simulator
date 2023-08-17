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
    'health': {
        'name': 'Health Set',
        'text': 'Health – Gives +15% health (2 pieces)',
        'items_req': 2,
        'key_stat': 'health_percent',
        'value': 15,
        'hunt': 'golem'
    },
    'defense': {
        'name': 'Defense Set',
        'text': 'Defense – Gives +15% defense (2 pieces)',
        'items_req': 2,
        'key_stat': 'def_percent',
        'value': 15,
        'hunt': 'golem'
    },
    'speed': {
        'name': 'Speed Set',
        'text': 'Speed – Gives 25% speed (4 pieces)',
        'items_req': 4,
        'key_stat': 'speed_percent',
        'value': 25,
        'hunt': 'wyvern'
    },
    'attack': {
        'name': 'Attack Set',
        'text': 'Attack – Gives +35% attack (4 pieces)',
        'items_req': 4,
        'key_stat': 'atk_percent',
        'value': 35,
        'hunt': 'golem'
    },
    'critical': {
        'name': 'Critical Set',
        'text': 'Gives +12% critical rate (2 pieces)',
        'items_req': 2,
        'key_stat': 'crit_rate',
        'value': 12,
        'hunt': 'wyvern'
    },
    'hit': {
        'name': 'Hit Set',
        'text': 'Gives +20% effectiveness(2 pieces)',
        'items_req': 2,
        'key_stat': 'effectiveness',
        'value': 20,
        'hunt': 'wyvern'
    },
    'destruction': {
        'name': 'Destruction Set',
        'text': 'Gives +40% critical damage (4 pieces)',
        'items_req': 4,
        'key_stat': 'crit_Damage',
        'value': 40,
        'hunt': 'banshee'
    },
    'lifesteal': {
        'name': 'Lifesteal Set',
        'text': 'Gives +20% lifesteal of the damage dealt to enemies (4 pieces)',
        'items_req': 4,
        'key_stat': 'lifesteal',
        'value': 20,
        'hunt': 'banshee'
    },
    'counter': {
        'name': 'Counter Set',
        'text': 'Gives +20 chance to counter attack when attacked. (4 pieces)',
        'items_req': 4,
        'key_stat': 'counter',
        'value': 20,
        'hunt': 'banshee'
    },
    'resist': {
        'name': 'Resist Set',
        'text': 'Gives +20% effect resistance(2 pieces)',
        'items_req': 2,
        'key_stat': 'eff_res',
        'value': 20,
        'hunt': 'banshee'
    },
    'unity': {
        'name': 'Unity Set',
        'text': 'Gives +4% chance to trigger dual attack (2 pieces)',
        'items_req': 2,
        'key_stat': 'dual_atk',
        'value': 4,
        'hunt': 'azimanak'
    },
    'rage': {
        'name': 'Rage Set',
        'text': 'Gives +30% damage when the enemy is debuffed (4 pieces)',
        'items_req': 4,
        'key_stat': 'debuff_dmg',
        'value': 30,
        'hunt': 'azimanak'
    },
    'immunity': {
        'name': 'Immunity Set',
        'text': 'Gives 1 turn immunity buff at the start of each battle phase (2 pieces)',
        'items_req': 2,
        'key_stat': 'immunity',
        'value': 1,
        'hunt': 'azimanak'
    },
    'protection': {
        'name': 'Protection Set',
        'text': 'Gives 2 turns 12% barrier buff at the start of each battle phase (4 pieces) to all allies',
        'items_req': 4,
        'key_stat': 'barrier',
        'value': 12,
        'hunt': 'golem'
    },
    'revenge': {
        'name': 'Revenge Set',
        'text': 'Gives +12% speed and an additional 0.5% speed for every 1% hp missing',
        'items_req': 4,
        'key_stat': 'speed',
        'value': [12, 0.5],
        'hunt': 'caides'
    },
    'injury': {
        'name': 'Injury Set',
        'text': 'Decreases max health of target by up to 6% (12% for single attack)',
        'items_req': 4,
        'key_stat': 'max_health',
        'value': [6, 12],
        'hunt': 'caides'
    },
    'penetration': {
        'name': 'Penetration Set',
        'text': 'Penetrates defense of target by 15%',
        'items_req': 2,
        'key_stat': 'penetration',
        'value': 15,
        'hunt': 'caides'
    },
    'torrent': {
        'name': 'Torrent Set',
        'text': 'Decreases health by 10%, increases damage by 10%',
        'items_req': 2,
        'key_stat': ['health', 'damage'],
        'value': [10, 10],
        'hunt': 'caides'
    },
}

# Save the data to a JSON file
with open('sets.json', 'w') as json_file:
    json.dump(SETS, json_file, indent=4)
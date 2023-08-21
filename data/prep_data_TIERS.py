# This code prepares the json data file for TIERS
# TIERS represent the different Tiers of gear that can be acquired in Epic Seven
# The Tier of a gear depends on the gear level, which is specified in the level_range key
# The gear_tier specifies the tier a gear belongs to for that level_range
# Notice that the tiers go from 5 to 7, this is because we don't have data
# on what tier a gear belongs to below level 58

import json

TIERS = {
    'tier 5': {
        'gear_tier': 5,
        'level_range': list(range(58, 72))
    },
    'tier 6': {
        'gear_tier': 6,
        'level_range': list(range(72, 86))
    },
    'tier 7': {
        'gear_tier': 7,
        'level_range': list(range(86, 100))
    }
}

# Save the data to a JSON file
with open('tiers.json', 'w') as json_file:
    json.dump(TIERS, json_file, indent=4)
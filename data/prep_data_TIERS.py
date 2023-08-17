# This code prepares the json data file for TIERS
# TIERS represent the different Tiers of items that can be acquired in Epic Seven
# The Tier of an item depends on the item level, which is specified in the level_range key
# The item_tier specifies the tier an item belongs to for that level_range
# Notice that the tiers go from 5 to 7, this is because we don't have data
# on what tier an item belongs to below level 58

import json

TIERS = {
    'tier 5': {
        'item_tier': 5,
        'level_range': list(range(58, 72))
    },
    'tier 6': {
        'item_tier': 6,
        'level_range': list(range(72, 86))
    },
    'tier 7': {
        'item_tier': 7,
        'level_range': list(range(86, 100))
    }
}

# Save the data to a JSON file
with open('tiers.json', 'w') as json_file:
    json.dump(TIERS, json_file, indent=4)
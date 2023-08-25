# This code prepares the json data file for STATS
# STATS represent the different stats that can appear on an item either as mainstat or substat
# There are 11 different stats currently: 0 ATK, 1 ATK%, 2 HP, 3 HP%, 4 DEF, 5 DEF%, 6 CRIT, 7 CDMG, 8 EFF, 9 ER, 10 Speed, 11 Speed%
# The 'id' key is used for identifying a particular stat as shown in the line above
# The 'text' key is used to describe the stats, where <A> and <B> are keys that are replaced with values when printing an item
# The 'gscore' key is the multiplier which is used for gear score calculation
# The 'reforge' key has two sub keys: # mainstat key specifies the reforged value of the stat if it is a mainstat, whereas the substat key specifies the
# value by which a stat is increased upon reforge depending on the number
# of times the stat has rolled. The length of substat key is 6, with each
# index referring to the number of rolls.
# The 'mod_vals' key has two subkey -  greater and lesser
# They have the values for item modification rolls. The first index of each list is for items lower than level 89
# And the second index is for items of level 90.
# 'vars' key contains the keys 'mainstat' and 'substat'.
# Each of these have 'key', 'type', and 'values'. 'substat' also has rates
# 'key' is the key which is replaced in the text. 'type' checks whether the value to use/parse is fixed or random
# 'values' contain the values for the different item grades. Each item grade in turn contains a list which
# has values for each item tier.
# 'rates' contains the probability values for each of the corresponding stat values.
# An additional key 'modded' is constructed, which stores how much to
# increase values by when a modded item is reforged.
# Reference values from:
# https://page.onstove.com/epicseven/global/view/7902683 
# https://discord.com/channels/595385354908073984/1014748448093917265

import json
import pandas as pd

# TIERS: T4 (LV 45-57), T5 (LV 58-71), T6 (LV 72-85), T7 (LV 88+) {These
# are showin in values under vars}

# Do not have roll ranges for T4 and T5 items

# Define some rates that will be used multiple times:
# These are mainstat values for ATK%, DEF%, HP%, EFF, and ER at Tiers 4,
# 5, 6, and 7
mainstat_vals = [10, 12, 13]
flat_atk_vals = [88, 100, 103]
flat_hp_vals = [472, 540, 553]
flat_def_vals = [52, 60, 62]
crit_vals = [9, 11, 12]  # Mainstat values for CRIT
cdmg_vals = [11, 13, 14]  # Mainstat values for CDMG
spd_vals = [8, 8, 9]

# VARIABLE NAMING EXAMPLES:
# flat_atk_r5 - first part is stat name, the 'r' stands for 'rare', 5 stands for tier, rt stands for rate
# flat_atk_h6_rt - first part is stat name, the 'h' stands for 'heroic', 6
# stands for tier, rt stands for rate

# ATK%, HP%, DEF%, EFF%, ER% for Tier 5
percent_stat_r5 = [4, 5, 5, 6]
percent_stat_h5 = [4, 5, 6, 7]
percent_stat_e5 = percent_stat_h5
percent_stat_r5_rt = [0.25, 0.25, 0.25, 0.25]  # Same for all Tier 5
percent_stat_h5_rt = percent_stat_r5_rt
percent_stat_e5_rt = percent_stat_r5_rt

# ATK%, HP%, DEF%, EFF%, ER% for Tier 6
percent_stat_r6 = [4, 5, 5, 6, 7]
percent_stat_h6 = [4, 5, 6, 7, 8]
percent_stat_e6 = percent_stat_h6
percent_stat_r6_rt = [0.20] * 5
percent_stat_h6_rt = percent_stat_r6_rt
percent_stat_e6_rt = percent_stat_r6_rt

# ATK%, HP%, DEF%, EFF%, ER% for Tier 7
percent_stat_r7 = [5, 5, 6, 7, 8]
percent_stat_h7 = [5, 6, 7, 8, 9]
percent_stat_e7 = percent_stat_h7
percent_stat_r7_rt = [0.20] * 5
percent_stat_h7_rt = percent_stat_r7_rt
percent_stat_e7_rt = percent_stat_r7_rt


# FLAT ATK
flat_atk_r5 = list(range(25, 37))
flat_atk_h5 = list(range(27, 39))
flat_atk_e5 = list(range(28, 41))
flat_atk_r5_rt = [0.03944] + [0.09527]*(len(flat_atk_r5) - 2) + [0.00781]
flat_atk_h5_rt = [0.08955] + [0.09027]*(len(flat_atk_h5) - 2) + [0.00776]
flat_atk_e5_rt = [0.04889] + [0.08576]*(len(flat_atk_e5) - 2) + [0.00772]

flat_atk_r6 = list(range(29, 43))
flat_atk_h6 = list(range(31, 45))
flat_atk_e6 = list(range(33, 47))
flat_atk_r6_rt = [0.01145] + [0.08177]*(len(flat_atk_r6) - 2) + [0.00736]
flat_atk_h6_rt = [0.03718] + [0.07746]*(len(flat_atk_h6) - 2) + [0.03331]
flat_atk_e6_rt = [0.06103] + [0.07353]*(len(flat_atk_e6) - 2) + [0.05662]

flat_atk_r7 = list(range(34, 49))
flat_atk_h7 = list(range(36, 51))
flat_atk_e7 = list(range(37, 54))
flat_atk_r7_rt = [0.06305] + [0.07149]*(len(flat_atk_r7) - 2) + [0.00758]
flat_atk_h7_rt = [0.06678] + [0.06773]*(len(flat_atk_h7) - 2) + [0.05270]
flat_atk_e7_rt = [0.00579] + [0.06435]*(len(flat_atk_e7) - 2) + [0.02896]


# FLAT HP
flat_hp_r5 = list(range(122, 158))
flat_hp_h5 = list(range(129, 167))
flat_hp_e5 = list(range(136, 176))
flat_hp_r5_rt = [0.00456] + [0.02847]*(len(flat_hp_r5) - 2) + [0.02733]
flat_hp_h5_rt = [0.00914] + [0.02698]*(len(flat_hp_h5) - 2) + [0.01983]
flat_hp_e5_rt = [0.01307] + [0.02563]*(len(flat_hp_e5) - 2) + [0.01307]

flat_hp_r6 = list(range(141, 183))
flat_hp_h6 = list(range(149, 193))
flat_hp_e6 = list(range(157, 203))
flat_hp_r6_rt = [0.00642] + [0.02468]*(len(flat_hp_r6) - 2) + [0.00642]
flat_hp_h6_rt = [0.00889] + [0.02339]*(len(flat_hp_h6) - 2) + [0.00889]
flat_hp_e6_rt = [0.01133] + [0.02221]*(len(flat_hp_e6) - 2) + [0.01133]

flat_hp_r7 = list(range(160, 207))
flat_hp_h7 = list(range(169, 219))
flat_hp_e7 = list(range(178, 230))
flat_hp_r7_rt = [0.00784] + [0.02178]*(len(flat_hp_r7) - 2) + [0.01220]
flat_hp_h7_rt = [0.00887] + [0.02064]*(len(flat_hp_h7) - 2) + [0.00062]
flat_hp_e7_rt = [0.01000] + [0.01960]*(len(flat_hp_e7) - 2) + [0.01000]


# FLAT DEF
flat_def_r5 = list(range(21, 28))
flat_def_h5 = list(range(22, 29))
flat_def_e5 = list(range(24, 31))
flat_def_r5_rt = [0.07565] + [0.18450]*(len(flat_def_r5) - 2) + [0.00185]
flat_def_h5_rt = [0.03671] + [0.17483]*(len(flat_def_h5) - 2) + [0.08916]
flat_def_e5_rt = [0.16639]*(len(flat_def_e5) - 1) + [0.00166]

flat_def_r6 = list(range(25, 32))
flat_def_h6 = list(range(26, 34))
flat_def_e6 = list(range(28, 36))
flat_def_r6_rt = [0.12816] + [0.15823]*(len(flat_def_r6) - 2) + [0.08070]
flat_def_h6_rt = [0.06147] + [0.14993]*(len(flat_def_h6) - 2) + [0.03898]
flat_def_e6_rt = [0.14265]*(len(flat_def_e6) - 1) + [0.00143]

flat_def_r7 = list(range(28, 37))
flat_def_h7 = list(range(30, 39))
flat_def_e7 = list(range(32, 41))
flat_def_r7_rt = [0.02909] + [0.13850]*(len(flat_def_r7) - 2) + [0.00139]
flat_def_h7_rt = [0.08005] + [0.13123]*(len(flat_def_h7) - 2) + [0.00131]
flat_def_e7_rt = [0.12484]*(len(flat_def_e7) - 1) + [0.00125]


# CRIT CHANCE
crit_r5 = [2, 3, 4]
crit_h5 = crit_r5
crit_e5 = crit_r5
crit_r5_rt = [0.33333, 0.33333, 0.33333]
crit_h5_rt = crit_r5_rt
crit_e5_rt = crit_r5_rt

crit_r6 = [3, 4, 5]
crit_h6 = crit_r6
crit_e6 = crit_r6
crit_r6_rt = [0.33333, 0.33333, 0.33333]
crit_h6_rt = crit_r6_rt
crit_e6_rt = crit_r6_rt

crit_r7 = [3, 4, 5, 5]
crit_h7 = [3, 4, 5, 6]
crit_e7 = crit_h7
crit_r7_rt = [0.25] * 4
crit_h7_rt = crit_r7_rt
crit_e7_rt = crit_r7_rt


# CRIT DAMAGE
cdmg_r5 = [3, 4, 5, 5]
cdmg_h5 = [3, 4, 5, 6]
cdmg_e5 = cdmg_h5
cdmg_r5_rt = [0.25] * 4
cdmg_h5_rt = cdmg_r5_rt
cdmg_e5_rt = cdmg_r5_rt

cdmg_r6 = [4, 5, 5, 6]
cdmg_h6 = [4, 5, 6, 7]
cdmg_e6 = cdmg_h6
cdmg_r6_rt = [0.25] * 4
cdmg_h6_rt = cdmg_r6_rt
cdmg_e6_rt = cdmg_r6_rt

cdmg_r7 = [4, 5, 5, 6, 7]
cdmg_h7 = [4, 5, 6, 7, 8]
cdmg_e7 = cdmg_h7
cdmg_r7_rt = [0.20] * 5
cdmg_h7_rt = cdmg_r7_rt
cdmg_e7_rt = cdmg_r7_rt


# SPEED
spd_r5 = [1, 2, 3]
spd_h5 = [1, 2, 3]
spd_e5 = [2, 3, 4]
spd_r5_rt = [0.11538, 0.54945, 0.33516]
spd_h5_rt = [0.05729, 0.52083, 0.42188]
spd_e5_rt = [0.49751, 0.49751, 0.00498]

spd_r6 = [1, 2, 3, 4]
spd_h6 = spd_r6
spd_e6 = [2, 3, 4, 5]
spd_r6_rt = [0.07721, 0.36765, 0.36765, 0.18750]
spd_h6_rt = [0.03833, 0.34843, 0.34843, 0.26481]
spd_e6_rt = [0.33223, 0.33223, 0.33223, 0.00332]

spd_r7 = [2, 3, 4]
spd_h7 = spd_r7
spd_e7 = [3, 4, 5]
spd_r7_rt = [0.17033, 0.54945, 0.28022]
spd_h7_rt = [0.08333, 0.52083, 0.39583]
spd_e7_rt = [0.49751, 0.49751, 0.00498]


# REFORGE VALUES:
rf_pct = [1, 3, 4, 5, 7, 8]
rf_crit = [1, 2, 3, 4, 5, 6]
rf_cdmg = [1, 2, 3, 4, 6, 7]
rf_spd = [0, 1, 2, 3, 4, 4]
rf_flat_atk = [11, 22, 33, 44, 55, 66]
rf_flat_def = [9, 18, 27, 36, 45, 54]
rf_flat_hp = [56, 112, 168, 224, 280, 336]


# MOD VALUES
flat_atk_greater_88 = [
    list(range(
        33, 48)), list(range(
            50, 78)), list(range(
                68, 102)), list(range(
                    79, 110)), list(range(
                        94, 130)), list(range(
                            128, 152))]
flat_atk_greater_90 = [
    list(range(
        44, 59)), list(range(
            72, 100)), list(range(
                101, 135)), list(range(
                    123, 154)), list(range(
                        149, 185)), list(range(
                            194, 218))]
flat_atk_lesser_88 = [
    list(range(
        28, 41)), list(range(
            42, 66)), list(range(
                58, 87)), list(range(
                    67, 94)), list(range(
                        80, 111)), list(range(
                            109, 129))]
flat_atk_lesser_90 = [
    list(range(
        39, 52)), list(range(
            64, 88)), list(range(
                91, 120)), list(range(
                    111, 138)), list(range(
                        135, 166)), list(range(
                            175, 195))]

flat_def_greater_88 = [
    list(range(
        28, 36)), list(range(
            32, 62)), list(range(
                51, 77)), list(range(
                    60, 81)), list(range(
                        73, 98)), list(range(
                            94, 112))]
flat_def_greater_90 = [
    list(range(
        37, 45)), list(range(
            50, 80)), list(range(
                78, 104)), list(range(
                    96, 117)), list(range(
                        118, 143)), list(range(
                            148, 166))]
flat_def_lesser_88 = [
    list(range(
        24, 31)), list(range(
            27, 53)), list(range(
                43, 66)), list(range(
                    51, 69)), list(range(
                        62, 83)), list(range(
                            80, 95))]
flat_def_lesser_90 = [
    list(range(
        33, 40)), list(range(
            45, 71)), list(range(
                70, 93)), list(range(
                    87, 105)), list(range(
                        107, 128)), list(range(
                            134, 149))]

flat_hp_greater_88 = [
    list(range(
        158, 204)), list(range(
            235, 337)), list(range(
                322, 423)), list(range(
                    378, 462)), list(range(
                        435, 579)), list(range(
                            561, 660))]
flat_hp_greater_90 = [
    list(range(
        214, 260)), list(range(
            347, 449)), list(range(
                490, 591)), list(range(
                    602, 686)), list(range(
                        715, 859)), list(range(
                            897, 996))]
flat_hp_lesser_88 = [
    list(range(
        134, 173)), list(range(
            200, 286)), list(range(
                274, 360)), list(range(
                    321, 393)), list(range(
                        370, 492)), list(range(
                            477, 561))]
flat_hp_lesser_90 = [
    list(range(
        190, 229)), list(range(
            312, 398)), list(range(
                442, 528)), list(range(
                    545, 617)), list(range(
                        650, 772)), list(range(
                            813, 897))]

percent_stats_greater_88 = [
    list(range(
        4, 9)), list(range(
            7, 12)), list(range(
                10, 15)), list(range(
                    13, 18)), list(range(
                        15, 19)), list(range(
                            16, 20))]
percent_stats_greater_90 = [
    list(range(
        5, 10)), list(range(
            10, 15)), list(range(
                14, 19)), list(range(
                    18, 23)), list(range(
                        22, 26)), list(range(
                            24, 28))]
percent_stats_lesser_88 = [
    list(range(
        3, 6)), list(range(
            5, 9)), list(range(
                8, 12)), list(range(
                    11, 15)), list(range(
                        13, 16)), list(range(
                            14, 17))]
percent_stats_lesser_90 = [
    list(range(
        4, 7)), list(range(
            8, 12)), list(range(
                12, 16)), list(range(
                    16, 20)), list(range(
                        20, 23)), list(range(
                            22, 25))]

crit_greater_88 = [
    list(range(
        2, 5)), list(range(
            3, 7)), list(range(
                5, 9)), list(range(
                    7, 11)), list(range(
                        9, 12)), list(range(
                            10, 13))]
crit_greater_90 = [
    list(range(
        3, 6)), list(range(
            5, 9)), list(range(
                8, 12)), list(range(
                    11, 15)), list(range(
                        14, 17)), list(range(
                            16, 19))]
crit_lesser_88 = [
    list(range(
        2, 4)), list(range(
            2, 5)), list(range(
                3, 6)), list(range(
                    4, 8)), list(range(
                        6, 9)), list(range(
                            7, 10))]
crit_lesser_90 = [
    list(range(
        3, 5)), list(range(
            4, 7)), list(range(
                6, 9)), list(range(
                    8, 12)), list(range(
                        11, 14)), list(range(
                            13, 16))]

cdmg_greater_88 = [
    list(range(
        4, 8)), list(range(
            6, 10)), list(range(
                8, 13)), list(range(
                    11, 16)), list(range(
                        13, 17)), list(range(
                            14, 18))]
cdmg_greater_90 = [
    list(range(
        5, 9)), list(range(
            8, 12)), list(range(
                11, 16)), list(range(
                    15, 20)), list(range(
                        19, 23)), list(range(
                            21, 25))]
cdmg_lesser_88 = [
    list(range(
        3, 5)), list(range(
            4, 7)), list(range(
                6, 10)), list(range(
                    9, 13)), list(range(
                        11, 14)), list(range(
                            12, 15))]
cdmg_lesser_90 = [
    list(range(
        4, 6)), list(range(
            6, 9)), list(range(
                9, 13)), list(range(
                    13, 17)), list(range(
                        17, 20)), list(range(
                            19, 22))]

spd_greater_88 = [
    list(range(
        2, 5)), list(range(
            3, 6)), list(range(
                4, 7)), list(range(
                    5, 9)), list(range(
                        6, 10)), list(range(
                            7, 11))]
spd_greater_90 = [
    list(range(
        2, 5)), list(range(
            4, 7)), list(range(
                6, 9)), list(range(
                    8, 12)), list(range(
                        10, 14)), list(range(
                            11, 15))]
spd_lesser_88 = [
    list(range(
        2, 4)), list(range(
            2, 5)), list(range(
                3, 6)), list(range(
                    4, 7)), list(range(
                        5, 8)), list(range(
                            6, 9))]
spd_lesser_90 = [
    list(range(
        2, 4)), list(range(
            3, 6)), list(range(
                5, 8)), list(range(
                    7, 10)), list(range(
                        9, 12)), list(range(
                            10, 13))]


STATS = {
    '0': {
        'id': 0,
        'text': '<A> <B>Attack',
        'key_stat': 'attack_flat',
        'gscore': (3.46 / 39),
        'reforge': {'mainstat': [525], 'substat': rf_flat_atk},
        'vars': {
                'mainstat': {'key': '<A>', 'type': 'fixed', 'values': {
                    'rare': flat_atk_vals,
                    'heroic': flat_atk_vals,
                    'epic': flat_atk_vals
                },
                },
            'substat': {'key': '<A>', 'type': 'rand', 'values': {
                'rare': [flat_atk_r5, flat_atk_r6, flat_atk_r7],
                'heroic': [flat_atk_h5, flat_atk_h6, flat_atk_h7],
                'epic': [flat_atk_e5, flat_atk_e6, flat_atk_e7]
            },
                    'rates': {
                    'rare': [flat_atk_r5_rt, flat_atk_r6_rt, flat_atk_r7_rt],
                    'heroic': [flat_atk_h5_rt, flat_atk_h6_rt, flat_atk_h7_rt],
                    'epic': [flat_atk_e5_rt, flat_atk_e6_rt, flat_atk_e7_rt]
            }
                    },
        },
        'mod_vals': {'greater': [flat_atk_greater_88, flat_atk_greater_90],
                     'lesser': [flat_atk_lesser_88, flat_atk_lesser_90]}
    },
    '1': {
        'id': 1,
        'text': '<A>% <B>Attack',
        'key_stat': 'attack_percent',
        'gscore': 1,
        'reforge': {'mainstat': [65], 'substat': rf_pct},
        'vars': {
                'mainstat': {'key': '<A>', 'type': 'fixed', 'values': {
                    'rare': mainstat_vals,
                    'heroic': mainstat_vals,
                    'epic': mainstat_vals
                },
                },
            'substat': {'key': '<A>', 'type': 'rand', 'values': {
                'rare': [percent_stat_r5, percent_stat_r6, percent_stat_r7],
                'heroic': [percent_stat_h5, percent_stat_h6, percent_stat_h7],
                'epic': [percent_stat_e5, percent_stat_e6, percent_stat_e7]
            },
                    'rates': {
                    'rare': [percent_stat_r5_rt, percent_stat_r6_rt, percent_stat_r7_rt],
                    'heroic': [percent_stat_h5_rt, percent_stat_h6_rt, percent_stat_h7_rt],
                    'epic': [percent_stat_e5_rt, percent_stat_e6_rt, percent_stat_e7_rt]
            }
                    },
        },
        'mod_vals': {'greater': [percent_stats_greater_88, percent_stats_greater_90],
                     'lesser': [percent_stats_lesser_88, percent_stats_lesser_90]}
    },
    '2': {
        'id': 2,
        'text': '<A> <B>Health',
        'key_stat': 'health_flat',
        'gscore': (3.09 / 174),
        'reforge': {'mainstat': [2835], 'substat': rf_flat_hp},
        'vars': {
                'mainstat': {'key': '<A>', 'type': 'fixed', 'values': {
                    'rare': flat_hp_vals,
                    'heroic': flat_hp_vals,
                    'epic': flat_hp_vals
                },
                },
            'substat': {'key': '<A>', 'type': 'rand', 'values': {
                'rare': [flat_hp_r5, flat_hp_r6, flat_hp_r7],
                'heroic': [flat_hp_h5, flat_hp_h6, flat_hp_h7],
                'epic': [flat_hp_e5, flat_hp_e6, flat_hp_e7]
            },
                    'rates': {
                    'rare': [flat_hp_r5_rt, flat_hp_r6_rt, flat_hp_r7_rt],
                    'heroic': [flat_hp_h5_rt, flat_hp_h6_rt, flat_hp_h7_rt],
                    'epic': [flat_hp_e5_rt, flat_hp_e6_rt, flat_hp_e7_rt]
            }
                    },
        },
        'mod_vals': {'greater': [flat_hp_greater_88, flat_hp_greater_90],
                     'lesser': [flat_hp_lesser_88, flat_hp_lesser_90]}
    },
    '3': {
        'id': 3,
        'text': '<A>% <B>Health',
        'key_stat': 'health_percent',
        'gscore': 1,
        'reforge': {'mainstat': [65], 'substat': rf_pct},
        'vars': {
                'mainstat': {'key': '<A>', 'type': 'fixed', 'values': {
                    'rare': mainstat_vals,
                    'heroic': mainstat_vals,
                    'epic': mainstat_vals
                },
                },
            'substat': {'key': '<A>', 'type': 'rand', 'values': {
                'rare': [percent_stat_r5, percent_stat_r6, percent_stat_r7],
                'heroic': [percent_stat_h5, percent_stat_h6, percent_stat_h7],
                'epic': [percent_stat_e5, percent_stat_e6, percent_stat_e7]
            },
                    'rates': {
                    'rare': [percent_stat_r5_rt, percent_stat_r6_rt, percent_stat_r7_rt],
                    'heroic': [percent_stat_h5_rt, percent_stat_h6_rt, percent_stat_h7_rt],
                    'epic': [percent_stat_e5_rt, percent_stat_e6_rt, percent_stat_e7_rt]
            }
                    },
        },
        'mod_vals': {'greater': [percent_stats_greater_88, percent_stats_greater_90],
                     'lesser': [percent_stats_lesser_88, percent_stats_lesser_90]}
    },
    '4': {
        'id': 4,
        'text': '<A> <B>Defense',
        'key_stat': 'defense_flat',
        'gscore': (4.99 / 31),
        'reforge': {'mainstat': [310], 'substat': rf_flat_def},
        'vars': {
                'mainstat': {'key': '<A>', 'type': 'fixed', 'values': {
                    'rare': flat_def_vals,
                    'heroic': flat_def_vals,
                    'epic': flat_def_vals
                },
                },
            'substat': {'key': '<A>', 'type': 'rand', 'values': {
                'rare': [flat_def_r5, flat_def_r6, flat_def_r7],
                'heroic': [flat_def_h5, flat_def_h6, flat_def_h7],
                'epic': [flat_def_e5, flat_def_e6, flat_def_e7]
            },
                    'rates': {
                    'rare': [flat_def_r5_rt, flat_def_r6_rt, flat_def_r7_rt],
                    'heroic': [flat_def_h5_rt, flat_def_h6_rt, flat_def_h7_rt],
                    'epic': [flat_def_e5_rt, flat_def_e6_rt, flat_def_e7_rt]
            }
                    },
        },
        'mod_vals': {'greater': [flat_def_greater_88, flat_def_greater_90],
                     'lesser': [flat_def_lesser_88, flat_def_lesser_90]}
    },
    '5': {
        'id': 5,
        'text': '<A>% <B>Defense',
        'key_stat': 'defense_percent',
        'gscore': 1,
        'reforge': {'mainstat': [65], 'substat': rf_pct},
        'vars': {
                'mainstat': {'key': '<A>', 'type': 'fixed', 'values': {
                    'rare': mainstat_vals,
                    'heroic': mainstat_vals,
                    'epic': mainstat_vals
                },
                },
            'substat': {'key': '<A>', 'type': 'rand', 'values': {
                'rare': [percent_stat_r5, percent_stat_r6, percent_stat_r7],
                'heroic': [percent_stat_h5, percent_stat_h6, percent_stat_h7],
                'epic': [percent_stat_e5, percent_stat_e6, percent_stat_e7]
            },
                    'rates': {
                    'rare': [percent_stat_r5_rt, percent_stat_r6_rt, percent_stat_r7_rt],
                    'heroic': [percent_stat_h5_rt, percent_stat_h6_rt, percent_stat_h7_rt],
                    'epic': [percent_stat_e5_rt, percent_stat_e6_rt, percent_stat_e7_rt]
            }
                    },
        },
        'mod_vals': {'greater': [percent_stats_greater_88, percent_stats_greater_90],
                     'lesser': [percent_stats_lesser_88, percent_stats_lesser_90]}
    },
    '6': {
        'id': 6,
        'text': '<A>% <B>Crit Chance',
        'key_stat': 'crit_rate',
        'gscore': (8/5),
        'reforge': {'mainstat': [60], 'substat': rf_crit},
        'vars': {
                'mainstat': {'key': '<A>', 'type': 'fixed', 'values': {
                    'rare': crit_vals,
                    'heroic': crit_vals,
                    'epic': crit_vals
                },
                },
            'substat': {'key': '<A>', 'type': 'rand', 'values': {
                'rare': [crit_r5, crit_r6, crit_r7],
                'heroic': [crit_h5, crit_h6, crit_h7],
                'epic': [crit_e5, crit_e6, crit_e7]
            },
                    'rates': {
                    'rare': [crit_r5_rt, crit_r6_rt, crit_r7_rt],
                    'heroic': [crit_h5_rt, crit_h6_rt, crit_h7_rt],
                    'epic': [crit_e5_rt, crit_e6_rt, crit_e7_rt]
            }
                    },
        },
        'mod_vals': {'greater': [crit_greater_88, crit_greater_90],
                     'lesser': [crit_lesser_88, crit_lesser_90]}
    },
    '7': {
        'id': 7,
        'text': '<A>% <B>Crit Damage',
        'key_stat': 'crit_damage',
        'gscore': (8/7),
        'reforge': {'mainstat': [70], 'substat': rf_cdmg},
        'vars': {
                'mainstat': {'key': '<A>', 'type': 'fixed', 'values': {
                    'rare': cdmg_vals,
                    'heroic': cdmg_vals,
                    'epic': cdmg_vals
                },
                },
            'substat': {'key': '<A>', 'type': 'rand', 'values': {
                'rare': [cdmg_r5, cdmg_r6, cdmg_r7],
                'heroic': [cdmg_h5, cdmg_h6, cdmg_h7],
                'epic': [cdmg_e5, cdmg_e6, cdmg_e7]
            },
                    'rates': {
                    'rare': [cdmg_r5_rt, cdmg_r6_rt, cdmg_r7_rt],
                    'heroic': [cdmg_h5_rt, cdmg_h6_rt, cdmg_h7_rt],
                    'epic': [cdmg_e5_rt, cdmg_e6_rt, cdmg_e7_rt]
            }
                    },
        },
        'mod_vals': {'greater': [cdmg_greater_88, cdmg_greater_90],
                     'lesser': [cdmg_lesser_88, cdmg_lesser_90]}
    },
    '8': {
        'id': 8,
        'text': '<A>% <B>Effectiveness',
        'key_stat': 'eff',
        'gscore': 1,
        'reforge': {'mainstat': [65], 'substat': rf_pct},
        'vars': {
                'mainstat': {'key': '<A>', 'type': 'fixed', 'values': {
                    'rare': mainstat_vals,
                    'heroic': mainstat_vals,
                    'epic': mainstat_vals
                },
                },
            'substat': {'key': '<A>', 'type': 'rand', 'values': {
                'rare': [percent_stat_r5, percent_stat_r6, percent_stat_r7],
                'heroic': [percent_stat_h5, percent_stat_h6, percent_stat_h7],
                'epic': [percent_stat_e5, percent_stat_e6, percent_stat_e7]
            },
                    'rates': {
                    'rare': [percent_stat_r5_rt, percent_stat_r6_rt, percent_stat_r7_rt],
                    'heroic': [percent_stat_h5_rt, percent_stat_h6_rt, percent_stat_h7_rt],
                    'epic': [percent_stat_e5_rt, percent_stat_e6_rt, percent_stat_e7_rt]
            }
                    },
        },
        'mod_vals': {'greater': [percent_stats_greater_88, percent_stats_greater_90],
                     'lesser': [percent_stats_lesser_88, percent_stats_lesser_90]}
    },
    '9': {
        'id': 9,
        'text': '<A>% <B>Effect Resistance',
        'key_stat': 'eff_res',
        'gscore': 1,
        'reforge': {'mainstat': [65], 'substat': rf_pct},
        'vars': {
                'mainstat': {'key': '<A>', 'type': 'fixed', 'values': {
                    'rare': mainstat_vals,
                    'heroic': mainstat_vals,
                    'epic': mainstat_vals
                },
                },
            'substat': {'key': '<A>', 'type': 'rand', 'values': {
                'rare': [percent_stat_r5, percent_stat_r6, percent_stat_r7],
                'heroic': [percent_stat_h5, percent_stat_h6, percent_stat_h7],
                'epic': [percent_stat_e5, percent_stat_e6, percent_stat_e7]
            },
                    'rates': {
                    'rare': [percent_stat_r5_rt, percent_stat_r6_rt, percent_stat_r7_rt],
                    'heroic': [percent_stat_h5_rt, percent_stat_h6_rt, percent_stat_h7_rt],
                    'epic': [percent_stat_e5_rt, percent_stat_e6_rt, percent_stat_e7_rt]
            }
                    },
        },
        'mod_vals': {'greater': [percent_stats_greater_88, percent_stats_greater_90],
                     'lesser': [percent_stats_lesser_88, percent_stats_lesser_90]}
    },
    '10': {
        'id': 10,
        'text': '<A> <B>Speed',
        'key_stat': 'speed_flat',
        'gscore': 2,
        'reforge': {'mainstat': [45], 'substat': rf_spd},
        'vars': {
                'mainstat': {'key': '<A>', 'type': 'fixed', 'values': {
                    'rare': spd_vals,
                    'heroic': spd_vals,
                    'epic': spd_vals
                },
                },
            'substat': {'key': '<A>', 'type': 'rand', 'values': {
                'rare': [spd_r5, spd_r6, spd_r7],
                'heroic': [spd_h5, spd_h6, spd_h7],
                'epic': [spd_e5, spd_e6, spd_e7]
            },
                    'rates': {
                    'rare': [spd_r5_rt, spd_r6_rt, spd_r7_rt],
                    'heroic': [spd_h5_rt, spd_h6_rt, spd_h7_rt],
                    'epic': [spd_e5_rt, spd_e6_rt, spd_e7_rt]
            }
                    },
        },
        'mod_vals': {'greater': [spd_greater_88, spd_greater_90],
                     'lesser': [spd_lesser_88, spd_lesser_90]}
    }
}


stats = []
rolls = []

greater_val_90 = []
greater_val_88 = []
greater_diff = []

lesser_val_90 = []
lesser_val_88 = []
lesser_diff = []

for i in range(0, len(STATS)):
    for j in range(0, 6):

        stat_name = STATS[str(i)]['key_stat']
        stats.append(stat_name)  # get stat namne
        rolls.append(j)  # get roll number

        # greater
        val_90 = STATS[str(i)]['mod_vals']['greater'][1][j][0]
        val_88 = STATS[str(i)]['mod_vals']['greater'][0][j][0]
        diff = val_90 - val_88
        greater_val_90.append(val_90)
        greater_val_88.append(val_88)
        greater_diff.append(diff)

        # lesser
        val_90 = STATS[str(i)]['mod_vals']['lesser'][1][j][0]
        val_88 = STATS[str(i)]['mod_vals']['lesser'][0][j][0]
        diff = val_90 - val_88
        lesser_val_90.append(val_90)
        lesser_val_88.append(val_88)
        lesser_diff.append(diff)


df = pd.DataFrame({'stat': stats,
                   'rolls': rolls,
                   'great 88': greater_val_88,
                   'great 90': greater_val_90,
                   'greater diff': greater_diff,
                   'less 88': lesser_val_88,
                   'less 90': lesser_val_90,
                   'lesser diff': lesser_diff})
df['diff'] = df['greater diff'] - df['lesser diff']

key_stats = df['stat'].unique()

vals_dict = {}  # Initialize an empty dictionary

for i, s in enumerate(key_stats):
    stat_name = s
    values = list(df[df['stat'] == key_stats[i]]['greater diff'])
    vals_dict[stat_name] = values

# print(vals_dict)

# Loop through the keys of the STATS dictionary
for stat_id in STATS.keys():
    stat_entry = STATS[stat_id]
    key_stat = stat_entry['key_stat']
    if key_stat in vals_dict:
        modded_values = vals_dict[key_stat]
        stat_entry['reforge']['modded'] = modded_values
        
        
# Save the data to a JSON file
with open('stats.json', 'w') as json_file:
    json.dump(STATS, json_file, indent=4)
# Tribes
REGULAR_TRIBE_NAMES =  ["Xinxi",    "Imperius", "Bardur",   "Oumaji",
                        "Kickoo",   "Hoodrick", "Luxidoor", "Vengir",
                        "Zebasi",   "Aimo",     "Quetzali", "Yadakk"]

SPECIAL_TRIBE_NAMES =  ["Aquarion", "Elyrion",  "Polaris",  "Cymanti"]

TRIBE_NAMES =  REGULAR_TRIBE_NAMES + SPECIAL_TRIBE_NAMES

# Technologies
TECHNOLOGY_NAMES = ["Riding", "FreeSpirit", "Chivalry", "Roads", "Trade",
                    "Organization", "Shields", "Farming", "Construction",
                    "Fishing", "Whaling", "Aquatism", "Sailing", "Navigation",
                    "Hunting", "Forestry", "Mathematics", "Archery", "Spiritualism",
                    "Climbing", "Meditation", "Philosophy", "Mining", "Smithery"]
TECHNOLOGY_OFFSET = 500

# Score Options
MAX_SCORE_K = 100 # Absolute max is 500

STAR_NAME_TO_SCORE = {
    "star_1": 10,
    "stars_2": 25,
    "stars_3": 50
}

def disable_tech_shuffle_for_special_tribes(tech_location: int, tech_item: int, playable_tribes: set[str]) -> bool:
    return False # Uncomment this to enable tech shuffle for special tribes.
    has_special_tribe = any(tribe in playable_tribes for tribe in SPECIAL_TRIBE_NAMES)
    return (tech_location != 0 or tech_item != 0) and has_special_tribe

def tribe_specific_id(tribe_index: int, id: int) -> int:
    return tribe_index * 1000 + id

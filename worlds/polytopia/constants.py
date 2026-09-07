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

def tribe_specific_id(tribe_index: int, id: int) -> int:
    return tribe_index * 1000 + id

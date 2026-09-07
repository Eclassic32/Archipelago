from dataclasses import dataclass

from Options import Choice, DefaultOnToggle, NamedRange, OptionGroup, OptionSet, PerGameCommonOptions, Range

from .constants import MAX_SCORE_K, REGULAR_TRIBE_NAMES, STAR_NAME_TO_SCORE, TRIBE_NAMES


# Playable Tribes
class PlayableTribes(OptionSet):
    """List of tribes that can be selected for play.
    Notice: Client mod does NOT let you select tribes that you do not own in main game.

    Possible values:
    ["Xinxi",   "Imperius", "Bardur",   "Oumaji",
    "Kickoo",   "Hoodrick", "Luxidoor", "Vengir",
    "Zebasi",   "Aimo",     "Quetzali", "Yadakk",
    "Aquarion", "Elyrion",  "Polaris",  "Cymanti"]
    """

    display_name = "Playable Tribes"
    valid_keys = TRIBE_NAMES
    default = REGULAR_TRIBE_NAMES

class FirstUnlockedTribe(Choice):
    """The first tribe that will be unlocked for the player.
    Notice: Client mod does NOT let you select tribes that you do not own in main game.

    Possible values:
    "Xinxi",    "Imperius", "Bardur",   "Oumaji", - included in any_free, any_regular
    "Kickoo",   "Hoodrick", "Luxidoor", "Vengir", - included in any_regular
    "Zebasi",   "Aimo",     "Quetzali", "Yadakk", - included in any_regular
    "Aquarion", "Elyrion",  "Polaris",  "Cymanti" - included in any_special
    "any_playable" - dynamically includes your playable tribes
    """

    display_name = "First Unlocked Tribe"
    option_any_free = -1
    option_any_regular = -2
    option_any_special = -3
    option_any_playable = -4

    option_xinxi    = 0
    option_imperius = 1
    option_bardur   = 2
    option_oumaji   = 3
    option_kickoo   = 4
    option_hoodrick = 5
    option_luxidoor = 6
    option_vengir   = 7
    option_zebasi   = 8
    option_aimo     = 9
    option_quetzali = 10
    option_yadakk   = 11
    option_aquarion = 12
    option_elyrion  = 13
    option_polaris  = 14
    option_cymanti  = 15

    default = option_any_playable

# Goal Options
class RequiredUniqueTribesWins(Range):
    """Amount of wins with unique tribes required for a player to goal the game.

    """

    display_name = "Unique Tribe Wins required for Victory "
    range_start = 1
    range_end = len(TRIBE_NAMES)
    default = 4

class RequiredScoreForVictory(NamedRange):
    """Score required for a tribe to be considered as victorious.

    Rating in the main game:
    1 star = 10k
    2 stars = 25k
    3 stars = 50k

    """

    display_name = "Score required for Tribe Victory (*1000)"
    range_start = 1
    range_end = MAX_SCORE_K
    default = 15
    special_range_names = STAR_NAME_TO_SCORE

# Score Check Options
class ShouldSendScoreChecksImmediately(DefaultOnToggle):
    """Whether to send score checks immediately or wait until the end of the match.

    True - Send score checks immediately
    False - Wait until the end of the match to send score checks
    """

    display_name = "Send Score Checks Immediately"

class ScoreChecksMin(NamedRange):
    """Minimum score*1000 for score checks.
    Setting ScoreChecksMin or ScoreChecksMax to 0 will disable score checks.

    Rating in the main game:
        1 star = 10k
        2 stars = 25k
        3 stars = 50k

    """

    display_name = "Minimum Score Checks (*1000)"
    range_start = 0
    range_end = MAX_SCORE_K
    default = 2
    special_range_names = STAR_NAME_TO_SCORE

class ScoreChecksMax(NamedRange):
    """Maximum score*1000 for score checks.
    Setting ScoreChecksMin or ScoreChecksMax to 0 will disable score checks.

    Rating in the main game:
        1 star = 10k
        2 stars = 25k
        3 stars = 50k

    """

    display_name = "Maximum Score Checks (*1000)"
    range_start = 0
    range_end = MAX_SCORE_K
    default = 20
    special_range_names = STAR_NAME_TO_SCORE

class ScoreChecksStep(Range):
    """Step size for score checks. (*1000)

    """

    display_name = "Score Checks Step Size (*1000)"
    range_start = 0
    range_end = MAX_SCORE_K
    default = 2

class ExcludeScoreChecksAfter(Range):
    """Exclude score checks after a certain score (*1000) to not have progressive items.
    **Disabled** (-1) - allows generation to place progressive items in any score check location.
    **After Victory** (0) - dynamically excludes score checks after the victory score.
    """

    display_name = "Exclude Score Checks After (*1000)"
    range_start = -1
    range_end = MAX_SCORE_K
    default = 0
    special_range_names = {
        "disable": -1,
        "after_victory": 0,
    }

# Technology Randomization Options
class TechnologyLocations(Choice):
    """Should technology locations be randomized or not.

    **Disabled** - Technology locations will not be randomized.
    **Enabled** - Technology locations will be randomized. (Adds 25 Locations)
    **Split by Tribe** - Each tribe has its own set of technology locations, and the randomization
                         will be done separately for each tribe. (Adds 25 Locations per tribe)
    """
    display_name = "Randomize Technology Locations"

    option_disable = 0
    option_off = 0
    option_enable = 1
    option_on = 1
    option_split_by_tribe = 2

    default = option_enable

class TechnologyItems(Choice):
    """Should technology items be randomized or not.

    **Disabled** - Technology items will not be randomized.
    **Enabled** - Technology items will be randomized. (Adds 25 Items)
    **Split by Tribe** - Each tribe has its own set of technology items, and the randomization
                         will be done separately for each tribe. (Adds 25 Items per tribe)
    **Split by Action** - Technology items are split by the action they are associated with. (Adds XX Items)
    **Split by Tribe and Action** - Technology items are split by both tribe and action. (Adds XX Items per tribe)
    """
    display_name = "Randomize Technology Items"

    option_disable = 0
    option_off = 0
    option_enable = 1
    option_on = 1
    option_split_by_tribe = 2
    # option_split_by_action = 3
    # option_split_by_tribe_and_action = 4

    default = option_enable

# class RandomizeStartingUnit(Choice):
#     """Whether to randomize starting unit or not.
#     Affects only when Technology Items are split by action.
#     """

#     display_name = "Randomize Starting Unit"
#     option_disable = 0
#     option_off = 0



polytopia_option_groups = [
    OptionGroup("Goal Options", [RequiredUniqueTribesWins, RequiredScoreForVictory]),
    OptionGroup("Playable Tribes", [PlayableTribes, FirstUnlockedTribe]),
    OptionGroup("Score Check Options", [ScoreChecksMin, ScoreChecksMax,
                                        ScoreChecksStep, ShouldSendScoreChecksImmediately, ExcludeScoreChecksAfter]),
    OptionGroup("Technology Randomization Options", [TechnologyLocations, TechnologyItems])
]

@dataclass
class PolytopiaOptions(PerGameCommonOptions):
    unique_tribes_wins: RequiredUniqueTribesWins
    score_for_victory: RequiredScoreForVictory
    playable_tribes: PlayableTribes
    first_unlocked_tribe: FirstUnlockedTribe
    score_checks_min: ScoreChecksMin
    score_checks_max: ScoreChecksMax
    score_checks_step: ScoreChecksStep
    send_score_checks_immediately: ShouldSendScoreChecksImmediately
    exclude_score_checks_after: ExcludeScoreChecksAfter
    technology_locations: TechnologyLocations
    technology_items: TechnologyItems





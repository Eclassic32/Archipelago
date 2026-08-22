from dataclasses import dataclass

from Options import Choice, DefaultOnToggle, NamedRange, OptionGroup, OptionSet, PerGameCommonOptions, Range, Toggle

from .strings import REGULAR_TRIBE_NAMES, TRIBE_NAMES


# Playable Tribes
class PlayableTribes(OptionSet):
    """List of tribes that can be selected for play.
    Notice: Client mod does NOT let you select tribes that you do not own in main game.

    Possible values: {TRIBE_NAMES}
    """

    display_name = "Playable Tribes"
    valid_keys = TRIBE_NAMES
    default = REGULAR_TRIBE_NAMES

class FirstUnlockedTribe(Choice):
    """The first tribe that will be unlocked for the player.
    Notice: Client mod does NOT let you select tribes that you do not own in main game.

    Possible values: {TRIBE_NAMES}
    """

    display_name = "First Unlocked Tribe"
    valid_keys = TRIBE_NAMES
    default = "Xinxi"

# Goal Options
class RequiredUniqueTribesWins(Range):
    """Amount of wins with unique tribes required for a player to goal the game.

    min = 1, max = 16, default = 4
    """

    display_name = "Match Wins required for Victory"
    range_start = 1
    range_end = 16
    default = 4

class RequiredScoreForVictory(NamedRange):
    """Score required for a tribe to be considered as victorious.

    Rating in the main game:
    1 star = 10k
    2 stars = 25k
    3 stars = 50k

    min = 1, max = 100, default = 50
    """

    display_name = "Score required for Victory"
    range_start = 1
    range_end = 100
    default = 50
    special_range_names = {  # noqa: RUF012
        "1_Star": 10,
        "2_Stars": 25,
        "3_Stars": 50
    }

# Score Check Options
class ScoreChecksMin(NamedRange):
    """Minimum score*1000 for score checks.
    Setting ScoreChecksMin and ScoreChecksMax to 0 will disable score checks.

    Rating in the main game:
        1 star = 10k
        2 stars = 25k
        3 stars = 50k

    min = 0, max = 100, default = 10
    """

    display_name = "Minimum Score Checks (*1000)"
    range_start = 0
    range_end = 100
    default = 10
    special_range_names = {  # noqa: RUF012
        "1_Star": 10,
        "2_Stars": 25,
        "3_Stars": 50
    }

class ScoreChecksMax(NamedRange):
    """Maximum score*1000 for score checks.
    Setting ScoreChecksMin and ScoreChecksMax to 0 will disable score checks.

    Rating in the main game:
        1 star = 10k
        2 stars = 25k
        3 stars = 50k

    min = 0, max = 100, default = 100
    """

    display_name = "Maximum Score Checks (*1000)"
    range_start = 0
    range_end = 100
    default = 50
    special_range_names = {  # noqa: RUF012
        "1_Star": 10,
        "2_Stars": 25,
        "3_Stars": 50
    }

class ScoreChecksStep(Range):
    """Step size for score checks. (*1000)

    min = 1, max = 100, default = 10
    """

    display_name = "Score Checks Step Size (*1000)"
    range_start = 1
    range_end = 100
    default = 10

class ShouldSendScoreChecksImmediately(DefaultOnToggle):
    """Whether to send score checks immediately or wait until the end of the match.

    True - Send score checks immediately
    False - Wait until the end of the match to send score checks
    """

    display_name = "Send Score Checks Immediately"

polytopia_option_groups = [
    OptionGroup("Goal Options", [RequiredUniqueTribesWins, RequiredScoreForVictory]),
    OptionGroup("Playable Tribes", [PlayableTribes, FirstUnlockedTribe]),
    OptionGroup("Score Check Options", [ScoreChecksMin, ScoreChecksMax,
                                        ScoreChecksStep, ShouldSendScoreChecksImmediately]),
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
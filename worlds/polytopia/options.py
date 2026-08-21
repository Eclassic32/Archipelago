from dataclasses import dataclass

from Options import OptionSet, Range, Toggle

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

# Goal Options
class RequiredUniqueTribeWins(Range):
    """Amount of wins with unique tribes required for a player to goal the game.

    min = 1, max = 16, default = 4
    """

    display_name = "Match Wins required for Victory"
    range_start = 1
    range_end = 16
    default = 4

class RequiredScoreForVictory(Range):
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

# Score Check Options
class ScoreChecksMin(Range):
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

class ScoreChecksMax(Range):
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

class ScoreChecksStep(Range):
    """Step size for score checks.

    min = 1, max = 100, default = 10
    """

    display_name = "Score Checks Step Size"
    range_start = 1
    range_end = 100
    default = 10

class ShouldSendScoreChecksImmediately(Toggle):
    """Whether to send score checks immediately or wait until the end of the match.

    True - Send score checks immediately
    False - Wait until the end of the match to send score checks
    """

    display_name = "Send Score Checks Immediately"
    default = True

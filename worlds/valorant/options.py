from dataclasses import dataclass

from Options import Choice, NamedRange, OptionGroup, OptionSet, PerGameCommonOptions, Range
from worlds.valorant.constants import AGENT_LIST


class PlayableAgents(OptionSet):
    """List of agents that can be selected for play.

    Possible values:
    ["Breach", "Brimstone", "Chamber", "Cypher", "Fade", "Harbor",
     "Jett",   "KAY/O",     "Killjoy", "Neon",   "Omen", "Phoenix",
     "Raze",   "Reyna",     "Sage",    "Skye",   "Sova", "Viper",
     "Yoru",   "Deadlock",  "Gekko",   "KAY/O",  "Neon",
     "Iso",    "Clove",     "Hush"]
    """

    display_name = "Playable Agents"
    valid_keys = AGENT_LIST
    default = AGENT_LIST

class FirstUnlockedAgent(Choice):
    """The first agent that will be unlocked for the player.

    Possible values:
    "Breach", "Brimstone", "Chamber", "Cypher", "Fade", "Harbor",
    "Jett",   "KAYO",     "Killjoy", "Neon",   "Omen", "Phoenix",
    "Raze",   "Reyna",     "Sage",    "Skye",   "Sova", "Viper",
    "Yoru",   "Deadlock",  "Gekko",   "KAY/O",  "Neon",
    "Iso",    "Clove",     "Hush",
    "any_playable" - random playable agent
    """

    display_name = "First Unlocked Agent"
    option_any_playable = -1

    option_brimstone = 1
    option_viper = 2
    option_omen = 3
    option_killjoy = 4
    option_cypher = 5
    option_sova = 6
    option_sage = 7
    option_phoenix = 9
    option_jett = 10
    option_reyna = 11
    option_raze = 12
    option_breach = 13
    option_skye = 14
    option_yoru = 15
    option_astra = 16
    option_kayo = 17
    option_chamber = 18
    option_neon = 19
    option_fade = 20
    option_harbor = 21
    option_gekko = 22
    option_deadlock = 23
    option_iso = 24
    option_clove = 25
    option_vyse = 26
    option_tejo = 27
    option_waylay = 28
    option_veto = 29
    option_miks = 30
    option_hush = 31

    default = option_any_playable

class GoalType(Choice):
    """The type of goal that will be used for the game.

    Possible values:
    "unique_agents" - win with a certain number of unique agents
    "score" - reach a certain score
    """

    display_name = "Goal Type"
    option_unique_agents = 1
    option_wins = 2

    default = option_unique_agents

class GoalUniqueAgentsWins(NamedRange):
    """Amount of wins with unique agents required for a player to goal the game.

    """

    display_name = "Unique Agent Wins required for Victory"
    range_start = 1
    range_end = len(AGENT_LIST)
    default = 4
    special_range_names = {
        "all_agents": -2,
        "all_playable": -1,
    }

class GoalWins(Range):
    """Amount of wins required for a player to goal the game.

    """

    display_name = "Wins required for Victory"
    range_start = 1
    range_end = 100
    default = 10

class PlantDefuseSanity(Choice):
    """Whether to include Plant/Defuse checks.

    Possible values:
    "off" - no sanity checks
    "on" - include sanity checks (+2 checks)
    "each_agent" - include sanity checks for each playable agent (+2 checks per agent)
    """

    display_name = "Plant/Defuse Sanity Check"
    option_off = 0
    option_on = 1
    option_each_agent = 2
    default = option_on

class AssistSanity(Choice):
    """Whether to include Assist checks.

    Possible values:
    "off" - no sanity checks
    "on" - include sanity checks (+1 check per agent)
    """

    display_name = "Assist Sanity Check"
    option_off = 0
    option_on = 1
    default = option_off

class EnemyAgentSanity(Choice):
    """Whether to include killing each enemy agent checks.

    Possible values:
    "off" - no sanity checks
    "once_per_playable_agent" - include checks for killing as each playable agent
                                                    (+1 check per playable_agent)
    "once_per_enemy_agent" - include checks for killing each enemy agent once
                                                    (+1 check per all_agents)
    "all_agents" - include checks for killing each enemy agent as each playable agent
                                                    (playable_agents * all_agents checks)
    """

    display_name = "Enemy Agent Sanity Check"
    option_off = 0
    option_once_per_playable_agent = 1
    option_once_per_enemy_agent = 2
    option_all_agents = 3
    default = option_once_per_playable_agent

class WeaponSanity(Choice):
    """Whether to include killing with each weapon sanity checks.

    Possible values:
    "off" - no sanity checks
    "each_weapon" - include checks for killing with each weapon
                                                    (+1 check per weapon)
    "once_per_playable_agent" - include checks for killing with each weapn as each playable agent
                                                    (playable_agents * all_weapons checks)
    """

    display_name = "Weapon Sanity Check"
    option_off = 0
    option_each_weapon = 1
    option_once_per_playable_agent = 2
    default = option_off

class IncludeDamagingAbilities(Choice):
    """Whether to include damaging abilities in the Weapons Sanity checks.
    Note: This option only applies if Weapon Sanity checks are enabled.

    Possible values:
    "off" - only use buyable weapons for Weapon Sanity checks
    "on" - include damaging abilities to Weapon Sanity checks
    """

    display_name = "Include Damaging Abilities in Weapons Sanity Checks"
    option_off = 0
    option_on = 1
    default = option_on

class EnableMaxSanityChecks(Choice):
    """Whether to enable the maximum number of sanity checks.
    Note: Max Sanity will disable any other Sanity checks.

    Possible values:
    "off" - no max sanity checks
    "on" - include max sanity checks
    """

    display_name = "Enable Max Sanity Checks"
    option_off = 0
    option_on = 1
    default = option_off

class IncludedMaxSanityLocationTypes(OptionSet):
    """List of location types that will be included in the max sanity checks.

    Possible values:
    ["Kill", "Assist", "Plant", "Defuse", "Round Results"]
    """

    display_name = "Included Max Sanity Location Types"
    valid_keys = ["Kill", "Assist", "Plant", "Defuse", "Round Results"]
    default = ["Kill", "Assist", "Plant", "Defuse"]

class IncludedMaxSanityChecks(OptionSet):
    """List of sanity checks that will be included in the game.


    Possible values:
    ["Playable Agent", "Enemy Agent", "Weapon", "Maps", "Game Modes"]
    """

    display_name = "Included Max Sanity Checks"
    valid_keys = ["Playable Agent", "Enemy Agent", "Weapon", "Maps", "Game Modes"]
    default = ["Playable Agent", "Enemy Agent", "Weapon"]

class IncludedMaps(OptionSet):
    """List of maps that will be included in the max sanity checks.

    Possible values:
    ["Bind", "Haven", "Split", "Ascent", "Icebox", "Breeze",
     "Fracture", "Pearl", "Lotus", "Sunset", "Abyss", "Corrode", "Summit",
     "District", "Kasbah", "Piazza", "Drift", "Glitch",
     "Skirmish A", "Skirmish B", "Skirmish C", "Skirmish D", "Skirmish E",
     "Gauntlet", "The Range"
     ]
    """

    display_name = "Included Maps"
    valid_keys = ["Bind", "Haven", "Split", "Ascent", "Icebox", "Breeze",
         "Fracture", "Pearl", "Lotus", "Sunset", "Abyss", "Corrode", "Summit",
         "District", "Kasbah", "Piazza", "Drift", "Glitch",
         "Skirmish A", "Skirmish B", "Skirmish C", "Skirmish D", "Skirmish E",
         "Gauntlet", "The Range"]
    default = ["Bind", "Haven", "Split", "Ascent", "Icebox", "Breeze",
         "Fracture", "Pearl", "Lotus", "Sunset", "Abyss", "Corrode", "Summit",
         "District", "Kasbah", "Piazza", "Drift", "Glitch",
         "Skirmish A", "Skirmish B", "Skirmish C", "Skirmish D", "Skirmish E",
         "Gauntlet", "The Range"]

class IncludedGameModes(OptionSet):
    """List of game modes that will be included in the max sanity checks.

    Possible values:
    ["Unrated", "Competitive", "Spike Rush", "Deathmatch", "Escalation", "Replication"]
    """

    display_name = "Included Game Modes"
    valid_keys = ["Unrated", "Competitive", "Spike Rush", "Deathmatch", "Escalation", "Replication"]
    default = ["Unrated", "Competitive", "Spike Rush"]

class IncludedMapsOnRotation(OptionSet):
    """List of maps that is currently included in the map rotation.
    Used for game modes Competitive, Premier and Deathmatch

    Possible values:
    ["Bind", "Haven", "Split", "Ascent", "Icebox", "Breeze",
    "Fracture", "Pearl", "Lotus", "Sunset", "Abyss", "Corrode", "Summit",]
    """

    display_name = "Included Maps on Rotation"
    valid_keys = ["Bind", "Haven", "Split", "Ascent", "Icebox", "Breeze",
        "Fracture", "Pearl", "Lotus", "Sunset", "Abyss", "Corrode", "Summit"]
    default = ["Abyss", "Bind", "Corrode", "Haven", "Lotus", "Sunset", "Summit"]

valorant_option_groups = [
    OptionGroup("Goal Options", [GoalType, GoalUniqueAgentsWins, GoalWins]),
    OptionGroup("Playable Agents", [PlayableAgents, FirstUnlockedAgent]),
    OptionGroup("Regular Sanity Checks", [AssistSanity, EnemyAgentSanity, WeaponSanity]),
    OptionGroup("Max Sanity Checks", [EnableMaxSanityChecks, IncludedMaxSanityChecks, IncludedMaxSanityLocationTypes,
                                      IncludedMaps, IncludedGameModes, IncludedMapsOnRotation]),
]

@dataclass
class ValorantOptions(PerGameCommonOptions):
    playable_agents: PlayableAgents

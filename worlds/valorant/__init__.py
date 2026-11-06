from collections.abc import Mapping
from typing import Any

from BaseClasses import Tutorial
from Options import OptionError
from worlds.AutoWorld import WebWorld, World

from . import items, locations, regions, rules
from .constants import (
    AGENT_LIST,
    AGENT_NAME_TO_ID,
    ALLOW_MAX_SANITY,
    ALLOW_RATING_GAME_MODES,
    COMPETITIVE_MODES,
    ROTATING_MAP_MODES,
    get_agent_id_list,
)
from .items import ITEM_NAME_TO_ID
from .locations import LOCATION_ID_TO_NAME, LOCATION_NAME_TO_ID
from .options import ValorantOptions, valorant_option_groups


class ValorantWebWorld(WebWorld):
    game = "Valorant"
    theme = "grass"
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Archipelago Valorant randomizer.",
        "English",
        "setup_en.md",
        "setup/en",
        ["ec32"],
    )
    tutorials = [setup_en]
    option_groups = valorant_option_groups


class ValorantWorld(World):
    """
    Valorant
    """
    game = "Valorant"

    options_dataclass = ValorantOptions
    options: ValorantOptions # type: ignore

    location_id_to_name = LOCATION_ID_TO_NAME
    location_name_to_id = LOCATION_NAME_TO_ID
    item_name_to_id = ITEM_NAME_TO_ID

    def create_regions(self) -> None:
        regions.create_and_connect_regions(self)
        locations.create_all_locations(self)

    def set_rules(self) -> None:
        rules.set_all_rules(self)

    def create_items(self) -> None:
        items.create_all_items(self)

    def create_item(self, name: str) -> items.ValorantItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def generate_early(self) -> None:
        o = self.options

        playable_agent_ids = get_agent_id_list(o.playable_agents.value)

        if not playable_agent_ids:
            raise OptionError("[VALORANT] No playable agents selected.")

        if o.first_unlocked_agent.value == -1:
            o.first_unlocked_agent.value = playable_agent_ids[self.random.randint(0, len(playable_agent_ids) - 1)]

        if o.first_unlocked_agent.value not in playable_agent_ids:
            raise OptionError("[VALORANT] First unlocked agent is not in the list of playable agents.")

        if o.goal_type.value == 1:
            if o.unique_agents_wins.value > len(playable_agent_ids):
                raise OptionError("[VALORANT] Not enough playable agents for the unique agents goal type.")

        if o.enable_max_sanity_checks.value == 1:
            if not ALLOW_MAX_SANITY:
                raise OptionError("[VALORANT] Max sanity checks are not allowed in the host.yaml file.")

            o.assist_sanity.value = 0
            o.plant_defuse_sanity.value = 0
            o.enemy_agent_sanity.value = 0
            o.weapon_sanity.value = 0

            if o.included_max_sanity_checks.value.__len__() < 1:
                raise OptionError("[VALORANT] At least one max sanity check must be included.")

            if o.included_max_sanity_location_types.value.__len__() < 1:
                raise OptionError("[VALORANT] At least one max sanity location type must be included.")

            if "Game Modes" in o.included_max_sanity_checks.value:
                if o.included_game_modes.value.__len__() < 1:
                    raise OptionError("[VALORANT] At least one game mode must be included.")
                includes_rating_game_modes = any(mode in o.included_game_modes.value for mode in COMPETITIVE_MODES)
                if not ALLOW_RATING_GAME_MODES and includes_rating_game_modes:
                    raise OptionError("[VALORANT] Rating game modes are not allowed in the host.yaml file.")

            if "Maps" in o.included_max_sanity_checks.value:
                if o.included_maps.value.__len__() < 1:
                    raise OptionError("[VALORANT] At least one map must be included.")
                includes_mods_with_rmaps = "Game Modes" in o.included_max_sanity_checks.value and \
                            any(mode in o.included_game_modes.value for mode in ROTATING_MAP_MODES)
                if includes_mods_with_rmaps and o.included_maps_on_rotation.value.__len__() < 1:
                    raise OptionError("[VALORANT] At least one map must be included in the map rotation.")


    def fill_slot_data(self) -> Mapping[str, Any]:
        return {
            "playable_agents": self.options.playable_agents.value,
            "goal_type": self.options.goal_type.value,
            "unique_agents_wins": self.options.unique_agents_wins.value,
            "goal_wins": self.options.goal_wins.value,
            "assist_sanity": self.options.assist_sanity.value,
            "enemy_agent_sanity": self.options.enemy_agent_sanity.value,
            "weapon_sanity": self.options.weapon_sanity.value,
            "include_damaging_abilities": self.options.include_damaging_abilities.value,
            "plant_defuse_sanity": self.options.plant_defuse_sanity.value,
            "enable_max_sanity_checks": self.options.enable_max_sanity_checks.value,
            "included_max_sanity_checks": self.options.included_max_sanity_checks.value,
            "included_max_sanity_location_types": self.options.included_max_sanity_location_types.value,
            "included_maps": self.options.included_maps.value,
            "included_game_modes": self.options.included_game_modes.value,
            "included_maps_on_rotation": self.options.included_maps_on_rotation.value,
        }

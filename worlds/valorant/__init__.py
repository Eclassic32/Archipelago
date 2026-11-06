from collections.abc import Mapping
from typing import Any

from BaseClasses import Tutorial
from Options import OptionError
from worlds.AutoWorld import WebWorld, World

from . import items, locations, regions, rules
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

        # Options Check here


    def fill_slot_data(self) -> Mapping[str, Any]:
        return {
            "playable_tribes": self.options.playable_tribes.value,
            "unique_tribes_wins": self.options.unique_tribes_wins.value,
            "score_to_victory": self.options.score_for_victory.value,
            "send_score_checks_immediately": self.options.send_score_checks_immediately.value,
            "technology_locations": self.options.technology_locations.value,
            "technology_items": self.options.technology_items.value,
        }

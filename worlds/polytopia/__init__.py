from collections.abc import Mapping
from typing import Any

from BaseClasses import Tutorial
from Options import OptionError
from worlds.AutoWorld import WebWorld, World
from worlds.polytopia.constants import TRIBE_NAMES, disable_tech_shuffle_for_special_tribes

from . import items, locations, regions, rules
from .items import ITEM_NAME_TO_ID
from .locations import LOCATION_ID_TO_NAME, LOCATION_NAME_TO_ID
from .options import PolytopiaOptions, polytopia_option_groups


class PolytopiaWebWorld(WebWorld):
    game = "The Battle of Polytopia"
    theme = "grass"
    setup_en = Tutorial(
        "Multiworld Setup Guide",
        "A guide to setting up the Archipelago The Battle of Polytopia randomizer.",
        "English",
        "setup_en.md",
        "setup/en",
        ["ec32"],
    )
    tutorials = [setup_en]
    option_groups = polytopia_option_groups


class PolytopiaWorld(World):
    """
    The Battle of Polytopia
    """
    game = "The Battle of Polytopia"

    options_dataclass = PolytopiaOptions
    options: PolytopiaOptions # type: ignore

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

    def create_item(self, name: str) -> items.PolytopiaItem:
        return items.create_item_with_correct_classification(self, name)

    def get_filler_item_name(self) -> str:
        return items.get_random_filler_item_name(self)

    def generate_early(self) -> None:
        o = self.options

        if o.exclude_score_checks_after.value == 0:
            o.exclude_score_checks_after.value = o.score_for_victory.value

        if o.playable_tribes.value.__len__() < 1:
            raise OptionError("[The Battle of Polytopia] At least one tribe must be selected to play.")

        if o.playable_tribes.value.__len__() < o.unique_tribes_wins.value:
            raise OptionError(
            f"[The Battle of Polytopia] The number of unique tribes required for victory ({o.unique_tribes_wins.value})"
            f" cannot exceed the number of playable tribes ({o.playable_tribes.value.__len__()})."
            )

        if o.first_unlocked_tribe.value == -4:
            tribe = TRIBE_NAMES[self.random.randint(0, len(o.playable_tribes.value) - 1)]
            o.first_unlocked_tribe.value = TRIBE_NAMES.index(tribe)

        if o.first_unlocked_tribe.value in [-3, -2, -1]: # first tribe is randomized
            choice = o.first_unlocked_tribe.value + 4
            randoms = [list(range(0, len(TRIBE_NAMES))), list(range(12, 16)), list(range(0, 12)), list(range(0, 4))]
            o.first_unlocked_tribe.value = randoms[choice][self.random.randint(0, len(randoms[choice]) - 1)]

        if TRIBE_NAMES[o.first_unlocked_tribe.value] not in o.playable_tribes.value:
            raise OptionError(
                f"[The Battle of Polytopia] The first unlocked tribe ({TRIBE_NAMES[o.first_unlocked_tribe.value]}) "
                f"must be one of the playable tribes ({o.playable_tribes.value})."
            )

        if disable_tech_shuffle_for_special_tribes(o.technology_locations.value,
                                                   o.technology_items.value,
                                                   o.playable_tribes.value):
            raise OptionError(
                "[The Battle of Polytopia] Shuffling of technology locations and items is not tested when "
                "special tribes are playable, therefore currently it is disabled. Please modify "
                "[polytopia/constants.py] to enable it if you want to use special tribes."
            )

    def fill_slot_data(self) -> Mapping[str, Any]:
        return {
            "playable_tribes": self.options.playable_tribes.value,
            "unique_tribes_wins": self.options.unique_tribes_wins.value,
            "score_to_victory": self.options.score_for_victory.value,
            "send_score_checks_immediately": self.options.send_score_checks_immediately.value,
            "technology_locations": self.options.technology_locations.value,
            "technology_items": self.options.technology_items.value,
        }

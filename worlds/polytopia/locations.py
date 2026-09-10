from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Location

from . import items
from .constants import MAX_SCORE_K, TECHNOLOGY_NAMES, TECHNOLOGY_OFFSET, TRIBE_NAMES, tribe_specific_id

# from .options import *

if TYPE_CHECKING:
    from . import PolytopiaWorld

class PolytopiaLocation(Location):
    game = "The Battle of Polytopia"

def generate_tribe_victory_locations() -> dict[str, int]:
    """Generate a dictionary of tribe victory locations with their corresponding IDs.

    Returns:
        dict[str, int]: A dictionary where keys are tribe names and values are their corresponding IDs.
    """
    base_id = 0
    return {f"{tribe} - Victory": tribe_specific_id(index, base_id)
                                  for index, tribe in enumerate(TRIBE_NAMES, start=1)}

def generate_tribe_score_locations() -> dict[str, int]:
    """Generate a dictionary of tribe score locations with their corresponding IDs.

    Returns:
        dict[str, int]: A dictionary where keys are tribe names and values are their corresponding IDs.
    """
    result = {}
    for tribe_index, tribe_name in enumerate(TRIBE_NAMES, start=1):
        for score in range(1, MAX_SCORE_K + 1):
            location_name = f"{tribe_name} - Score {score}K"
            location_id = tribe_specific_id(tribe_index, score)
            result[location_name] = location_id

    return result

def generate_technology_locations() -> dict[str, int]:
    """Generate a dictionary of technology locations with their corresponding IDs.

    Returns:
        dict[str, int]: A dictionary where keys are technology names and values are their corresponding IDs.
    """
    return {f"Technology - {tech_name}": tribe_specific_id(0, index + TECHNOLOGY_OFFSET)
                                         for index, tech_name in enumerate(TECHNOLOGY_NAMES, start=1)}

def generate_technology_locations_by_tribe() -> dict[str, int]:
    """Generate a dictionary of technology locations for each tribe with their corresponding IDs.

    Returns:
        dict[str, int]: A dictionary where keys are technology names and values are their corresponding IDs.
    """
    result = {}
    for tribe_index, tribe_name in enumerate(TRIBE_NAMES, start=1):
        for tech_index, tech_name in enumerate(TECHNOLOGY_NAMES, start=1):
            location_name = f"{tribe_name} - Technology - {tech_name}"
            location_id = tribe_specific_id(tribe_index, tech_index + TECHNOLOGY_OFFSET)
            result[location_name] = location_id

    return result

location_table = {
    **generate_tribe_victory_locations(),
    **generate_tribe_score_locations(),
    **generate_technology_locations(),
    **generate_technology_locations_by_tribe(),
}

LOCATION_ID_TO_NAME: dict[int, str] = {id: location_name for location_name, id in location_table.items()}
LOCATION_NAME_TO_ID: dict[str, int] = dict(location_table.items())

def get_location_names_with_ids(location_names: list[str]) -> dict[str, int | None]:
    return {location_name: location_table[location_name] for location_name in location_names}

def create_regular_locations(world: PolytopiaWorld) -> None:
    o = world.options

    if o.technology_locations.value == 1:
        menu = world.get_region("Menu")
        for tech_id, tech_name in enumerate(TECHNOLOGY_NAMES, start=1):
            menu.locations.append(PolytopiaLocation(world.player, f"Technology - {tech_name}",
                                                    tribe_specific_id(0, tech_id + TECHNOLOGY_OFFSET), menu))

    for tribe in o.playable_tribes.value:
        tribe_index = TRIBE_NAMES.index(tribe) + 1
        region = world.get_region(f"Tribe - {tribe}")

        victory_location = PolytopiaLocation(world.player, f"{tribe} - Victory",
                                            tribe_specific_id(tribe_index, 0), region)
        region.locations.append(victory_location)

        if o.technology_locations.value == 2:
            for tech_id, tech_name in enumerate(TECHNOLOGY_NAMES, start=1):
                region.locations.append(PolytopiaLocation(world.player, f"{tribe} - Technology - {tech_name}",
                                                tribe_specific_id(tribe_index, tech_id + TECHNOLOGY_OFFSET), region))

        if o.score_checks_min == 0 or o.score_checks_max == 0 or o.score_checks_step == 0:
            continue

        for score in range(o.score_checks_min, o.score_checks_max + 1, o.score_checks_step):
            location = PolytopiaLocation(world.player, f"{tribe} - Score {score}K",
                                         tribe_specific_id(tribe_index, score), region)

            region.locations.append(location)


def create_events(world: PolytopiaWorld) -> None:
    menu = world.get_region("Menu")
    menu.add_event("All Tribes Victorious", "Game Goaled",
                        location_type=PolytopiaLocation, item_type=items.PolytopiaItem)

def create_all_locations(world: PolytopiaWorld) -> None:
    create_regular_locations(world)
    create_events(world)

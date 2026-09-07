from typing import TYPE_CHECKING, NamedTuple

from BaseClasses import Item
from BaseClasses import ItemClassification as IC  # noqa: N817

# from .options import *
from .constants import TECHNOLOGY_NAMES, TECHNOLOGY_OFFSET, TRIBE_NAMES, tribe_specific_id

if TYPE_CHECKING:
    from . import PolytopiaWorld

class PolytopiaItem(Item):
    game: str = "The Battle of Polytopia"

class ItemData(NamedTuple):
    id: int
    classification: IC

base_id = 0


def generate_tribe_unlock_items() -> dict[str, ItemData]:
    """Generate a dictionary of tribe unlock items with their corresponding IDs.

    Returns:
        dict[str, ItemData]: A dictionary where keys are tribe names and values are their corresponding ItemData.
    """
    return {f"Tribe Unlock - {tribe_name}": ItemData(tribe_specific_id(index, 0), IC.progression|IC.useful) \
                                            for index, tribe_name in enumerate(TRIBE_NAMES, start=1)}

def generate_technology_items() -> dict[str, ItemData]:
    """Generate a dictionary of technology items with their corresponding IDs.

    Returns:
        dict[str, ItemData]: A dictionary where keys are technology names and values are their corresponding ItemData.
    """
    return {f"Technology Unlock - {tech_name}": \
                ItemData(tribe_specific_id(0, index + TECHNOLOGY_OFFSET), IC.progression|IC.useful) \
                for index, tech_name in enumerate(TECHNOLOGY_NAMES, start=1)}

def generate_technology_items_by_tribe() -> dict[str, ItemData]:
    """Generate a dictionary of technology items for each tribe with their corresponding IDs.

    Returns:
        dict[str, ItemData]: A dictionary where keys are technology names and values are their corresponding ItemData.
    """
    result = {}
    for tribe_index, tribe_name in enumerate(TRIBE_NAMES, start=1):
        for tech_index, tech_name in enumerate(TECHNOLOGY_NAMES, start=1):
            item_name = f"{tribe_name} - Technology Unlock - {tech_name}"
            item_id = tribe_specific_id(tribe_index, tech_index + TECHNOLOGY_OFFSET)
            result[item_name] = ItemData(item_id, IC.progression|IC.useful)
    return result

item_table = {
    **generate_tribe_unlock_items(),
    **generate_technology_items(),
    **generate_technology_items_by_tribe(),
    "Filler": ItemData(base_id + 900, IC.filler),
}
ITEM_NAME_TO_ID: dict[str, int] = {item_name: data.id for item_name, data in item_table.items()}

def get_random_filler_item_name(world: "PolytopiaWorld") -> str:
    # if world.random.randint(0, 99) < world.options.trap_chance.value:
    #     return world.random.choice(traps)
    # return world.random.choice("filler")
    return "Filler"

def create_item_with_correct_classification(world: "PolytopiaWorld", name: str) -> PolytopiaItem:
    classification = item_table[name].classification

    # if world.options.option_variable_1.value == OptionClass1.option_1 and name in items_to_change:
    #    classification = IC.progression

    return PolytopiaItem(name, classification, ITEM_NAME_TO_ID[name], world.player)


def create_all_items(world: "PolytopiaWorld") -> None:
    o = world.options
    item_pool = []
    for tribe in TRIBE_NAMES:
        if tribe not in o.playable_tribes.value:
            continue
        if o.first_unlocked_tribe.value == TRIBE_NAMES.index(tribe):
            world.push_precollected(world.create_item(f"Tribe Unlock - {tribe}"))
            continue
        item_pool.append(world.create_item(f"Tribe Unlock - {tribe}"))

    match o.technology_items.value:
        case 0:  # No Technology Items
            pass
        case 1:  # No Split
            item_pool.append(world.create_item(f"Technology Unlock - {tech_name}") for tech_name in TECHNOLOGY_NAMES)

        case 2:  # Split by Tribe
            for tribe in TRIBE_NAMES:
                if tribe not in o.playable_tribes.value:
                    continue
                item_pool.append(world.create_item(f"Technology Unlock - {tribe} - {tech_name}")
                                                    for tech_name in TECHNOLOGY_NAMES)

        # case 3:  # Split by Action

        # case 4:  # Split by Tribe and Action

    # length of current itempool
    number_of_items = len(item_pool)

    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    # create filler for the remaining needed
    item_pool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += item_pool



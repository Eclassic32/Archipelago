from typing import TYPE_CHECKING, NamedTuple

from BaseClasses import Item
from BaseClasses import ItemClassification as IC

from .options import *
from .strings import TRIBE_NAMES

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
    return {f"Tribe Unlock - {tribe_name}": ItemData(base_id + index, IC.progression|IC.useful) \
                                            for index, tribe_name in enumerate(TRIBE_NAMES, start=1)}

item_table = generate_tribe_unlock_items()
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
    op = world.options
    item_pool = []
    item_pool.extend(world.create_item(item) for item in item_table)
    world.push_precollected(item_pool[op.first_unlocked_tribe.value])

    # length of current itempool
    number_of_items = len(item_pool)

    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    # create filler for the remaining needed
    item_pool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += item_pool



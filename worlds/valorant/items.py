from typing import TYPE_CHECKING, NamedTuple

from BaseClasses import Item
from BaseClasses import ItemClassification as IC  # noqa: N817

# from .options import *
from .constants import AGENTS, get_agent_id_list

if TYPE_CHECKING:
    from . import ValorantWorld

class ValorantItem(Item):
    game: str = "Valorant"

class ItemData(NamedTuple):
    id: int
    classification: IC

base_id = 0
# !!! FIX: Replace how IDs are given later !!!

def generate_agent_unlock_items() -> dict[str, ItemData]:
    """Generate a dictionary of agent unlock items with their corresponding IDs.

    Returns:
        dict[str, ItemData]: A dictionary where keys are agent names and values are their corresponding ItemData.
    """
    # Placeholder for agent names and IDs
    return {f"Agent Unlock - {AGENTS[agent]}": ItemData(base_id + agent + 1, IC.progression|IC.useful) \
                                                    for agent in AGENTS}



item_table = {
    **generate_agent_unlock_items(),
    "Filler": ItemData(base_id + 900, IC.filler),
}
ITEM_NAME_TO_ID: dict[str, int] = {item_name: data.id for item_name, data in item_table.items()}

def get_random_filler_item_name(world: "ValorantWorld") -> str:
    # if world.random.randint(0, 99) < world.options.trap_chance.value:
    #     return world.random.choice(traps)
    # return world.random.choice("filler")
    return "Filler"

def create_item_with_correct_classification(world: "ValorantWorld", name: str) -> ValorantItem:
    classification = item_table[name].classification

    # if world.options.option_variable_1.value == OptionClass1.option_1 and name in items_to_change:
    #    classification = IC.progression

    return ValorantItem(name, classification, ITEM_NAME_TO_ID[name], world.player)

def create_all_items(world: "ValorantWorld") -> None:
    o = world.options
    item_pool = []
    playable_agent_ids = get_agent_id_list(o.playable_agents.value)

    for agent in AGENTS:
        if agent not in playable_agent_ids:
            continue
        if o.first_unlocked_agent.value == agent:
            world.push_precollected(world.create_item(f"Agent Unlock - {AGENTS[agent]}"))
            continue
        item_pool.append(world.create_item(f"Agent Unlock - {AGENTS[agent]}"))


    number_of_items = len(item_table)

    number_of_unfilled_locations = len(world.multiworld.get_unfilled_locations(world.player))
    needed_number_of_filler_items = number_of_unfilled_locations - number_of_items
    # create filler for the remaining needed
    item_pool += [world.create_filler() for _ in range(needed_number_of_filler_items)]

    world.multiworld.itempool += item_pool

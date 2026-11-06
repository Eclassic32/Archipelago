from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Region

from .constants import AGENT_LIST

if TYPE_CHECKING:
    from . import ValorantWorld

def connect_regions(world: ValorantWorld) -> None:
    menu = world.multiworld.get_region("Menu", world.player)
    for agent_name in AGENT_LIST:
        agent_region = world.multiworld.get_region(f"Playing as {agent_name}", world.player)
        menu.connect(agent_region, f"Playing as {agent_name}")

def create_all_regions(world: ValorantWorld) -> None:
    menu = Region("Menu", world.player, world.multiworld)
    agent_regions = [Region(f"Playing as {agent_name}", world.player, world.multiworld) for agent_name in AGENT_LIST]

    world.multiworld.regions += menu, *agent_regions

def create_and_connect_regions(world: ValorantWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

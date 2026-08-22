from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import Region

from .constants import TRIBE_NAMES

if TYPE_CHECKING:
    from . import PolytopiaWorld

def connect_regions(world: PolytopiaWorld) -> None:
    main_menu = world.multiworld.get_region("Main Menu", world.player)
    for tribe_name in TRIBE_NAMES:
        tribe_region = world.multiworld.get_region(f"Tribe - {tribe_name}", world.player)
        main_menu.connect(tribe_region, f"Tribe - {tribe_name}")

def create_all_regions(world: PolytopiaWorld) -> None:
    main_menu = Region("Main Menu", world.player, world.multiworld)
    tribe_regions = [Region(f"Tribe - {tribe_name}", world.player, world.multiworld) for tribe_name in TRIBE_NAMES]

    world.multiworld.regions += main_menu, *tribe_regions

def create_and_connect_regions(world: PolytopiaWorld) -> None:
    create_all_regions(world)
    connect_regions(world)

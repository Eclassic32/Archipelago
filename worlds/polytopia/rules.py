from __future__ import annotations

from typing import TYPE_CHECKING

from BaseClasses import LocationProgressType
from rule_builder.rules import Has

# from .options import *

if TYPE_CHECKING:
    from . import PolytopiaWorld

def set_all_rules(world: PolytopiaWorld) -> None:
    set_all_location_rules(world)
    set_all_entrance_rules(world)

    # set_goal_rules(world)
    set_completion_condition(world)

def set_completion_condition(world: PolytopiaWorld) -> None:
    world.set_completion_rule(Has("Game Goaled"))

def set_all_entrance_rules(world: PolytopiaWorld) -> None:
    for tribe in world.options.playable_tribes.value:
        entrance = world.get_entrance(f"Tribe - {tribe}")
        world.set_rule(entrance, Has(f"Tribe Unlock - {tribe}"))

def set_all_location_rules(world: PolytopiaWorld) -> None:
    o = world.options
    for tribe in world.options.playable_tribes.value:
        item = f"Tribe Unlock - {tribe}"
        victory_loc = world.get_location(f"{tribe} - Victory")
        world.set_rule(victory_loc, Has(item))

        if o.score_checks_min == 0 or o.score_checks_max == 0 or o.score_checks_step == 0:
            continue

        for score in range(o.score_checks_min, o.score_checks_max + 1, o.score_checks_step):
            location = world.get_location(f"{tribe} - Score {score}K")

            if o.exclude_score_checks_after != -1 and score > o.exclude_score_checks_after:
                location.progress_type = LocationProgressType.EXCLUDED

            world.set_rule(location, Has(item))

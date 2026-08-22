from worlds.AutoWorld import WebWorld, World

from . import options as options


class PolytopiaWorld(World):
    """
    The Battle of Polytopia
    """
    game = "The Battle of Polytopia"

    options_dataclass = options.PolytopiaOptions
    options: options.PolytopiaOptions # type: ignore


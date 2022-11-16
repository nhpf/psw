"""Any Collectable that can be equipped  by the player as a weapon."""
from .collectable import Collectable
from typing import Tuple


class Equipable(Collectable):
    """Any Collectable that can be equipped  by the player as a weapon."""

    def __init__(
        self,
        position: Tuple[int, int],
        image_paths: list[str],
        dimensions: Tuple[int, int],
        rarity: float,
        attack_force: int,
        weight: float,
    ) -> None:
        """Initialize Equipable instance."""
        self.attack_force = attack_force
        self.weight = weight
        super().__init__(position, image_paths, dimensions, rarity)

"""Class that stores information about an authenticated user."""
from typing import Tuple


class AuthPlayer:
    """Class that stores information about an authenticated user."""

    def __init__(
        self,
        user_id: str,
        name: str,
        last_room: str,
        num_points: int,
        ranking: dict[int, int],
    ) -> None:
        """Initialize AuthPlayer instance."""
        self.user_id = user_id
        self.str = str
        self.name = name
        self.last_room = last_room
        self.num_points = num_points
        self.ranking = ranking

    @classmethod
    def subscribe_to_ranking(self) -> None:

        pass

    @classmethod
    def update_player_data(self, points: int, pos: Tuple[int, int]) -> None:

        pass

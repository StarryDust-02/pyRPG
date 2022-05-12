"""This is the file for objects abstract classes in pyRPG.

(c) StarryDust @StarryDust-02, all rights reserved."""

# imports
from __future__ import annotations
from typing import Optional


class Character:
    """An abstract class for all characters in the game.

    Instance Attributes:
        - name: the name of this character.
    """
    name: Optional[str] = 'placeholder_name'

    def __init__(self) -> None:
        raise NotImplementedError


class Item:
    """An abstract class for all items in the game.

    Instance Attributes:
        - name: the name of this item.
        - consumable: weather this item is a consumable item.
        """
    name: Optional[str] = 'unnamed_item'
    consumable: Optional[bool] = True

    def __init__(self) -> None:
        raise NotImplementedError

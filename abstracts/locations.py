"""This is the file abstract classes for in-game locations in pyRPG.

(c) StarryDust @StarryDust-02, all rights reserved."""

# imports
from __future__ import annotations
from typing import Optional


class Location:
    """An abstract class for all maps in the game.

    Instance Attributes:
        - name: the name of this location.
        - identifier: the identification of this location.
        - root: the root area of this location, if any.
        - sub: the sub area(s) of this location, if any.
    """
    name: Optional[str] = 'unnamed_map'
    identifier: str
    root: Optional[list[Location]] = None
    sub: Optional[list[Location]] = None

    def __init__(self, identifier: str) -> None:
        self.identifier = identifier

    def warp(self) -> None:
        raise NotImplementedError

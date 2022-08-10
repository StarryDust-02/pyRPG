"""This is the file for stats calculations in pyRPG.

(c) StarryDust @StarryDust-02, all rights reserved."""

# imports
from __future__ import annotations
from typing import Any, Optional


class Statistic:
    """An abstract class for for a set of stats in game.
    
    Instance Attributes
        - stat_set: the name and value of a set of stats.
    """
    _stat_set: Optional[list[str, dict[str: Any]]] = ['unamed_set', {'unnamed_attribute', None}]

    def __init__(self) -> None:
        raise NotImplementedError

    def add(self, attribute: str, value: float) -> str:

        self._stat_set[1][attribute] += value
        return 'added!'

    def subtract(self, attribute: str, value: float) -> str:

        self._stat_set[1][attribute] -= value
        return 'subtracted!'

    def change(self, attribute: str, value: Any) -> str:

        self._stat_set[1][attribute] = value
        return 'changed!'

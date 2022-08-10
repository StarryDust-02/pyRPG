"""As the name suggested.

(c) StarryDust @StarryDust-02, all rights reserved."""

# imports
from abstracts.objects import Character
from abstracts.stats import Statistic

class Occupation(Statistic):

    def __init__(self, job_title: str, \
        hp: int, mp: int, ap: int, dp: int) -> None:
        self._stat_set[0] = job_title
        self._stat_set[1]['Health'] = hp
        self._stat_set[1]['Magic'] = mp
        self._stat_set[1]['Attack'] = ap
        self._stat_set[1]['Defense'] = dp


class Protagonist(Character):
    """The player controled protagonist"""
    gender = str

    def __init__(self, name: str='default', is_female: bool=False) -> None:

        if is_female and name == 'default':
            self.name = 'Haruka'
            self.gender = 'Girl'

        elif not is_female and name == 'default':
            self.name = 'Sora'
            self.gender = 'Boy'
        
        elif is_female and name != 'default':
            self.name = name
            self.gender = 'Girl'
        
        else:
            self.name = name
            self.gender = 'Boy'


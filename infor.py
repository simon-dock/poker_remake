from cgitb import small
from enum import Enum

class status(Enum):
    Waiting = 0
    Blind = 1
    Cheched = 2
    Called = 3
    Raised = 4
    Folded = 5
    Allin = 6

class Position(Enum):
    DealerButton = 0
    SmallBlind = 1
    BigBlind = 2
    UnderTheGun = 3
    HighJack = 4
    CutOff = 5
 

class Setting():

    def __init__(self):
        self.sb_value = None
        self.game_count = None


class Player():
    
    def __init__(self):
        self.name = None
        self.status = status.Waiting
        self.position = None
        self.betting = 0
        self.cip = 100
        self.log_win = 0
        self.log_join = 0
        self.log_raise = 0
        self.log_cip = []
        
    def set_name(self, name):
        self.name = name

from enum import Enum

class status(Enum):
    waiting = 0
    cheched = 1
    called = 2
    raised = 3
    folded = 4
    allin = 5

class Setting():

    def __init__(self):
        self.sb_value = None
        self.game_count = None


class Player():
    
    def __init__(self):
        self.name = None
        self.state = status.waiting
        self.betting = 0
        self.log_win = 0
        self.log_join = 0
        self.log_raise = 0
        self.log_cip = 0
        
    def set_name(self, name):
        self.name = name

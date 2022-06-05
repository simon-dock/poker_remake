from cgitb import small
from enum import Enum
from re import S

class Status(Enum):
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
        self.status = Status.Waiting
        self.position = None
        self.betting = 0
        self.cip = 100
        self.log_win = 0
        self.log_join = 0
        self.log_raise = 0
        self.log_allin = 0
        self.log_cip = []
        
    def set_name(self, name):
        self.name = name

    def do_call(self, value):
        self.status = Status.Called
        self.betting += value
        self.cip -= value

    def do_raise(self, value):
        self.status = Status.Raised
        self.log_raise += 1
        self.betting += value
        self.cip -= value

    def do_check(self):
        self.status = Status.Cheched

    def do_Fold(self):
        self.status = Status.Folded

    def do_allin(self):
        self.status = Status.Allin
        self.betting += self.cip
        self.cip = 0

    def judge_command(self, command, max_bet):
        if type(command) == int:
            if self.betting + command == max_bet:
                self.do_call(command)
            elif self.betting + command >= max_bet*1.25:
                self.do_raise(command)
        elif command == 'c':
            self.do_check()
        elif command == 'f':
            self.do_Fold()
        elif command == 'allin':
            self.do_allin()
        else:
            print("error do_command")
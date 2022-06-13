import enum
from re import S

#色
WHITE = [255, 255, 255]
BLACK = [0, 0, 0]
GRAY = [193, 162, 129]
BLUE = [51, 255, 255]
W_BLUE = [204,255,255]
ORANGE = [255,127,0]

#サイズ
WIN_WIDTH = 1500
WIN_HEIGHT = 900

#状態を列挙
class Status(enum.Enum):
    Initial = 0
    MakeFunc = 1
    MakeP_1 = 2
    MakeP_2 = 3

#pygameの設定を管理するクラス
class Setting():

    def __init__(self):
        self.status_func = Status.Initial
        self.status_inner = Status.Initial
        self.entered = False
        self.txt = ""

    def set_status_func(self,status):
        self.status_func = status

    def set_status_inner(self,status):
        self.status_inner = status

    def set_entered(self,status):
        self.entered= status

    def set_txt(self,txt):
        self.txt= txt
    



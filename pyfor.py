import enum

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
    Makedata = 1
    Makeset = 2

#pygameの設定を管理するクラス
class Setting():

    def __init__(self):
        self.status = Status.Initial

    def set_status(self,status):
        self.status = status

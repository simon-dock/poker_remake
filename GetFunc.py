import infor

status = infor.Status
position = infor.Position

#次の添字を取得
def next_index(players, now_index):

    next_index = now_index + 1
    if next_index == len(players):
        next_index = 0

    return next_index

#特定の状態の人の数を取得する
def status_count(players, status):
    count = 0
    for i in range(len(players)):
        if players[i].status == status:
            count += 1
    return count

#特定の行動の人の数を取得する
def action_count(players, action):
    count = 0
    for i in range(len(players)):
        if players[i].action == action:
            count += 1
    return count

#何人残っているかを判断しフラグの状態を取得
def remain_count(Redo_Flag, players, setting):
    fold_count = status_count(players, status.Folded)
    if fold_count == len(players)-1:
        if players[setting.turn].position == position.BigBlind:
            Redo_Flag = False

    return Redo_Flag
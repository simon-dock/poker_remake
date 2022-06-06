import numpy as np

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
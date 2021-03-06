from ast import In
from distutils.log import info
from itertools import count
from operator import setitem
from tkinter import Place
from typing import List, Tuple
import copy
import GetFunc
import InFunc
import infor

status = infor.Status
position = infor.Position


def run_poker(Redo_Flag:bool, players:List[infor.Player], setting:infor.Setting, backup_play:List[infor.Player], backup_set:infor.Setting)->Tuple[bool, List[infor.Player], infor.Setting, List[infor.Player], infor.Setting]:
    """通常フェイズの処理

    Args:
        Redo_Flag (bool):
        players (List[infor.Player]): 
        setting (infor.Setting): 

    Returns:
        Tuple[bool, List[infor.Player], infor.Setting]:
    """
    #フォールド,オールインしていない
    if players[setting.turn].status != status.Folded and players[setting.turn].status != status.Allin:
        Rollback_Flag = True
        while Rollback_Flag:
            #データの表示
            print("--------------------")
            print("Now Player is ",players[setting.turn].name)
            print("You have         $",players[setting.turn].cip)
            print("Pot has          $",setting.main_pot)
            print("You are betting  $",players[setting.turn].betting)
            print("Max bet is       $",setting.call_need)
            print("Minimum raise is $",setting.call_need+setting.raise_before)
            print("--------------------")

            
            #入力受付、格納
            command = InFunc.what_do(players, setting)
            if command == 'b':
                print("")
                print("--------------------")
                print("Roll Back 1 phase")
                print("--------------------")
                print("")
                players = copy.deepcopy(backup_play)
                setting = copy.deepcopy(backup_set)
            else:
                #backupの作成
                backup_play = copy.deepcopy(players)
                backup_set = copy.deepcopy(setting)
                Rollback_Flag = False

                players[setting.turn].judge_command(command, setting.call_need)
                setting.set_turn_player_status(players[setting.turn].status)

                #オールインかチェックする
                if players[setting.turn].cip == 0:
                    players[setting.turn].set_status(status.Allin)
        

                #場の最大掛け金の更新 raiseの場合
                if players[setting.turn].status == status.Raised:
                    setting.update_raise_before(players[setting.turn].betting)
                    
                #allinの場合
                if players[setting.turn].status == status.Allin:
                    if players[setting.turn].betting > setting.call_need:
                        setting.update_raise_before(players[setting.turn].betting)
                
                #potの計算
                players, setting = get_pot(players, setting)
        
            

    #次のプレイヤーの添字を取得
    setting.turn = GetFunc.next_index(players, setting.turn)


    #次のプレイヤーの掛け金が場の掛け金と同額かつ
    #Wating状態でなくFold状態でもなければ終了
    if players[setting.turn].betting == setting.call_need:
        if players[setting.turn].status != status.Waiting and players[setting.turn].status != status.Folded:
            Redo_Flag = False

    return Redo_Flag, players, setting, backup_play, backup_set


def get_pot(players:List[infor.Player], setting:infor.Setting)->Tuple[List[infor.Player], infor.Setting]:
    """potを計算する

    Args:
        players (List[infor.Player]): 
        setting (infor.Setting): 

    Returns:
        Tuple[List[infor.Player], infor.Setting]:
    """

    setting.set_main_pot(sum_betting(players))

    return players, setting


def sum_betting(players: List[infor.Player])-> int:
    """プレイヤーの全員のベットを合計する

    Args:
        players (list[player]):

    Returns:
        sum
    """
    sum = 0
    for i in range(len(players)):
        sum += players[i].export_bet()

    return sum

def clean_up_phase(players:List[infor.Player], setting:infor.Setting)-> Tuple[List[infor.Player], infor.Setting]:
    """フェイズの後処理

    Args:
        players (List[infor.Player]):
        setting (infor.Setting): 

    Returns:
        Tuple[List[infor.Player], infor.Setting]:
    """
    setting.cleanup_phase()
    for i in range(len(players)):
        players[i].cleanup_phase()
    return players, setting


def clean_up_round(players:List[infor.Player], setting:infor.Setting)->Tuple[List[infor.Player], infor.Setting]:
    """ラウンドの後処理

    Args:
        players (List[infor.Player]): 
        setting (infor.Setting): 

    Returns:
        Tuple[List[infor.Player], infor.Setting]: 
    """
    setting.cleanup_round()
    for i in range(len(players)):
        players[i].cleanup_round()

    #ポジションを回す
    tmp_position = players[len(players)-1].position
    for i in reversed(range(1,len(players))):
        players[i].set_position(players[i-1].position)
    players[0].set_position(tmp_position)

    return players, setting

#u y ya t 
def preflop(players:List[infor.Player], setting:infor.Setting)-> Tuple[List[infor.Player],infor.Setting]:
    """プリフロップの処理
        ・sb,bbの設定
        ・bbのレイズの処理
        ・フロップへの参加者をカウント

    Args:
        players (List[infor.Player]):
        setting (infor.Setting):

    Returns:
        Tuple[List[infor.Player],infor.Setting]: 
    """

    print("/////////////////")
    print("Now it's Preflop.")
    print("/////////////////")
    print("")

    #sb,bbの状態とベット,ターンプレイヤーを設定
    for i in range(len(players)):
        if players[i].position == position.SmallBlind:
            players[i].set_blind(setting.sb_value)

        if players[i].position == position.BigBlind:
            players[i].set_blind(setting.sb_value*2)
            setting.update_blind(GetFunc.next_index(players, i))

    if len(players) == 2:
        players[0].set_blind(setting.sb_value*2)
        setting.update_blind(GetFunc.next_index(players, 0))

    Redo_Flag = True
    backup_play = copy.deepcopy(players)
    backup_set = copy.deepcopy(setting)

    #potの計算
    players, setting = get_pot(players, setting)

    while(Redo_Flag):
        
        Redo_Flag, players, setting, backup_play, backup_set = run_poker(Redo_Flag, players, setting, backup_play, backup_set)
        
        #一度もレイズされずbbに回った場合レイズする権利がある
        if players[setting.turn].betting == setting.sb_value*2 and setting.first_bb == True:
            Redo_Flag = True
            setting.set_first_bb(False)

        #何人残っているか確認する
        Redo_Flag = GetFunc.remain_count(Redo_Flag, players)

        #終わってよいか確認する
        if Redo_Flag == False:
            Redo_Flag, players, setting, backup_play, backup_set = GetFunc.check_comfirm(Redo_Flag, players, setting, backup_play, backup_set)
                


    #フロップに参加した人への処理
    for i in range(len(players)):
        if players[i].status != status.Folded and players[i].status != status.Blind and players[i].status != status.Waiting:
            players[i].add_log_join()

    #フェイズの後処理    
    return clean_up_phase(players, setting) 


def common(players:List[infor.Player], setting:infor.Setting, phase_name:str)-> Tuple[List[infor.Player],infor.Setting]:
    """ゲーム共通の処理

    Args:
        players (List[infor.Player]): 
        setting (infor.Setting):
        phase_name (str):

    Returns:
        Tuple[List[infor.Player],infor.Setting]:
    """

    #Wfoldとallinの人数を数える
    waiting_count = GetFunc.status_count(players, status.Waiting)

    #wating状態が一人以下の場合この処理を飛ばす
    if waiting_count  <= 1:
        return players, setting
            
    print("/////////////////")
    print("Now it's",phase_name)
    print("/////////////////")
    print("")

    #Smallblindからはじまる
    for i in range(len(players)):
        if players[i].position == position.SmallBlind:
            setting.set_turn(i)

    Redo_Flag = True
    backup_play = copy.deepcopy(players)
    backup_set = copy.deepcopy(setting)

    while(Redo_Flag):
        Redo_Flag, players, setting, backup_play, backup_set = run_poker(Redo_Flag, players, setting, backup_play, backup_set)
        #何人残っているか確認する
        Redo_Flag = GetFunc.remain_count(Redo_Flag, players)
        #終わってよいか確認する
        if Redo_Flag == False:
            Redo_Flag, players, setting, backup_play, backup_set = GetFunc.check_comfirm(Redo_Flag, players, setting, backup_play, backup_set)


    return  clean_up_phase(players, setting) 


def showdwon_or_autowin(players:List[infor.Player], setting:infor.Setting)-> Tuple[List[infor.Player], infor.Setting]:
    """ショウダウンか自動勝利

    Args:
        players (List[infor.Player]): 
        setting (infor.Setting): 

    Returns:
        Tuple[List[infor.Player], infor.Setting]: 
    """
    #foldの人数を数える
    waiting_list = []
    allin_list = []
    fold_list = []
    fold_index = [0 for i in range(len(players))]

    for i in range(len(players)):
        if players[i].status == status.Folded:
            fold_list.append(i)
            fold_index[i] = 1
        if players[i].status == status.Allin:
            allin_list.append(i)
        if players[i].status == status.Waiting:
            waiting_list.append(i)

    #allin状態かwaiting状態が一人の場合autowinの処理
    if len(players) - len(fold_list) == 1:
        if len(waiting_list) == 1:
            winner_index = waiting_list[0]
        if len(allin_list) == 1:
            winner_index = allin_list[0]
        print("Winnner is",players[winner_index].name)
        print("Get pot $",setting.main_pot)
        players[winner_index].win(setting.main_pot)
        #過去の誰よりも一番多くチップを多く持っていたら更新
        if players[winner_index].cip > setting.most_cip_ever:
            setting.set_most_cip_ever(players[winner_index].cip)
        
    #そうでない場合、showdownを行う
    else:
        for i in range(len(players)):
            if fold_index[i] == 0:
                print(players[i].name," is ", i)
        
        print("Who won?")
        winner_index = InFunc.winner(fold_index)
        
        #オールインした時の場合とそうでない場合
        pot = 0
        if len(allin_list) != 0:
            while(1):
                tmp_box = players[winner_index].personal_bet
                #全員の賭けた額から勝った人が賭けた金額を引く
                for i in range(len(players)):
                    if players[i].personal_bet < tmp_box:
                        pot += players[i].personal_bet
                        setting.set_main_pot(setting.main_pot-players[i].personal_bet)
                        players[i].set_personal_bet(0)
                    else:
                        pot += tmp_box
                        setting.set_main_pot(setting.main_pot-tmp_box)
                        players[i].set_personal_bet(players[i].personal_bet-tmp_box)
                    if players[i].personal_bet == 0:
                        fold_index[i] = 1

                players[winner_index].win(pot)
                #過去の誰よりも一番多くチップを多く持っていたら更新
                if players[winner_index].cip > setting.most_cip_ever:
                    setting.set_most_cip_ever(players[winner_index].cip)
                print(players[winner_index].name," get $",pot)
                if setting.main_pot == 0:
                    break

                pot = 0
                print("Who next won?")
                winner_index = InFunc.winner(fold_index)

        else:
            print("Winnner is",players[winner_index].name)
            print("Get pot $",setting.main_pot)
            players[winner_index].win(setting.main_pot)
            #過去の誰よりも一番多くチップを多く持っていたら更新
            if players[winner_index].cip > setting.most_cip_ever:
                setting.set_most_cip_ever(players[winner_index].cip)

    return clean_up_round(players, setting)

import random
import time

honest_list = ['最喜欢在座哪位异性？',
            '愿意为爱牺牲到什么程度？',
            '做过最丢人的事情是什么？',
            '如果在这群人里选一个人结婚，你选谁？',
            '你想做而不敢做的事情是什么？']
brave_list = ['抓着铁门大喊，放我出去！',
            '深情地吻墙10秒',
            '绕指定地点跑一圈，边跑边喊，我再也不尿床了',
            '做一个大家都满意的鬼脸',
            '模仿脑白金广告，边跳边唱',
            '对外面大喊“我好寂寞啊”']

def choice_honest():
    '''选择诚实时的惩罚'''
    punishment_h = random.choice(honest_list)
    print('-'*40)
    print(punishment_h)
    print('-'*40)

def choice_brave():
    '''选择勇敢时的惩罚''' 
    punishment_b = random.choice(brave_list)
    print('-'*50)
    print(punishment_b)
    print('-'*50)   

def add_player():
    '''确定参与者'''
    players_list = []
    print('-'*30 + '准备迎接诚实勇敢的挑战吧' + '-'*30)
    while True:
        name = input('请输入参与者姓名(退出输入n)：')
        if name == 'n':
            break
        players_list.append(name)
        time.sleep(0.5)
    return players_list

def choice_player(players):
    '''抽取玩家'''
    players_list = players
    punished_player = random.choice(players_list)
    time.sleep(1)
    print(' ')
    print('被抽中的玩家是【{}】 ╮(￣▽ ￣)╭'.format(punished_player))
    print(' ')
    player_choice = input('{}选择  1.诚实  2.勇敢（输入数字）：'.format(punished_player))
    time.sleep(1)
    if player_choice == '1':
        choice_honest()
    elif player_choice == '2':
        choice_brave()
    else:
        print('没有其他选项，接受惩罚吧')
        choice_brave()

def main():
    players = add_player()
    while True:
        choice_player(players)
        twich = input('重新开始游戏按回车，退出游戏输入n：')
        if twich == 'n':
            break

main()

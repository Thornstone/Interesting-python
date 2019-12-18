'''
制作简单狼人杀
'''

import random 
'''
简单版狼人杀
'''

import time

# start ----------------------------------- 游戏规则介绍 ----------------------------------- start
ID_list = ['村民','猎人','狼人']
ID_dict = {'1':'村民','2':'猎人','3':'狼人'}
print('欢迎来到狼人杀游戏')
time.sleep(1)
print('选择你的身份，然后抽取卡片')
time.sleep(1)
print('''
村民遇到猎人获得胜利，村民遇到狼人被击杀
猎人遇到狼人获得胜利，猎人遇到农民狼逃跑
狼人遇到村民获得胜利，狼人遇到猎人被击杀
''')
time.sleep(1)
print('-'*30)
time.sleep(1)
#   end ----------------------------------- 游戏规则介绍 ----------------------------------- end


# start ----------------------------------- 开始游戏 ----------------------------------- start
User_Choice = input('''1.【村民】  2.【猎人】  3.【狼人】
选择你的身份（输入数字）:''')
User_ID = ID_dict[User_Choice]
print('你选择的身份是【{}】'.format(User_ID )+ '\n')
time.sleep(1)
card_choice = input('''1.【♠】 2.【♥】 3.【♣】
抽取上面卡片（输入数字）:''')
Computer_Choice_ID = random.choice(ID_list)
time.sleep(0.5)
result = input('按回车查看结果' + '\n')
if User_ID == Computer_Choice_ID:
    print('没想到，对方也是【{}】，一起抱团取暖'.format(Computer_Choice_ID))
elif User_ID == ID_list[ID_list.index(Computer_Choice_ID)-1]:
    print('恭喜你，你遇到了【{}】，获得了胜利'.format(Computer_Choice_ID))
else:
    print('很遗憾，你遇到了【{}】，战役失败了'.format(Computer_Choice_ID))
time.sleep(0.5)
print('-'*30)
#   end ----------------------------------- 开始游戏 ----------------------------------- end

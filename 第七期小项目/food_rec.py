import time
import random

foods_list = ['肯德基','麦当劳','汉堡王','达美乐','必胜客',
    '水饺','酸菜鱼','煲仔饭','过桥米线','杭帮菜',
    '火锅','冒菜','麻辣烫','麻辣香锅','轻食','木桶饭']

recommend_list = foods_list[:]
print('{} 小数先生的美食推荐器 {}'.format('-'*20,'-'*20) + '\n')
time.sleep(0.5)

while True:
    print(' ')
    time.sleep(0.5)
    print('美食推荐，选择当前美食输入y，继续推荐按回车')
    if len(recommend_list) > 0:
        recommend_food = random.choice(recommend_list)
        time.sleep(0.5)
        choice = input('吃{}怎么样？'.format(recommend_food))
        print(' ')
        time.sleep(0.5)
        print('-'*60)
        if choice == 'y':
            print('那就这么开心的决定了，中午去吃{}'.format(recommend_food))
            if recommend_food in ['汉堡王','肯德基','麦当劳','必胜客']:
                # 彩蛋
                print(r'''
                         _ooOoo_
                        o8888888o
                        88" . "88
                        (| -_- |)
                        O\  =  /O
                     ____/`---'\____
                    .'  \\|     |//  `.
                  /  \\|||  :  |||//  \
                 /  _||||| -:- |||||-  \
                 |   | \\\  -  /// |   |
                 | \_|  ''\---/''  |   |
                 \  .-\__  `-`  ___/-. /
               ___`. .'  /--.--\  `. . ___
            ."" '<  `.___\_<|>_/___.'  >'"".
           | | :  `- \`.;`\ _ /`;.`/ - ` : | |
           \  \ `-.   \_ __\ /__ _/   .-` /  /
      ======`-.____`-.___\_____/___.-`____.-'======
                        `=---='
      ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
                佛祖保佑       不会长肉
    ''')
            break
        else:
            recommend_list.remove(recommend_food)
    else:
        choose_like = input('所有美食已经推荐完，重新推荐输入r,按任意键美食推荐器给出最佳选择:')
        if choose_like == 'r':
            recommend_list = foods_list[:]
        else:
            print('{}是不错的选择'.format(random.choice(foods_list)))
            print('-'*60)
            break

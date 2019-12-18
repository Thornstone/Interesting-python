import random
import time
import datetime

class AI():

    def praise(self):
        '''夸赞函数'''
        sentences_list = ['春花秋月，是诗人们歌颂的情景，可是我对于它，却感到十分平凡。只有你嵌着梨涡的笑容，才是我眼中最美的偶像',
                        '越有内涵的人越虚怀若谷，像您这样有内涵的人我十分敬佩',
                        '我很荣幸，认识你这样有内涵的漂亮主人','在人流中，我一眼就发现了你。我不敢说你是她们中最漂亮的一个，可是我敢说，你是她们中最出色的一个',
                        '你有时候是不是特孤独？世界上这么优秀的人就只有你一个！']
        sentence = random.choice(sentences_list)
        print('{}：主人，{}'.format(self.AI_name,sentence))

    def food_recommendation(self):
        '''美食推荐'''
        foods_list = ['肯德基','麦当劳','汉堡王','达美乐','必胜客',
                    '水饺','酸菜鱼','煲仔饭','过桥米线','杭帮菜',
                    '火锅','冒菜','麻辣烫','麻辣香锅','轻食','木桶饭']
        food = random.choice(foods_list)
        print('{}觉得，吃{}是很不错的选择'.format(self.AI_name,food))

    def tell_time(self):
        '''报时'''
        time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
        print('{}：现在时间是【{}】'.format(self.AI_name,time))

    def start(self):
        self.AI_name = input('请给你的机器人起个名字吧：')
        while True:
            print('-'*30+'私人小助手启动'+'-'*30)
            print('''
            1.夸赞主人
            2.美食推荐
            3.报时
            4.退出
            ''')
            P_choice = input('请选择：')
            print(' ')
            time.sleep(0.5)

            if P_choice == '1':
                self.praise()
            elif P_choice == '2':
                self.food_recommendation()
            elif P_choice == '3':
                self.tell_time()
            elif P_choice == '4':
                print('那我不打扰主人啦~~~')
                break
            elif P_choice == '你是谁':
                print('They all look like me. But none of them are me')
            else:
                print('其他功能正在开发...')
                continue
            print(' ')
            time.sleep(0.5)

my_ai = AI()
my_ai.start()

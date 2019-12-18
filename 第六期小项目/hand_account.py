'''
知识手账
'''

import time

# start ----------------------------------- 封装知识 ----------------------------------- start
#字典封装,内容可自定义
notes = {
    '数字':'Python数字类型用于存储数值',
    '字符串':'字符串是Python中最常用的数据类型。可以使用单引号或双引号来创建字符串',
    '列表':'列表由一系列按特定顺序排列的元素组成。用方括号[]来表示，用逗号来分隔其中的元素',
    '元组':'元组使用小括号(),元素之间用逗号隔开',
    '集合':'集合(set)是一个无序的不重复元素列表',
    '字典':'Python中字典是一种可变容器模型，且可储存任意类型对象，具有极快的查找速度，如字符串、数字、元组等'
}
#   end ----------------------------------- 封装知识 ----------------------------------- end


print('小数先生的手账') 
time.sleep(1)
switch = True #设置循环开关

while switch:
    print('-'*40) 
    question = input('想查询Python哪个数据类型？') #记录查询内容
    for note in notes:
        if question in note:          
            try:
                answer = notes[question]
                print('\n' + answer)
                print('-'*40 + '\n') 
            except:
                print('输入信息有误')
                print('-'*40 + '\n') 
    
    time.sleep(1)
    choice = input('继续查询按回车，输入q退出')
    if choice == 'q': #用户输入q，结束while循环
        switch = False
        
print('手账查询结束')

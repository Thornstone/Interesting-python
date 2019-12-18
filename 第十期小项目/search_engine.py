# 根据输入的关键词查询文档内匹配字段

file_adress = input('输入查询文档绝对路径：')
file = open(r'{}'.format(file_adress),'r',encoding='gbk')
print('-'*30+'文档搜索引擎'+'-'*30+'\n')
file_lines = file.readlines()

while True:
    employee_name = input('输入员工姓名,即可查询工资：') # 查询关键词
    for file_line in file_lines:
        if employee_name in file_line:
            print(file_line)
    p_choice = input('【1】继续查询  【2】退出：')
    print(' ')
    if p_choice == '2':
        break
print('-'*30+' 搜 索 结 束 '+'-'*30)
file.close()

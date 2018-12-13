# coding:utf-8

import os, sys


dir = os.path.abspath(os.path.dirname(__file__))
# opts, args = getopt.getopt(sys.argv[1:], '-p:-m:')
print(dir)
# try:
#     project_name = sys.argv[1]
# except Exception as e:
#     print('参数错误')
#     sys.exit()
#
# if project_name == '':
#     print('请输入项目名称')
#     sys.exit()


def mkdir(path):
    isExists = os.path.exists(path)

    if not isExists:
        os.makedirs(path)
        print(path, '创建成功')
        return True
    else:
        print(path, '目录已存在')
        return False

project_name = '01'

path = dir + '/' + project_name + '/'
dirlist = ['common', 'module', 'config']

for i in dirlist:
    if i in ['module' or 'config']:
        i_dir = path + i
        mkdir(i_dir)
        initname = i_dir + '/' + '__init__.py'
        with open(initname) as f:
            print('创建成功')
    else:
        i_dir = path + i
        mkdir(i_dir)




# for op, value in opts:
#     if op == '-p':
#         project_name = value
#     elif op == '-m':
#         module_name = value

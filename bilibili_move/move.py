import os
import shutil
import sys

# 获得该p视频的名称
def get_name(file_name):
    f = open(file_name, 'r', encoding = 'utf-8')    #用utf8编码打开文件
    tt = 123
    for each in range(5000):        #查找PartName关键字
        try:
            tt = f.read(8)
            if(tt != 'PartName'):
                f.seek(each, 0)
            else:
                break
        except UnicodeDecodeError:          #忽略问题，可能是由编码产生的问题，但不知道是为什么产生
            pass
    each_begin = each + 10          #获得名称最开始的位置
    f.seek(each_begin, 0)           #到达最开始名称的位置
    for each in range(50):          #获得名称最后结束的位置
        try:
            if(f.read(1) != '"'):
                pass
            else:
                break
        except UnicodeDecodeError:
            pass
    f.seek(each_begin, 0)       #再次到达名称最开始的地方
    part_name = f.read(each)    #读取名称
    return part_name

file_dir = os.getcwd()  #获得当前路径
for each in range(100):
    try:
        dir_name = file_dir + "\\" + str(each)  #获得要进入的文件路径
        filenameflv = os.path.basename(file_dir) + "_" + str(each) +"_0.flv"    #获得视频文件名
        file_name = os.path.basename(file_dir)  #获得info名
        os.chdir(dir_name)  #进入文件
        shutil.move(filenameflv, "..")  #移动视频文件
        file_name = file_name + '.info'
        part_name = get_name(file_name) #得到视频文件名
        os.chdir(file_dir)
        shutil.rmtree(str(each))        #删除多余文件
        part_name = part_name + '.flv'
        print(part_name)
        os.rename(filenameflv, part_name)   #重命名
        print("转移" + str(each) + "成功")
    except FileNotFoundError:
        print('转移'+ str(each) +'失败')
input()

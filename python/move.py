import os
import shutil
import sys

def get_name(file_name):
    f = open(file_name, 'r', encoding = 'utf-8')
    tt = 123
    for each in range(5000):
        try:
            tt = f.read(8)
            if(tt != 'PartName'):
                f.seek(each, 0)
            else:
                break
        except UnicodeDecodeError:
            pass
    each_begin = each + 10
    f.seek(each_begin, 0)
    for each in range(50):
        try:
            if(f.read(1) != '"'):
                pass
            else:
                break
        except UnicodeDecodeError:
            pass
    f.seek(each_begin, 0)
    part_name = f.read(each)
    return part_name

file_dir = os.getcwd()
for each in range(100):
    try:
        dir_name = file_dir + "\\" + str(each)
        filenameflv = os.path.basename(file_dir) + "_" + str(each) +"_0.flv"
        file_name = os.path.basename(file_dir)
        os.chdir(dir_name)
        shutil.move(filenameflv, "..")
        file_name = file_name + '.info'
        part_name = get_name(file_name)
        os.chdir(file_dir)
        shutil.rmtree(str(each))
        part_name = str(each) + part_name + '.flv'
        print(part_name)
        os.rename(filenameflv, part_name)
        print("转移" + str(each) + "成功")
    except FileNotFoundError:
        print('转移'+ str(each) +'失败')
input()

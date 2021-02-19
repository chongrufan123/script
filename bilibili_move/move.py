import os
import shutil
import sys
file_dir = os.getcwd()
for each in range(100):
    dir_name = file_dir + "\\" + str(each)
    try:
        filenameflv = os.path.basename(file_dir) + "_" + str(each) +"_0.flv"
        os.chdir(dir_name)
        shutil.move(filenameflv, "..")
        os.chdir(file_dir)
        shutil.rmtree(str(each))
        os.rename(filenameflv, str(each) + ".flv")
        print("转移" + str(each) + "成功")
    except:
        print("转移" + str(each) + "失败") 
    
input()

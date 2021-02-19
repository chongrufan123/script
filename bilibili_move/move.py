import os
import shutil
import sys
file_dir = os.getcwd()
for each in range(100):
    dir_name = file_dir + "\\" + str(each)
    try:
        filenameflv = os.path.basename(file_dir) + "_" + str(each) +"_0.flv"
        filenamemp4 = os.path.basename(file_dir) + "_" +str(each) + "_0.mp4"
        os.chdir(dir_name)
        try:
            shutil.move(filenameflv, "..")
        except:
            shutil.move(filenamemp4, "..")
        finally:
            os.chdir(file_dir)
            shutil.rmtree(str(each))
            print("转移" + filename + "成功")
    except:
        print("转移" + filename + "失败") 
    
input()

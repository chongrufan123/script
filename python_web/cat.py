###************************************************************************
	# File Name: code1_0.py
	# Author: Fan Chongru
	# Mail: chongrufan123@gmail.com
	# Created Time: 2021年03月04日 星期四 12时03分17秒
  # notes: 
###***********************************************************************

import urllib.request as urlreq
import easygui as g

def main():
    while 1:
        fieldNames = ["长", "宽"]
        title = '下载一只瞄'
        msg = '请填写瞄的尺寸,默认600*400'
        fieldvalue = []
        fieldvalue = g.multenterbox(msg, title, fieldNames)
        for each in range(2):
            try:
                aa = int(fieldvalue[each])
            except ValueError:
                fieldvalue[each] = 600 if each else 400

        url = "http://placekitten.com/g/" + str(fieldvalue[1]) + "/" + str(fieldvalue[0])
        cat_image = urlreq.urlopen(url).read()
        filepath = g.diropenbox("请选择存放喵的文件夹")

        msg2 = '请输入下载的文件名称'
        filename = g.enterbox(msg2, title)
        if filepath:
            filename = filepath + '//' + filename + '.jpg'
        else:
            filename = filename + '.jpg'

        with open(filename, 'wb') as f:
            f.write(cat_image)
        if g.ccbox("下载完成, 还要继续下载吗", choices=("继续", "不了")):
            pass
        else:
            break
            
if __name__ == "__main__":
    main()



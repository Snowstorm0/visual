
import os

path = "E:\\0WeiYun\\Program\\OTB\\recent_result\\CFNet\\"

# 获取该目录下所有文件，存入列表中
filelist = os.listdir(path)

n = 0
for i in filelist:
    # 设置旧文件名（就是路径+文件名）
    oldname = path + os.sep + filelist[n]  # os.sep添加系统分隔符

    # 设置新文件名
    # newname = path + os.sep + filelist[n][4:-4] + "_ECO.mat"  # 截取4到-4个字符串
    newname = path + os.sep + filelist[n][:-11] + "_CFNet.mat"  # 截取4到-4个字符串

    os.rename(oldname, newname)  # 用os模块中的rename方法对文件改名
    print(oldname, '======>', newname)

    n += 1


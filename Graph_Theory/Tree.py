from os import listdir
from os.path import isfile, join

#根目录入口
def printname(Start_dir):
    try:
        files = sorted(listdir(Start_dir))
    except:
        print('no permission' + Start_dir)
        return
    for file in files:
        full_path = join(Start_dir,file)
        if isfile(full_path):
            print(full_path)
        else:
            printname(full_path)

#当根目录传入进来，会检查会不会操作系统卡权限，如果不卡，会将文件和文件夹每个目录合并起来，并且打印出来.可是如果不是文件的话，就继续往下一层目录继续找
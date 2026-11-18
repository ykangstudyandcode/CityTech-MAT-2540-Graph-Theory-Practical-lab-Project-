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



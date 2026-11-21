from collections import deque
def MoringToDoMoring(Todo):
    return Todo == '穿衣服'

def Moring():
    morning = {}
    morning['起床'] = ['刷牙','打包早饭','锻炼']
    morning['刷牙'] = ['吃早饭']
    morning['锻炼'] = ['洗澡']
    morning['洗澡'] = ['穿衣服']
    #创建队列
    search_queue = deque()
    #将队列开头
    search_queue += morning['起床']

    while search_queue:
        Todo = search_queue.popleft()
        print(Todo)
        if MoringToDoMoring(Todo):
            print(Todo + " 结束后出发上学")
            return True
        if Todo in morning:
            search_queue += morning[Todo]
    return False
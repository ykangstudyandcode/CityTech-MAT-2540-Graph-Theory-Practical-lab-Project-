from collections import deque

def person_is_seller(name):
    return name[-1] == 'm'
def search():
    graph = {}
    graph['you'] = ['bob','alice','claire']
    graph['bob'] = ['anuj','peggy']
    graph['alice'] = ['peggy']
    graph['claire'] = ['thom','jonny']
    graph['anuj'] = []
    graph['peggy'] = []
    graph['thom'] = []
    graph['jonny'] = []
    search_queue = deque()
    search_queue += graph ['you']
    searched = set()


    while search_queue:
        #将从you开始，因为我在搜索队列里面放置的第一个元素是you
        #从you开始，去检查每一个元素里是否有名字结尾为m的人
        person=search_queue.popleft()
        print(person)
        #为了防止重复检查 检查这个人是否已经被标已检查
        if person not in searched:
            if person_is_seller(person):
                print(person + " is seller")
                return True
            else:
                search_queue += graph[person]
                searched.add(person)
    return False
import math
def dijksra():
    graph = {}
    graph['start']["a"] =6
    graph['start']["b"] =2

    graph['a'] = {}
    graph['a']['fin'] = 1

    graph['b'] = {}
    graph['b']['fin'] = 5

    graph['fin'] = {}

    infinity = math.inf
    cost = {}
    cost['a'] = 6
    cost['b'] = 2
    cost['fin'] = infinity

    parents = {}
    parents['a'] = 'start'
    parents['b'] = 'start'
    parents['fin'] = 'None'

    processed = set()



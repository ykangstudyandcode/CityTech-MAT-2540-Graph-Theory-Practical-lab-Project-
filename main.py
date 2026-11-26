from asyncio import graph

from Graph_Theory import printname


#printname('D:/')


import math
#This is an adjacency list, which represents the nodes that each point can connect to, along with the associated weights.
graph = {
    'start': {'a': 5, 'b': 2},
    'a': {'start': 5, 'c': 2, 'd': 6},
    'b': {'start': 2, 'c': 4},
    'c': {'a': 2, 'd': 1, 'b': 4, 'end': 10},
    'd': {'a': 6, 'c': 1, 'end': 3},
    'end': {'d': 3, 'c': 10}
}

# Initialize the weights for each node from start to end.
costs = {
    'start': 0,
    'a': math.inf,
    'b': math.inf,
    'c': math.inf,
    'd': math.inf,
    'end': math.inf
}

parents={}
parents['a']='start'
parents['b']='start'
parents['c']=None
parents['d']=None
parents['end']=None

processed=set()

#Use a greedy algorithm to first find the shortest path.
def find_shortest_path(costs):
    lowest_cost = math.inf
    shortest_node = None
    for node in costs:
        if costs[node] < lowest_cost and node not in processed:
            lowest_cost = costs[node]
            shortest_node = node
    return shortest_node

node=find_shortest_path(costs)
while node is not None:
    cost=costs[node]
    neighbors=graph[node]
    for n in neighbors.keys():
        new_cost = cost + neighbors[n]
        if new_cost < costs[n]:
            costs[n] = new_cost
            parents[n] = node
    processed.add(node)
    node = find_shortest_path(costs)

print(costs)

path = ['end']
node = 'end'
while node != 'start':
    node = parents[node]
    path.append(node)

path.reverse()
print(path)

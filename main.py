import math
from Graph_Theory import printname

#printname('D:/')

#This is an adjacency list, which represents the nodes that each point can connect to, along with the associated weights.
graph={}
graph['start']={}
graph['start']['a'] =5
graph['start']['b'] = 2

graph['a']={}
graph['a']['start'] = 5
graph['a']['c']=2
graph['a']['d']=6

graph['b']={}
graph['b']['start'] = 2
graph['b']['c']=4

graph['c']={}
graph['c']['a']=2
graph['c']['d']=1
graph['c']['b']=4
graph['c']['end']=10

graph['d']={}
graph['d']['a']=6
graph['d']['c']=1
graph['d']['end']=3

graph['end']={}
graph['end']['d']=3
graph['end']['c']=10



costs={}
costs['start']=0
costs['a']=5
costs['b']=2
costs['c']=math.inf
costs['d']=math.inf
costs['end']=math.inf


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
    #A hash map recording the nodes adjacent to this node at the current moment
    neighbors=graph[node]
    #Iterate through the key-value pairs of this hash map; `n` will point to the key-value of each current node.
    print(f"\nCurrent node: {node}, total cost: {cost}")
    for n in neighbors.keys():
        print(f"Checking: {node} -> {n}")
        new_cost = cost + neighbors[n]
        if new_cost < costs[n]:
            costs[n] = new_cost
            parents[n] = node
    processed.add(node)
    node = find_shortest_path(costs)

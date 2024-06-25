import itertools
graph = {'A': {'B': 10, 'C': 15, 'D': 20, 'E': 25, 'F': 30}, 'B': {'A': 10, 'C': 35, 'D': 25, 'E': 20, 'F': 15}, 'C': {'A': 15, 'B': 35, 'D': 30, 'E': 20, 'F': 10}, 'D': {'A': 20, 'B': 25, 'C': 30, 'E': 35, 'F': 25}, 'E': {'A': 25, 'B': 20, 'C': 20, 'D': 35, 'F': 15}, 'F': {'A': 30, 'B': 15, 'C': 10, 'D': 25, 'E': 15}}
possibilites=itertools.permutations(["B","C","D","E","F"])
mincost,minpath=float('inf'),float('inf')
for i in possibilites:
    new_cost=graph['A'][i[0]]+graph[i[0]][i[1]]+graph[i[1]][i[2]]+graph[i[2]][i[3]]+graph[i[3]][i[4]]+graph[i[3]]['A']
    if new_cost<mincost:
        mincost,minpath=new_cost,i
print(mincost,tuple('A')+minpath+tuple('A'))
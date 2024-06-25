graph={}
vertices=int(input("Enter the number of vertices: "))
for i in vertices:
    vertex=input(f"Enter the vertex {i+1}: ")
    graph[vertex]=list(map(str,input("Enter neighbours of vertex {vertex} with spaces: ").split()))
visited=set()
start=input("Enter starting node: ")
queue=[start]
while queue:
    node=queue.pop(0)
    print(node,end=" ")
    if node not in visited:
        visited.add(node)
        for i in graph[node]:
            if i not in queue and i not in visited:
                queue.append(i)
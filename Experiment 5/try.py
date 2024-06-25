graph={}
vertices=int(input("Enter the number of vertices: "))
for i in range(vertices):
    vertex=input(f"Enter the vertex {i+1}: ")
    graph[vertex]=list(map(str,input("Enter the connected vertex {vertex} seperated by spaces: ").split()))
visited=set()
start=input("Enter the starting node: ")
queue=[start]
while queue:
    node=queue.pop()
    print(node,end=" ")
    if node not in visited:
        visited.add(node)
        for i in graph[node]:
            if i not in visited and i not in queue:
                queue.append(i)
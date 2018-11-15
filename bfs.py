adj_list=[[1,2],[2,3],[4],[],[]]
v=[0 for i in range(len(adj_list))]
start=0
queue=[start]
v[start] = 1
bfs=[]
while queue:
    a=queue.pop(0)
    bfs.append(a)

    for node in adj_list[a]:
        if(v[node]==0):
            queue.append(node)
            v[node]=1
print(bfs)

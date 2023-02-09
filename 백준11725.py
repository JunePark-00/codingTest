#root: 1
N = int(input())
graph = [[] for i in range(N+1)]
visited = [0]*(N+1)
for i in range(N-1):
    a,b = map(int,input().split())
    graph[a].append(b)
    graph[b].append(a)
print(graph)
def dfs(s):
    for i in graph[s]:
        if visited[i]==0:
            visited[i]=s
            print(visited)
            dfs(i)
dfs(1)

for i in range(2,N+1):
    print(visited[i])
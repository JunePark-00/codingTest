n, m = map(int, input().split())
s = list(map(int, input().split()))
s.sort()
s2 = []
visited = [False]*n


def dfs():
    if len(s2) == m:
        print(' '.join(map(str, s2)))
        return

    for i in range(n):
        if not visited[i]:
            s2.append(s[i])
            visited[i] = True
            dfs()
            #print(s2)
            visited[i] = False
            s2.pop()
            #print(s2)


dfs()
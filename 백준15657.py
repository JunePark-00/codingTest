from itertools import combinations_with_replacement

n,m = map(int,input().split())
s = list(map(int,input().split()))
s.sort()
s2 = []

for i in combinations_with_replacement(s, m):
    s2.append(i)

for j in s2:
    print(' '.join(map(str,j)))
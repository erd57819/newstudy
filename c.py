n,m = map(int,input().split())
lst = []
for i in range(1,n+1):
    lst.append(i)
for i in range(m):
    a,b = map(int,input().split())
    lst[a-1],lst[b-1] = lst[b-1],lst[a-1]
print(' '.join(map(str,lst)))


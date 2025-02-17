def dfs(i):
    stack = []
    visited = [False]*(n+1)
    stack.append(i)
    while stack: # stack에 데이터가 있는 경우 == len(stack)>0
        v = stack.pop()
        # stack에서 pop한것을 사용한다
        if not visited[v]:
            visited[v] = True
        for w in g[v]:
            if not visited[w]:
                stack.append(w)


lst = [1,2,1,3,2,4,2,5,4,6,5,6,6,7,3,7]
n = 7
g=[[] for _ in range(n+1)]
for i in range(0,len(lst),2):
    p1 = lst[i]
    p2 = lst[i+1]
    g[p1].append(p2) 
    g[p2].append(p1)
# 단순 버전
def dfs(i):
    stack = []
    visited = [False]*(n+1)

    stack.append(i)
    visited[i] = True
    while stack: # stack에 데이터가 있는 경우 == len(stack)>0
        v = stack.pop()
        for w in g[v]:
            if not visited[w]:
                stack.append(w)
                visited[w] =True

# 제귀버전
# visited = [False]*(n+1)
def dfs_r(v):
    print(v)
    visited[v] =True

    for w in g[v]:
        if not visited[w]:
            dfs_r(w)

dfs(1)
visited = [False]*(n+1)
dfs_r(1)
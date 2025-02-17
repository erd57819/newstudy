t = int(input())  
for tc in range(1, t + 1):
    v, e = map(int, input().split())
    g = [[] for _ in range(v+1)]  
    for _ in range(e):
        u, c = map(int, input().split())  
        g[u].append(c)
    s, g = map(int, input().split())  
    def dfs(i,g):
        stack = []
        visited = [False]*(v+1)
        stack.append(i)
        visited[i] = True
        while stack: # stack에 데이터가 있는 경우 == len(stack)>0
            v = stack.pop()
            if v == g:
                return 1
            for w in g[v]:
                if not visited[w]:
                    stack.append(w)
                    visited[w] =True
        return 0
    print(f'#{tc} {dfs(s,g)}')
    
 
    
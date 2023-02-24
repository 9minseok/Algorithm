def bfs(S, G ,adj):
    visited = [0] * (V+1)   # visited 생성
    q = []                  # 큐 생성
    q.append(S)             # 시작점 인큐
    visited[S] = 1          # 시작점 인큐표시
    while q:                # 큐가 비어있지 않으면
        t = q.pop(0)            # 디큐
        for v in adj[t]:       # t에 인접이고 방문한 적 없는 v
            if not visited[v]:
                q.append(v)     # v 인큐
                visited[v] = visited[t] + 1  # v 인큐되었음 표시
    return 0 if visited[G] == 0 else visited[G] - 1

T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adjL = [[] for _ in range(V+1)]
    for i in range(E):
        n1, n2 = map(int, input().split())
        adjL[n1].append(n2)
        adjL[n2].append(n1)
    S, G = map(int, input().split())

    print(f'#{tc} {bfs(S, G, adjL)}')
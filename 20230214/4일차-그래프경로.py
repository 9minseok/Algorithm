T = int(input())

def dfs(S, G):
    stack = []
    stack.append(S)

    while stack:
        v = stack.pop()
        if visited[v] == 0:            # 방문한적 없다면
            visited[v] = 1             # 방문
            for w in range(1, V + 1):  # 인접 노드 순회
                if graph[v][w] == 1 and visited[w] == 0:    # 노선이 연결 & 방문한적없음
                    if w == G:
                        return 1
                    stack.append(w)
    return 0

for tc in range(1, T+1):
    V, E = map(int, input().split()) # V개 정점, E개의 간선
    visited = [0] * (V+1)
    graph = [[0] * (V+1) for _ in range(V + 1)]

    for _ in range(E):
        i, j = map(int, input().split())
        graph[i][j] = 1
    S, G = map(int, input().split())
    print(f'#{tc} {dfs(S,G)}')
import pprint

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

for _ in range(10):
    V = 100
    tc, E = map(int, input().split())
    visited = [0] * (V + 1)
    graph = [[0] * (V + 1) for _ in range(V + 1)]
    li = list(map(int, input().split()))
    for i in range(0, len(li), 2):
        i, j = li[i], li[i+1]
        graph[i][j] = 1

    print(f'#{tc} {dfs(0,99)}')
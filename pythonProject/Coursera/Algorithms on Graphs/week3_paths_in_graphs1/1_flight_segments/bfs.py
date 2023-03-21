import sys
from collections import deque


def distance(n, adj, u, v):
    '''Находит расстояние от точки u до v графа'''
    # расстояние от начальной точки до других (n + 1, чтобы начинать с индекса 1 и не заморачиваться)
    # помощь была только в использовании deque
    dist = [float('inf')] * (n + 1)
    dist[u] = 0
    queue = deque()
    queue.append(u)
    while queue:
        u = queue.popleft()
        for k in adj[u]:
            if dist[k] == float('inf'):
                queue.append(k)
                dist[k] = dist[u] + 1
    if dist[v] == float('inf'):
        return -1
    return dist[v]


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    # допер, что n - число вершин, m - число граней
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n + 1)]
    for (a, b) in edges:
        adj[a].append(b)
        adj[b].append(a)
    u, v = data[-2:len(data)]
    # нужно определить расстояние от u до v
    print(distance(n, adj, u, v))

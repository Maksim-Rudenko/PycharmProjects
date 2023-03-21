import sys
from collections import deque


def shortet_paths(n, edges, adj, s):
    dist = [float('inf')] * (n + 1)
    dist[s] = 0
    prev = [None] * (n + 1)
    negative_nodes = deque()
    for i in range(n):
        for u, v, w in edges:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                prev[v] = u
                if i == n - 1:
                    negative_nodes.append(v)

    visited = [False] * (n + 1)
    while negative_nodes:
        u = negative_nodes.popleft()
        visited[u] = True
        dist[u] = '-'
        for v in adj[u]:
            if not visited[v]:
                negative_nodes.append(v)
    return dist
    pass


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(3 * m):3], data[1:(3 * m):3], data[2:(3 * m):3]))
    # start point
    data = data[3 * m:]
    #print(data)
    #print(edges)
    adj = [[] for _ in range(n + 1)]
    for (a, b, w) in edges:
        adj[a].append(b)
    #print(adj)
    s = data[0]
    distance = shortet_paths(n, edges, adj, s)
    for dist in distance[1:]:
        if dist == float('inf'):
            print('*')
        else:
            print(dist)

'''
Input:
6 7
1 2 10
2 3 5
1 3 100
3 5 7
5 4 10
4 3 -18
6 1 -1
1

[[], [], [], [], [], [], []]
[[], [2, 3], [3], [5], [3], [4], [1]]
[(1, 2, 10), (2, 3, 5), (1, 3, 100), (3, 5, 7), (5, 4, 10), (4, 3, -18), (6, 1, -1)]
'''
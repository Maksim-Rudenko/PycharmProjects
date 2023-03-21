import sys
# вместо того, что было дано по умолчанию упростил edges и использовал
'''
def negative_cycle(adj, cost):
    Расстояние до вершин - бесконечность. 1 вершина - 0 (расст). Далее проходим по всем вершинам
    dist = [float('inf')] * (cost + 1)
    dist[1] = 0
    prev = [None] * (cost + 1)
    negative_nodes = []
    for i in range(cost):
        for u, v, w in adj:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                prev[v] = u
                if i == cost - 1:
                    negative_nodes.append(v)
    if not negative_nodes:
        return 0
    else:
        return 1


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(3 * m):3], data[1:(3 * m):3], data[2:(3 * m):3]))
    print(negative_cycle(edges, n))

'''
#Git

def BellmanFord(n, graph):
    # dist = [float('inf')] * (n + 1)
    dist = [1001] * (n + 1)
    dist[1] = 0
    prev = [None] * (n + 1)
    negative_nodes = []
    for i in range(n):
        for u, v, w in graph:
            if dist[v] > dist[u] + w:
                dist[v] = dist[u] + w
                prev[v] = u
                if i == n - 1:
                    negative_nodes.append(v)
    if not negative_nodes:
        return 0
    else:
        return 1


if __name__ == '__main__':
    n_vertices, n_edges = map(int, input().split())
    edges = []
    #print(n_vertices, n_edges)
    for i in range(n_edges):
        a, b, w = map(int, input().split())
        edges.append((a, b, w)) # (start, end, weight)
    #print(edges, 'edges')
    negative_cycle = BellmanFord(n_vertices, edges)

    print(negative_cycle)

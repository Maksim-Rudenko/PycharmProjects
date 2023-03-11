import sys


def dfs(adj, used, order, x):
    global clock
    order[used] = True
    for v in adj[used]:
        if not order[v]:
            dfs(adj, v, order, x)
    x[used] = clock
    clock += 1


def toposort(n, adj, visited, order):
    global clock
    for i in range(1, n + 1):
        if not visited[i]:
            dfs(adj, i, visited, order)
    post = list(enumerate(order[1:], start=1))
    post.sort(key=lambda x: x[1], reverse=True)
    return post


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]

    # список связей
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))

    # список связей n + 1 чтобы конкретно индекс соответсвовал номеру вершины (вершина 1 -> индекс 1)
    adj = [[] for _ in range(n + 1)]

    for (a, b) in edges:
        adj[a].append(b)

    # идея с гита как сделать: список как и для adj и по нему проходим, если зашли в какой-то индекс, то
    # помечаем, что зашли
    visited = [False] * (n + 1)

    order = [0] * (n + 1)
    clock = 1

    order = toposort(n, adj, visited, order)
    for x, post in order:
        print(x, end=' ')


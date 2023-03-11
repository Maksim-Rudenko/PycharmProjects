import sys


def explore(adj, vertex, visited, stack, is_dag):
    visited[vertex] = True
    stack.append(vertex)
    for v in adj[vertex]:
        if v in stack:
            is_dag[0] = False
        if not visited[v]:
            explore(adj, v, visited, stack, is_dag)
    stack.pop()


def acyclic(adj, visited, n):
    is_dag = [True]
    stack = []
    for i in range(1, n + 1):
        if not visited[i]:
            explore(adj, i, visited, stack, is_dag)
            if not is_dag[0]:
                return 0
    return 1


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

    check = acyclic(adj, visited, n)
    if check:
        print(0)
    else:
        print(1)



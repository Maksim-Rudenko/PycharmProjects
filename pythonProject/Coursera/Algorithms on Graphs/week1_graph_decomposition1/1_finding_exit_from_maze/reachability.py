import sys


def reach(adj, visited, x, y):
    '''заходим в массив и помечаем, что были. Проходим для всего adj, по итогу проверяем есть ли соединение'''
    visited[x] = True
    for vertex in adj[x]:
        if not visited[vertex]:
            reach(adj, visited, vertex, y)
    return 1 if visited[y] == True else 0


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    # список связей
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))

    # последняя связь, которую проверяем замкнется ли граф
    x, y = data[2 * m:]

    # список связей n + 1 чтобы конкретно индекс соответсвовал номеру вершины (вершина 1 -> индекс 1)
    adj = [[] for _ in range(n + 1)]

    # список связей между вершинами (индекс списка = вершина, содержание = с какими вершинами связана)
    for (a, b) in edges:
        adj[a].append(b)
        adj[b].append(a)

    # идея с гита как сделать: список как и для adj и по нему проходим, если зашли в какой-то индекс, то
    # помечаем, что зашли
    visited = [False] * (n + 1)
    print(reach(adj, visited, x, y))


import math

class MinimumLength:
    def __init__(self, n, edges):
        # разделяем все точки отдельно в начальные деревья (каждому свое)
        self.parent = [i for i in range(n)]
        # расстояние до
        self.rank = [0] * n
        self.edges = edges

    def Find(self, i):
        '''Возвращает какому дереву принадлежит i-я вершина'''
        if i != self.parent[i]:
            # если выбранная вершина куда-то вошла, то берем вершину к которой она присоединилась
            #  и возвращаем рекурсивно
            self.parent[i] = self.Find(self.parent[i])
        return self.parent[i]

    def Union(self, i, j):
        i_parent = self.Find(i)
        j_parent = self.Find(j)
        if i_parent == j_parent:
            # если вершины уже объединены, то ничего не делаем
            return
        else:
            if self.rank[i_parent] > self.rank[j_parent]:
                self.parent[j_parent] = i_parent
            else:
                self.parent[i_parent] = j_parent
                if self.rank[i_parent] == self.rank[j_parent]:
                    self.rank[j_parent] += 1

    def Kruskal(self):
        '''Возвращает минимальное значение длины соединенного графа (по представленным координатам точек)'''
        dist = 0
        self.edges.sort(key=lambda i: i[2])
        for u, v, w in edges:
            if self.Find(u) != self.Find(v):
                dist += w
                self.Union(u, v)
        return dist



if __name__ == '__main__':
    n = int(input())
    # список координат точек
    points = [None] * n
    for i in range(n):
        a, b = map(int, input().split())
        points[i] = (a, b)

    # список (точка_1, точка_2, расстояние_между_точка_1-точка_2)
    # указаны индексы точек в списке points
    edges = []
    for i in range(n):
        (x0, y0) = points[i]
        for j in range(i + 1, n):
            (x, y) = points[j]
            distance = math.sqrt((x - x0) ** 2 + (y - y0) ** 2)
            edges.append((i, j, distance))

    graph = MinimumLength(n, edges)
    min_length = graph.Kruskal()
    print("{0: .9f}".format(min_length))

'''
Input:
4
0 0
0 1
1 0
1 1

'''
#From git

class MinHeap:
    def __init__(self, array):
        self.A = array
        self.size = len(self.A)
        self.swaps = []


    def SiftDown(self, i):
        min_index = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < self.size and self.A[left_child] < self.A[min_index]:
            min_index = left_child

        if right_child < self.size and self.A[right_child] < self.A[min_index]:
            min_index = right_child

        if min_index != i:
            self.swaps.append((i, min_index))
            self.A[i], self.A[min_index] = self.A[min_index], self.A[i]
            self.SiftDown(min_index)

    def BuildHeap(self):
        n = self.size
        for i in range(n // 2 - 1, -1, -1):
            self.SiftDown(i)



def main():
    n = int(input())
    array = list(map(int, input().split()))
    assert len(array) == n

    heap = MinHeap(array)
    MinHeap.BuildHeap(heap)
    swaps = heap.swaps

    print(len(swaps))
    for swap in swaps:
        print(*swap)


if __name__ == "__main__":
    main()


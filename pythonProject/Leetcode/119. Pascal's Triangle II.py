class Solution:
    def getRow(self, rowIndex: int) -> list[int]:
        pascal_list_0 = [1]
        pascal_list_1 = [1, 1]
        if rowIndex > 0:
            for i in range(rowIndex - 1):
                pascal_list_0 = list(pascal_list_1)
                pascal_list_1.append(1)
                for index in range(1, i + 2):
                    pascal_list_1[index] = pascal_list_0[index - 1] + pascal_list_0[index]
            return pascal_list_1
        else:
            return pascal_list_0



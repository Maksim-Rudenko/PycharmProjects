# Дан отсортированный список целых чисел и искомое число. Вернуть индекс искомого числа в списке
# Если этого числа нет, то вернуть индекс где это число было бы, будь оно в списке
class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        find_index = 0
        if target in nums:
            find_index = nums.index(target)
        elif target < nums[-1]:
            while target > nums[find_index]:
                find_index += 1
        else:
            find_index = len(nums)
        return find_index



print(find_index)

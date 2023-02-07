class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        result = []
        for i in nums:
            if i not in result:
                result.append(i)
            else:
                result.remove(i)
        return result[0]


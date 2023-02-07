class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        sub_count = 0
        result_string = ""
        index = 0
        if strs[0] != "":
            test_letter = strs[0][index]
            while True:
                for letter in strs:
                    if letter[:index + 1] == test_letter:
                        sub_count += 1
                if sub_count == len(strs):
                    result_string = test_letter
                    sub_count = 0
                    if len(strs[0]) > index + 1:
                        index += 1
                        test_letter += strs[0][index]
                    else:
                        break
                else:
                    break
        return result_string






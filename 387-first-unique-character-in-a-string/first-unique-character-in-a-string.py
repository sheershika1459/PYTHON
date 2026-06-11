class Solution:
    def firstUniqChar(self, s: str) -> int:
        frequency_map = {}
        for char in s:
            frequency_map[char] = frequency_map.get(char, 0) + 1
        for index, char in enumerate(s):
            char = s[index]
            if frequency_map[char] == 1:
                return index
        return -1        
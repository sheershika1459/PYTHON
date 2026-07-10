class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = set()
        left = 0
        ans = 0
        for right in range(len(s)):
            if s[right] not in d:
                d.add(s[right])
            else:
                while s[right] in d:
                    d.remove(s[left])
                    left += 1
                d.add(s[right])
            ans = max(ans, right - left + 1)
        return ans
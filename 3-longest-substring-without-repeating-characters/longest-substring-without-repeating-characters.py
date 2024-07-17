class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxi = 0
        current_dict = {}
        start = 0
        for end in range(len(s)):
            if s[end] not in current_dict or current_dict[s[end]] == 0:
                current_dict[s[end]] = 1
                current = end - start + 1
                maxi = max(current, maxi)
            else:
                current_dict[s[end]] += 1
                while current_dict[s[end]] > 1:
                    current_dict[s[start]] -= 1
                    start += 1
                current = end - start + 1
                maxi = max(current, maxi)
        return maxi
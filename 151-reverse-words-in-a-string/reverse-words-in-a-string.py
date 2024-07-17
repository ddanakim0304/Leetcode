class Solution:
    def reverseWords(self, s: str) -> str:
        split_list = s.split()
        split_list = split_list[::-1]
        return ' '.join(split_list)
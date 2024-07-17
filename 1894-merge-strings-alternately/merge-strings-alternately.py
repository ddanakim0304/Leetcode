class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        solution = ''
        if len(word1) > len(word2):
            for i in range(len(word2)):
                solution += word1[i]
                solution += word2[i]
            for k in range(len(word2), len(word1)):
                solution += word1[k]
        else:
            for i in range(len(word1)):
                solution += word1[i]
                solution += word2[i]
            for k in range(len(word1), len(word2)):
                solution += word2[k]
        return solution
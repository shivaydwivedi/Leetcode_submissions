class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        res = [words[0]]  # start with the first word

        for i in range(1, len(words)):
            # compare sorted versions of current and last added word
            if sorted(words[i]) != sorted(res[-1]):
                res.append(words[i])

        return res

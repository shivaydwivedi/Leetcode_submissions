class Solution:
    def nextBeautifulNumber(self, n: int) -> int:
        def is_balanced(x: int) -> bool:
            from collections import Counter
            cnt = Counter(str(x))
            # each digit should appear exactly its own value times
            for d, f in cnt.items():
                if f != int(d):
                    return False
            return True
        
        num = n + 1
        while True:
            if is_balanced(num):
                return num
            num += 1
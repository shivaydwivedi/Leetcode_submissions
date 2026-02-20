class Solution:
    def makeLargestSpecial(self, s: str) -> str:

        n = len(s)
        if n <= 2:
            return s
        
        res = []
        balance = 0
        start = 0
        
        for i in range(n):
            if s[i] == '1':
                balance += 1
            else:
                balance -= 1
            
            if balance == 0:
                inner = self.makeLargestSpecial(s[start + 1:i])
                res.append('1' + inner + '0')
                start = i + 1
        
        res.sort(reverse=True)
        return ''.join(res)
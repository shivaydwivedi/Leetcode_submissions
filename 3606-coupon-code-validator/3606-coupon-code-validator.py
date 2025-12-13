import re

class Solution:
    def validateCoupons(self, code, businessLine, isActive):
        order = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3
        }
        
        valid = []
        pattern = re.compile(r'^[A-Za-z0-9_]+$')
        
        for c, b, active in zip(code, businessLine, isActive):
            if not active:
                continue
            if b not in order:
                continue
            if not c or not pattern.match(c):
                continue
            valid.append((order[b], c))
        
        valid.sort()
        return [c for _, c in valid]

# import gcd function from math library
from math import gcd
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # condition_1
        if str1 + str2 != str2 + str1:
            return ""
        
        # gcd_str length
        gcd_len = gcd(len(str1), len(str2))
        
        # return the substring of gcd_len
        return str1[0:gcd_len]


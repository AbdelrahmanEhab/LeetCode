class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        c = dict()

        if (len(s) != len(t)): return False

        for l in s:
            c[l] = 1 + c.get(l, 0)

        for l in t:
            if l not in c or c[l] - 1 < 0:
                return False
            
            c[l] -= 1
        

        return True
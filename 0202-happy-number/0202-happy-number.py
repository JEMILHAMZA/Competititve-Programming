class Solution:
    def isHappy(self, n: int) -> bool:
        c = {n:1}
        while True:
            ns = str(n)
            s = 0
            for i in ns:
                s += (int(i) * int(i))
            if s == 1:
                return True
            elif s in c:
                return False
            else:
                c[s]=1
                n = s
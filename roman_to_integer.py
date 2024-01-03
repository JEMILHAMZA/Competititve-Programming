class Solution:
    def romanToInt(self, s: str) -> int:
        ls1 = []
        store = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        for i in range(len(s) - 1):
            if store[s[i]] >= store[s[i + 1]]:
                ls1.append(store[s[i]])
            else:
                ls1.append(store[s[i + 1]] - store[s[i]])
        ls1.append(store[s[len(s) - 1]])

        ls2 = ls1[::-1]

        result = []
        for i in range(len(ls2) - 1):
            if ls2[i] <= ls2[i + 1]:
                result.append(ls2[i])
        result.append(ls2[len(ls2) - 1])
        
        sum = 0
        for i in result:
            sum += i
        return sum


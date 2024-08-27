class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        p = nums
        c = {0: 1}  
        ans = 0
        current_sum = 0

        for num in p:
            current_sum += num
            if current_sum - k in c:
                ans += c[current_sum - k]
            if current_sum in c:
                c[current_sum] += 1
            else:
                c[current_sum] = 1

        return ans

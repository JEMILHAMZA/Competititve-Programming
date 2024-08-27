class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = 0
        cumulative_sum = 0
        remainder_map = {0: 1} 

        for num in nums:
            cumulative_sum += num
            remainder = cumulative_sum % k
            
           
            if remainder < 0:
                remainder += k
            
            
            if remainder in remainder_map:
                count += remainder_map[remainder]
                remainder_map[remainder] += 1
            else:
                remainder_map[remainder] = 1
        return count

        
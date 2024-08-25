class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
            left = 0
            max_len = 0
            count = 0
            k=1

            for right in range(len(nums)):
                if nums[right] != 1:
                    count += 1

                while count > k:
                    if nums[left] != 1:
                        count -= 1
                    left += 1

                max_len = max(max_len, right - left )

            return max_len

       
  
        
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=0
        max_len=0
        c=0
        

        for right in range(len(nums)):
            if nums[right]!=1:
                c+=1

            while c>k:
                if nums[left]!=1:
                    c-=1
                left+=1
            max_len=max(max_len,right-left+1)

        return max_len

        
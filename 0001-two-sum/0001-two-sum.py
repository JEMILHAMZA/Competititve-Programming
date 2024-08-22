class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        c={}
        for i in range(len(nums)):
            co=target-nums[i]
            if (co) in c:
                return [i,c[co]]
            else:
                c[nums[i]]=i
        
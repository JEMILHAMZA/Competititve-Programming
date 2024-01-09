class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = {}
        result = []
       
        for num in nums:
            if num not in seen:
                result.append(num)
                seen[num] = True
        nums[:len(result)]=result
        return len(result)
        

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        p=nums

        for i in range(1,len(p)):
            p[i]+=p[i-1]
        for i in range(len(nums)):
            if i-1<0:
                if p[len(p) - 1] - p[i] == 0:
                    return i
            else:
                if p[len(p) - 1] - p[i] == p[i-1]:
                    return i
        return -1


        
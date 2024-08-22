class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n  # handle cases where k > n
        def reverse(i, j) -> None:
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1


        
        reverse(0, n - 1)
       
        reverse(0, k - 1)
       
        reverse(k, n - 1)
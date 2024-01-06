class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        n = len(nums)

        for i in range(n - 2):
        # Skip duplicate target elements
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = nums[i]
            left = i + 1
            right = n - 1

            while left < right:
                total = nums[left] + nums[right]
                if total == -target:
                    result.append([target, nums[left], nums[right]])
                # Skip duplicate left and right elements
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    left += 1
                    right -= 1
                elif total < -target:
                    left += 1
                else:
                    right -= 1

        return result

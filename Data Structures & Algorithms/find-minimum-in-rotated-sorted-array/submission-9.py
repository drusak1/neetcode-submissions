class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        if nums[left] <= nums[right]:        
            return nums[0]
        while left < right:
            mid = (left + right + 1) // 2       
            if nums[mid] >= nums[left]:         
                left = mid
            else:
                right = mid - 1
        return nums[(left + 1) % len(nums)]
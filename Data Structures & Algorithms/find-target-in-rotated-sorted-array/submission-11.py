class Solution:
    def bin_search(self, nums, target):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2       
            if nums[mid] == target:         
                return mid
            elif nums[mid] > target:
                right = mid - 1
            else:
                left = mid + 1
        return -1
        
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        if nums[left] <= nums[right]:        
            return self.bin_search(nums,target)

            
        while left < right:
            mid = (left + right + 1) // 2       
            if nums[mid] >= nums[left]:         
                left = mid
            else:
                right = mid - 1
        
        res_left = self.bin_search(nums[:left+1],target)
        res_right = self.bin_search(nums[left+1:],target)
        final_right = res_right + left+1 if res_right != -1 else -1
        return res_left if res_left != -1 else final_right
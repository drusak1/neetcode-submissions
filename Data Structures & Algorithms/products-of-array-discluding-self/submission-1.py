class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        if n == 0:
            return []
        
        left = [1] * n
        right = [1] * n
        output = [1] * n
        
        # Fill left array
        for i in range(1, n):
            left[i] = left[i-1] * nums[i-1]
        
        # Fill right array
        for i in range(n-2, -1, -1):
            right[i] = right[i+1] * nums[i+1]
        
        # Fill output array
        for i in range(n):
            output[i] = left[i] * right[i]
        
        return output
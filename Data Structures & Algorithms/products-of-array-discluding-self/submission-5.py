class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        postfix = [1] * len(nums)
        prefix = [1] * len(nums)
        res = []

        for i in range(1,len(nums)):
            prefix[i] = prefix[i-1] * nums[i-1]
        for i in range(len(nums)-2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i+1]
        
        for i in range(len(nums)):
            res.append(prefix[i] * postfix[i])
        return res


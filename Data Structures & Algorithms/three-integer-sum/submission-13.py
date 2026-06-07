class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sorted_nums = sorted(nums)
        res = []


        for i in range(len(sorted_nums)):
            if i > 0 and sorted_nums[i-1] == sorted_nums[i]:
                continue

            left,right = i+1, len(sorted_nums) - 1

            while left < right:
                curr_num = sorted_nums[i] + sorted_nums[left] + sorted_nums[right]
                if curr_num > 0:
                    right -=1
                elif curr_num < 0:
                    left += 1
                else:
                    res.append([sorted_nums[i], sorted_nums[left], sorted_nums[right]])
                    left += 1
                    right -= 1
                    while sorted_nums[left] == sorted_nums[left-1] and left < right:
                        left += 1
        return res
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        for i,el in enumerate(nums):
            if i > 0 and el == nums[i-1]:
                continue

            left_pointer, right_pointer = i+1, len(nums) - 1

            while left_pointer < right_pointer:
                num = el +nums[left_pointer] + nums[right_pointer]

                if num == 0:
                    res.append([el, nums[left_pointer], nums[right_pointer]])
                    right_pointer -= 1
                    left_pointer += 1
                    while nums[left_pointer] == nums[left_pointer - 1] and left_pointer < right_pointer:
                        left_pointer += 1

                elif num > 0:
                    right_pointer -= 1
                else:
                    left_pointer += 1
        return res
                
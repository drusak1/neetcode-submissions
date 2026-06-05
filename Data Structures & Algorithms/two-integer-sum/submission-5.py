class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev_map = {}

        for i in range(len(nums)):
            if prev_map.get(target - nums[i]) is None:
                prev_map[nums[i]] = i
            else:
                return [prev_map.get(target - nums[i]), i]

        
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] + nums[j] == target:
        #             return [i,j]

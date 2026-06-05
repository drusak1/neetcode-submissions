class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}

        for i,v in enumerate(nums):
            num_map[v] = i

        for i in range(len(nums)):
            if num_map.get(target-nums[i]) is not None and i != num_map.get(target-nums[i]):
                return [i,num_map.get(target-nums[i])]

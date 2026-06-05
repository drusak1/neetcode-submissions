class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = {}
        hash_map[nums[0]] = 0

        for i in range(1,len(nums)):
            diff = target - nums[i]
            if hash_map.get(diff) is not None:
                return [hash_map.get(diff), i]
            hash_map[nums[i]] = i
            


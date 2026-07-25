import heapq

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        arr = []
        res = []

        window_start =- 0
        for window_end in range(len(nums)):
            heapq.heappush(arr, (-nums[window_end],window_end))

            if (window_end - window_start + 1) >= k:
                while arr[0][1] <= window_end - k:
                    heapq.heappop(arr)
                res.append(-arr[0][0])
        return res
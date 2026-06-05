class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque()
        res = []
        window_start = 0
        for window_end in range(len(nums)):
            while q and nums[q[-1]] < nums[window_end]:
                q.pop()
            q.append(window_end)

            if window_start > q[0]:
                q.popleft()
            
            if (window_end+1) >= k:
                res.append(nums[q[0]])
                window_start += 1
        return res
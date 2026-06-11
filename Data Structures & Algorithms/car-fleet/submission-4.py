class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)
        stack = []

        for i in range(len(pair)):
            curr_hours = (target - pair[i][0]) / pair[i][1]
            if len(stack) > 0 and curr_hours <= stack[-1][1] and pair[i][0] < stack[-1][0]:
                continue
            
            stack.append((pair[i][0],curr_hours))
        return len(stack)

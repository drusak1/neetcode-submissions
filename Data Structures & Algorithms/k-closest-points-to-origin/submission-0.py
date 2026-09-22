class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distances =  [(-((x**2 + y**2))**(1/2),(x,y)) for x,y in points ]

        heapq.heapify(distances)

        while len(distances) > k:
            heapq.heappop(distances)

        return [points for distance,points in distances]


class Solution:
    def minmaxGasDist(self, stations: List[int], k: int) -> float:

        stations.sort()

        intervals = []
        for j in range(1, len(stations)):
            intervals.append((-(stations[j] - stations[j-1]), 1))

        heapq.heapify(intervals)

        while k > 0:
            max_dist, parts = heapq.heappop(intervals)
            heapq.heappush(
                intervals, (max_dist * parts / (parts + 1), parts + 1))
            k -= 1

        return -heapq.heappop(intervals)[0]

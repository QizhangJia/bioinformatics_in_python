class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        """
            Runtime: 88 ms, faster than 94.21% of Python3 online submissions for Remove Covered Intervals.
            Memory Usage: 14.8 MB, less than 55.14% of Python3 online submissions for Remove Covered Intervals.
        """

        intervals.sort(key=lambda x: (x[0], -x[1]))

        count = 0

        s0, e0 = float("-inf"), float("-inf")
        for start, end in intervals:
            if start >= s0 and end <= e0:
                continue
            else:
                count += 1
                s0, e0 = start, end

        return count

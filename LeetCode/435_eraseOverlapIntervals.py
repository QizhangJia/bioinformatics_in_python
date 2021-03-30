class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        """
            Runtime: 76 ms, faster than 31.03% of Python3 online submissions for Non-overlapping Intervals.
            Memory Usage: 17.5 MB, less than 13.11% of Python3 online submissions for Non-overlapping Intervals.
        """

        intervals.sort(key=lambda x: x[0])

        prev = float("-inf")
        count = 0
        for start, end in intervals:
            if start >= prev:
                prev = end
                continue
            else:
                prev = min(prev, end)
                count += 1

        return count

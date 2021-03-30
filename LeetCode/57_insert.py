class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        intervals is a sorted list, so insertion sort works best for the new one element.

            Runtime: 68 ms, faster than 98.89% of Python3 online submissions for Insert Interval.
            Memory Usage: 17.4 MB, less than 92.76% of Python3 online submissions for Insert Interval.
        """

        if intervals == []:
            return [newInterval]

        result = []
        new_start, new_end = newInterval

        i = 0
        while i < len(intervals) and intervals[i][1] < new_start:
            result.append(intervals[i])
            i += 1
        # after this while loop, i stops at intervals[i][1] >= new_start

        # resolve merging.
        if i == len(intervals):
            result.append(newInterval)
            return result

        new_start = min(new_start, intervals[i][0])

        while i < len(intervals) and intervals[i][0] <= new_end:
            new_end = max(new_end, intervals[i][1])
            i += 1
        # after this while loop, i stops at intervals[i][0] > new_end
        result.append([new_start, new_end])

        # append remaining items.
        while i < len(intervals):
            result.append(intervals[i])
            i += 1

        return result

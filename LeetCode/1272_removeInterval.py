class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        """
        Runtime: 384 ms, faster than 54.27% of Python3 online submissions for Remove Interval.
        Memory Usage: 20 MB, less than 95.12% of Python3 online submissions for Remove Interval.
        """

        start, end = toBeRemoved

        ans = []
        i = 0

        while i < len(intervals):

            a, b = intervals[i]

            if b <= start or a >= end:
                ans.append(intervals[i])
            elif a < start < end < b:
                ans.extend([[a, start], [end, b]])
            elif a < start < b:
                ans.append([a, start])
            elif a < end < b:
                ans.append([end, b])

            i += 1

        return ans

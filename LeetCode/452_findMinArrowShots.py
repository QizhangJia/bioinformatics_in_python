class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        """
        sort points then find the overlap.

            Runtime: 408 ms, faster than 76.19% of Python3 online submissions for Minimum Number of Arrows to Burst Balloons.
            Memory Usage: 19.5 MB, less than 47.44% of Python3 online submissions for Minimum Number of Arrows to Burst Balloons.
        """

        points.sort(key=lambda x: x[0])

        count = 0
        e1 = float("-inf")
        for s2, e2 in points:
            if s2 > e1:
                # No overlap.
                s1, e1 = s2, e2
                count += 1
            else:
                # Overlap.
                e1 = min(e1, e2)

        return count

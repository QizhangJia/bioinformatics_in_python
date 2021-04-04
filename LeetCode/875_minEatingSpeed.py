class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        binary search.
        """
        lower = math.ceil(sum(piles) / h)
        upper = max(piles)
        # lower could be a solution,
        # upper must be a solution.

        while lower < upper:
            mid = (lower + upper) // 2
            hours = sum([math.ceil(i / mid) for i in piles])
            if hours > h:
                lower = mid + 1
            else:
                upper = mid

        return upper

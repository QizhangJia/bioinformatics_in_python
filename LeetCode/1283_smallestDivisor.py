class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:

        upper = max(nums)
        lower = 1

        def isBelowThreshold(divisor: int) -> bool:
            total = 0
            for num in nums:
                total += math.ceil(num / divisor)
            return total <= threshold

        # upper is a solution, lower may not be a solution.
        while lower < upper:
            mid = lower + (upper - lower) // 2
            if isBelowThreshold(mid):
                upper = mid
            else:
                lower = mid + 1

        return upper

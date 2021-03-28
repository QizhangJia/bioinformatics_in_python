class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        
        """
        Two pointers.
        """
        i = j = k
        
        curr_min = nums[k]
        n = len(nums)
        
        optimal = nums[k]
        
        while True:
            if i == 0 and j == (n-1):
                break
                
            # No left or right is larger, move right.
            if i == 0:
                j += 1
                if nums[j] < curr_min:
                    curr_min = nums[j]
                
                optimal = max(optimal, curr_min * (j-i+1))
            # No right or left is larger, move left.
            elif j == (n-1) or nums[j+1] < nums[i-1]:
                i -= 1
                if nums[i] < curr_min:
                    curr_min = nums[i]
                optimal = max(optimal, curr_min * (j-i+1))
            else:
                j += 1
                if nums[j] < curr_min:
                    curr_min = nums[j]
                optimal = max(optimal, curr_min * (j-i+1))
                
        return optimal
                
            
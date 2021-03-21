class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        
        slots1.sort()
        slots2.sort()
        
        p1 = 0
        p2 = 0
        
        m = len(slots1)
        n = len(slots2)
        
        while p1 < m and p2 < n:
            s1, e1 = slots1[p1]
            s2, e2 = slots2[p2]
            
            if min(e1, e2) - max(s1, s2) >= duration:
                return [max(s1, s2), max(s1, s2) + duration]
            
            if e1 >= e2:
                p2 += 1
            else:
                p1 += 1
                
        return []
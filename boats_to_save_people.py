class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        minimum_boat_number = 0
        a = sorted(people, reverse=True)
        while a:
            if a[0] + a[-1] <= limit and len(a) > 1:
                minimum_boat_number += 1
                del(a[0])
                del(a[-1])
            else:
                minimum_boat_number += 1
                del(a[0])

            
        return minimum_boat_number

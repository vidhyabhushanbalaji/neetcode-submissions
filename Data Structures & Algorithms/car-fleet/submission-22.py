class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        sort_by_pos = [[p,s] for p,s in zip(position, speed)]
        sort_by_pos.sort(reverse=True)

        fleets = 0
        fastest_arrival_time = float("-infinity")

        for pos, speed in sort_by_pos:
            arrival_time =(target-pos)/speed
            if arrival_time>fastest_arrival_time:
                fastest_arrival_time = arrival_time
                fleets+=1
        
        return fleets
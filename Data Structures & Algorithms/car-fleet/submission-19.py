class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [[p,s] for p,s in zip(position, speed)]
        pairs.sort(reverse=True)
        
        best_time = 0
        fleets = 0

        for i in pairs:
            time = (target-i[0])/i[1]
            if time>best_time:
                best_time = time
                fleets+=1
        return fleets
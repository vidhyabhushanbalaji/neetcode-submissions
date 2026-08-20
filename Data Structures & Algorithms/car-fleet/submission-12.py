class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position, speed)]
        pair = sorted(pair)

        top=-1
        count=0

        for i in range(len(pair)-1, -1, -1):
            time = (target-pair[i][0])/pair[i][1]
            if time>top or top==-1:
                count+=1
                top = time
        return (count)
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p,s] for p,s in zip(position, speed)]
        pair = sorted(pair)

        top=(target-pair[-1][0])/pair[-1][1]
        count=1

        for i in range(len(pair)-1, -1, -1):
            time = (target-pair[i][0])/pair[i][1]
            if time>top:
                count+=1
                top = time
        return (count)
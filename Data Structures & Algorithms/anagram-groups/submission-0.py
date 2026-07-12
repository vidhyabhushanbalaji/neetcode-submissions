class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}
        for i in strs:
            x = ''.join(sorted(i))
            if x in grouped:
                grouped[x].append(i)
            else:
                grouped[x] = [i]
        empty = []
        for i in grouped:
            empty.append(grouped[i])
        return empty
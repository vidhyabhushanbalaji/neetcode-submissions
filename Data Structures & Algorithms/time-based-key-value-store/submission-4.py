class TimeMap:

    def __init__(self):
        self.mainMap = {}
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.mainMap:
            self.mainMap[key].append(value)
            self.timeMap[key].append(timestamp)
        else:
            self.mainMap[key] = [value]
            self.timeMap[key] = [timestamp]

    def get(self, key: str, timestamp: int) -> str:
        arr = self.timeMap.get(key, None)
        if arr:
            if timestamp>arr[-1]:
                return self.mainMap[key][-1]
            elif timestamp<arr[0]:
                return ""

            left = 0
            right = len(arr)-1
            while left<=right:
                if arr[left]>timestamp:
                    if left>0:
                        return self.mainMap[key][left-1]
                    else:
                        return ""
                elif arr[right]<timestamp:
                    return self.mainMap[key][left]
                
                mid = (left+right)//2
                if arr[mid]==timestamp:
                    return self.mainMap[key][mid]
                elif timestamp>arr[mid]:
                    left = mid+1
                else:
                    right = mid-1
        return ""
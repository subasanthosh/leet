class TimeMap:

    def __init__(self):
        self.objs = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.objs:
            self.objs[key] = []

        self.objs[key].append([timestamp,value])


    def get(self, key: str, timestamp: int) -> str:
        if key not in self.objs:
            return ""

        pairs = self.objs[key]
        low = 0
        high = len(pairs)-1
        res = ""

        while low<=high:
            mid = (low+high)//2
            mid_time = pairs[mid][0]
            mid_value = pairs[mid][1]
            if mid_time==timestamp:
                return mid_value

            if mid_time > timestamp:
                high = mid-1

            elif mid_time < timestamp:
                res = mid_value
                low = mid+1 
        return res

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
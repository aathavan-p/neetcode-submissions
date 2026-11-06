class MedianFinder:

    def __init__(self):
        self.small, self.large = [], []
        
    def addNum(self, num: int) -> None:
        heapq.heappush(self.small, -1 * num)

        #check if every element in small is smaller than elements in large
        if (self.small and self.large and -1 * self.small[0] > self.large[0]):
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        #check if diff of length of small and large is not greater than 1
        if len(self.small) > len(self.large)+1:
            val = -1 * heapq.heappop(self.small)
            heapq.heappush(self.large, val)
        
        if len(self.large) > len(self.small) + 1:
            val = -1 * heapq.heappop(self.large)
            heapq.heappush(self.small, val)

    def findMedian(self) -> float:
        if len(self.small) > len(self.large):
            return -1 * self.small[0]
        if len(self.large) > len(self.small):
            return self.large[0]
        
        return ((-1 * self.small[0]) + self.large[0]) / 2
        
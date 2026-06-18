class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        
        heap = [(-freq, val) for val, freq in counter.items()]
        heapq.heapify(heap)
        
        result = []
        for _ in range(k):
            freq, val = heapq.heappop(heap)
            result.append(val)
        
        return result
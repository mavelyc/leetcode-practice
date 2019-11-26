import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ref = collections.Counter(nums)
        return heapq.nlargest(k, ref.keys(), key=ref.get)
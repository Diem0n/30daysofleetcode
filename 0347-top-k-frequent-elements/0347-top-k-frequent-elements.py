class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = Counter(nums)
        buckets = [[] for _ in range(len(nums) + 1)]
        for num, freq in freq_map.items():
            buckets[freq].append(num)
        top_k = []
        for i in range(len(buckets) - 1, 0, -1):
            top_k.extend(buckets[i])
            if len(top_k) >= k:
                break
        return top_k[:k]
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # since it is a top k and we don't need to worry about if k is too large
        # we want to have a list of tuples as (frequency, value)
        # then use a heap to find the top k
        count = {}
        for num in nums:
            if num not in count:
                count[num] = 1
            else:
                count[num] += 1
        print(count)
        heap = []
        for num in count:
            heapq.heappush(heap, (count[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        result = []
        for i in heap:
            result.append(i[1])
        return result
        
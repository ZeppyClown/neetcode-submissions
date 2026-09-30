class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = {}

        for num in nums:
            if num not in frequent:
                frequent[num] = 0
            frequent[num] += 1

        bucket = [[] for i in range(len(nums) + 1)]

        for num, count in frequent.items():
            bucket[count].append(num)
        

        result = []
        
        for i in range(len(bucket) - 1, 0, -1):
            for num in bucket[i]:
                result.append(num)
                if len(result) == k:
                    return result
            
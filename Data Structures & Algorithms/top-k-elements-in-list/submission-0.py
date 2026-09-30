class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequent = {}

        for num in nums:
            if num not in frequent:
                frequent[num] = 0
            frequent[num] += 1
        
            
            
        return sorted(frequent, key=lambda n: frequent[n], reverse=True)[:k]
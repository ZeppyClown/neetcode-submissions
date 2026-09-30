class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            complete = ''.join(sorted(word))
            if complete not in groups:
                groups[complete] = []
            groups[complete].append(word)
        return list(groups.values())

    

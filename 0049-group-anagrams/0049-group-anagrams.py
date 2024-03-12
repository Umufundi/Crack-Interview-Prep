class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for s in strs:
            key = "".join(sorted(s))
            exists = groups.get(key)
            if exists:
                exists.append(s)
                groups[key] = exists
            else:
                groups[key] = [s]
        return groups.values()
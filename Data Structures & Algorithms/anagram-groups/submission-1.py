class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            sortedd = ''.join(sorted(s))
            res[sortedd].append(s)
        return list(res.values())
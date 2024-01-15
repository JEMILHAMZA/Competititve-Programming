class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mapp = defaultdict(list)
        ans=[]
        for s in strs:
            sorted_s=tuple(sorted(s))
            mapp[sorted_s].append(s)
        for item in mapp.values():
            ans.append(item)
        return ans


from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = dict()

        for s in strs:
            ss = tuple(sorted(s))
            if ss in list(hashmap.keys()):
                hashmap[ss].append(s)
            else:
                hashmap[ss] = [s]

        return list(hashmap.values())
        
from typing import List

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        res = []

        for j in range(len(words)):
            for k in range(len(words)):
                if words[j] == words[k]:
                    continue
                elif words[j] in words[k] and words[j] not in res:
                    res.append(words[j])
                else:
                    continue
        
        return res
        
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ''
        
        ans = ''
        compare = min(strs,key=len)

        for i in range(len(compare)):
            for word in strs:
                if word[i] != compare[i]:
                    return ans
            ans+=compare[i]
        return ans
        
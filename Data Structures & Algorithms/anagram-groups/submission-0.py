class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        master_dict = {}
        signature_key = ''

        for i in range (len(strs)):
            signature_key = ''.join(sorted(strs[i]))
            if signature_key in master_dict:
                master_dict[signature_key].append(strs[i])
            else:
                master_dict[signature_key] = [strs[i]]
        return list(master_dict.values())
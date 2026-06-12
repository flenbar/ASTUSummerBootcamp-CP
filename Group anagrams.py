class Solution(object):
    def groupAnagrams(self, strs):
        dictionary = {}
        for i in strs:
            if b not in dictionary:
                dictionary[b] = []
            dictionary[b].append(i)
        return list(dictionary. values()) 
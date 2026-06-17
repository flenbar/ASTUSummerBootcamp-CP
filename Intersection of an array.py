class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        result = []
        Nums1 = list(set(nums1))
        Nums2 = list(set(nums2))
        for i in range(len(Nums1)):
            for j in range(len(Nums2)):
                if Nums1[i] == Nums2[j]:
                    result.append(Nums1[i])       
        return result
        


       
        
                   
        

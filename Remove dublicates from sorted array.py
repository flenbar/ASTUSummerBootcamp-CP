class Solution(object):
    def removeDuplicates(self, nums):
        my_list = []
        for i in nums:
            if i not in my_list:
                my_list.append(i)
        for j in range(len(my_list)):
            nums[j] = my_list[j]
        return len(my_list)    


        
        

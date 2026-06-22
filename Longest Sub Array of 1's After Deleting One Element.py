class Solution:
    def longestSubarray(self, nums):
        left = 0
        removen = 0
        best = 0
        for right in range(len(nums)):
            if nums[right] == 0:
                removen += 1
            while removen  > 1:
                if nums[left] == 0:
                    removen -= 1
                left += 1
            best = max(best, right - left)
        return best

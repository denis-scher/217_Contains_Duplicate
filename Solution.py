class Solution:
    # Easy Nested loop solution:
    def containsDuplicateEasy(self, nums) -> bool:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
    
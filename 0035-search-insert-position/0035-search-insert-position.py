class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        k=-1
        for num in nums:
            k += 1
            if target == num:
                return nums.index(num)
            elif target < num:
                return k
        return k+1


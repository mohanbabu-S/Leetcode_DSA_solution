class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lef, rig = 0, len(nums) - 1

        while lef <= rig:
            mid = (lef + rig) // 2
            if target == nums[mid]:
                return mid

            # left sorted portion
            if nums[lef] <= nums[mid]:
                if target > nums[mid] or target < nums[lef]:
                    lef = mid + 1
                else:
                    rig = mid - 1
            # right sorted portion
            else:
                if target < nums[mid] or target > nums[rig]:
                    rig = mid - 1
                else:
                    lef = mid + 1
        return -1
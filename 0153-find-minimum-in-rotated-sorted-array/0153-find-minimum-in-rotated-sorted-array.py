class Solution:
    def findMin(self, nums: List[int]) -> int:
        fi_start , la_end = 0, len(nums) - 1 
        curr_min = float("inf")
        
        while fi_start  <  la_end :
            mid = fi_start + (la_end - fi_start ) // 2
            curr_min = min(curr_min,nums[mid])
            
            # right has the min 
            if nums[mid] > nums[la_end]:
                fi_start = mid + 1
                
            # left has the  min 
            else:
                la_end = mid - 1 
                
        return min(curr_min,nums[fi_start])